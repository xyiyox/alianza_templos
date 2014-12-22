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

#####################################################################
########				SERVIDOR DE PRODUCCION				#########
#####################################################################

def deploy():
	update_code()
	actualizar_requerimientos()
	colectar_estaticos()
	sincronizar_bd()
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

def default_data():
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
	update_default_data()
	verificar_status_repo()
	commit()

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
