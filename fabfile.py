from fabric.api import * 
from fabric.contrib.console import confirm
from fabric.colors import green, red, yellow

from contextlib import contextmanager as _contextmanager

import os
import re

try:
 	# llamamos un private file con variables estaticas 
	import private
except ImportError:
	print('no se encuentran los datos privados')
	pass 

RUTA_PROYECTO = os.path.join(os.path.dirname(os.path.abspath(__file__)))
env.hosts = [private.HOST1]
PROD_PATH = private.PROD_PATH
ENV = 'alianza_templos'

POSTGRESQL_PATH  = private.POSTGRESQL_PATH
DB_BACKUP_PATH   = private.DB_BACKUP_PATH
DB_BACKUP_FILE   = private.DB_BACKUP_FILE
DB_PROD_USER     = private.DB_PROD_USER
DB_PROD_NAME     = private.DB_PROD_NAME
DB_DEV_USER      = private.DB_DEV_USER
DB_DEV_NAME      = private.DB_DEV_NAME



#####################################################################
########				SERVIDOR DE PRODUCCION				#########
#####################################################################

def deploy():
	update_code()
	actualizar_requerimientos()
	colectar_estaticos()
	sincronizar_bd()
	#actualizar_default_data
	reiniciar_servidor()

def update_code():
	print(green('Actualizando repositorio central...'))
	local('git push origin master')

	print(green('Actualizando repositorio de produccion...'))
	with cd(PROD_PATH):
		run('git pull')

def actualizar_requerimientos():
	with cd(PROD_PATH):
		run('source ../bin/activate && pip install -r requirements.txt')

def colectar_estaticos():
	with cd(PROD_PATH):
		run('source ../bin/activate && ./manage.py collectstatic --noinput')
 	#collectstatic()

def sincronizar_bd():
	with cd(PROD_PATH):
		#run('source ../bin/activate && ./manage.py syncdb --no-initial-data')
		run('source ../bin/activate && ./manage.py migrate')

def actualizar_default_data():
	with cd(PROD_PATH):
		run('source ../bin/activate && ./manage.py loaddata auth_data.json')

def reiniciar_servidor():
	with cd('/home/alianza/webapps/alianza_templos/apache2'):
		run('bin/restart')

#####################################################################
########				SERVIDOR DE DESARROLLO				#########
#####################################################################

def consolidar_local():
	consolidar_requirements()
	#update_default_data()
	verificar_status_repo()
	commit()

def actualizar_db_local():
	if not confirm(yellow("ANTES ELIMINE TODAS LAS TABLAS EN LOCAL, SI YA LO HIZO CONTINUE")):
		abort('Abortado por el usuario')
	print 'Adelante ...'

	with cd(DB_BACKUP_PATH):
		run('rm -f %s' % DB_BACKUP_FILE)		
		run('%s/pg_dump -Fp -b -U %s %s > %s/%s' %(POSTGRESQL_PATH, DB_PROD_USER, DB_PROD_NAME, DB_BACKUP_PATH, DB_BACKUP_FILE) )  # -Fp: formato plane text, -b: include large objects
		local('rm -f %s' % DB_BACKUP_FILE)
		local('scp %s:%s/%s %s' %(env.hosts[0], DB_BACKUP_PATH, DB_BACKUP_FILE, DB_BACKUP_FILE))
		run('rm -f %s' % DB_BACKUP_FILE)

	local('psql -U %s -d %s -f %s' %(DB_DEV_USER, DB_DEV_NAME, DB_BACKUP_FILE))


def git_log():
	local('git log --oneline --graph --decorate')

def update_default_data():
	local('./manage.py dumpdata auth --natural-foreign --natural-primary --indent 4  > auth_data.json')

def load_default_data():
	local('./manage.py loaddata auth_data.json')


def consolidar_requirements():
	local('pip freeze > requirements.txt')

def verificar_status_repo():
	local('git status') 
	if not confirm(yellow("status verificado, desea continuar?")):
		abort('Abortado por el usuario')
	print 'Adelante ...'

def commit():
	local('git add . && git commit -a')

FFMPEG_EXE = '~/bin/ffmpeg'

def gource():
	local('gource  --title "Alianza Templos" --logo main/static/main/img/logo.png --key -s 1')

def gource_record():
	local('gource --title "Alianza Templos" --logo main/static/main/img/logo.png --key --seconds-per-day 1 -640x360 -o - | %s -y -r 60 -f image2pipe -vcodec ppm -i - -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 gource.mp4' %FFMPEG_EXE) 
