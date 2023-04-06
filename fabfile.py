"""
TAREAS AUTOMATIZADAS

Requerimientos:
    - sudo apt install python3-pip
    - pip3 install fabric==3.0   Nota: funciona en python 3.6
    - pip3 install -U python-dotenv
    - source ~/.profile
"""

import os
from fabric import Connection, Config, task
from invoke import Responder
from dotenv import load_dotenv
from pathlib import Path
from getpass import getpass


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(os.path.join(BASE_DIR, '.env'))


##################### VARIABLES REQUERIDAS ######################
SERVER_NAME     = os.getenv('SERVER_NAME')
SERVER_APP_PATH = os.getenv('SERVER_APP_PATH')
DB_USER         = os.getenv('DB_USER')
DB_NAME         = os.getenv('DB_NAME')
DB_BACKUP_FOLDER     = os.getenv('DB_BACKUP_FOLDER')
SERVER_DB_FILE_PAHT  = os.path.join(SERVER_APP_PATH, DB_BACKUP_FOLDER, 'db.sql')
LOCAL_DB_FILE_PAHT   = os.path.join(BASE_DIR, DB_BACKUP_FOLDER, 'db.sql')
DB_DATA_FOLDER       = os.getenv('DB_DATA_FOLDER')
LOCAL_MEDIA_ROOT           = os.path.join(BASE_DIR, 'public/media')

##################### CONECTIONS ######################
#fabic conexion
ssh_pass = getpass("ssh password:")
con = Connection(host=SERVER_NAME, connect_kwargs={"passphrase": ssh_pass})



##################### ACTUALIZAR DEV ###########################
"""
1. Sincronizar db
2. Sincronizar Archivos 
3. Actualizar repositorio
"""

# fabric crear tarea con ventana de confirmación
@task
def hola(c):
    print(os.path.join(DB_DATA_FOLDER, '*'))

@task 
def syncdb(c): 
    # dump server db
    con.run(f'cd {SERVER_APP_PATH} && \
             docker-compose -f deploy.yml exec postgres sh -c \
             "pg_dump -Fp -b -U {DB_USER} {DB_NAME}" \
             > {SERVER_DB_FILE_PAHT}', pty=True)
    
    # descargar db
    con.get(SERVER_DB_FILE_PAHT, LOCAL_DB_FILE_PAHT)

    # delete server db file
    con.run(f'rm {SERVER_DB_FILE_PAHT}')

    # delete dbdata files
    local_db_files = os.path.join(DB_DATA_FOLDER, '*')
    con.local(f'sudo rm -rf {DB_DATA_FOLDER}' )

    # recreate postgres container
    con.local(f'docker-compose up --force-recreate -d postgres')
              
@task
def syncmedia(c):
    # download media files
    # https://linux.die.net/man/1/rsync
    con.local(f'rsync -auvzP -e ssh --delete --exclude="/tmp/" --exclude=".gitignore" \
               {SERVER_NAME}:{SERVER_APP_PATH}/public/media/ {LOCAL_MEDIA_ROOT}', pty=True)

