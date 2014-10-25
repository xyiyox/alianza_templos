from fabric.api import * 
from fabric.contrib.console import confirm
from fabric.colors import green, red, yellow

from contextlib import contextmanager as _contextmanager

import os
import re

try:
  import private # llamamos un private file con variables estaticas 
except ImportError:
  print 'no se encuentran los datos privados'
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
		run('source ../bin/activate && ./manage.py syncdb --no-initial-data')
		run('source ../bin/activate && ./manage.py migrate')

def reiniciar_servidor():
	with cd('/home/alianza/webapps/alianza_templos/apache2'):
		run('bin/restart')

#####################################################################
########				SERVIDOR DE DESARROLLO				#########
#####################################################################

# def test():
# 	#local('git log --oneline --graph --decorate')
# 	with cd('/home/alianza/webapps/alianza_templos'):
# 		run('source bin/activate')

# def django_manage(command='help', virtualenv='alianza_templos'):
# 	return "/bin/bash -l -c 'source ~/env/alianza_templos/bin/activate && pip freeze'"  %(virtualenv, command)

# @_contextmanager
# def virtualenv():
# 	with lcd('/home/yiyo/env/alianza_templos/'):
# 		with prefix('source bin/activate'):
# 			yield

# def deploy():
# 	with virtualenv():
# 		local('pip freeze')

def git_log():
	with cd(PROD_PATH):
		run('git log')