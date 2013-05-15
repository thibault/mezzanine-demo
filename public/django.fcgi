#!/usr/bin/python
import os, sys

venv_file = '/home/mezzanine/.virtualenvs/mezzanine/bin/activate_this.py'              
if os.path.isfile(venv_file):                                                   
    execfile(venv_file, dict(__file__=venv_file))

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PROJECT_DIR)
sys.path.insert(0, os.path.dirname(_PROJECT_DIR))

_PROJECT_NAME = _PROJECT_DIR.split('/')[-1]
os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % _PROJECT_NAME

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
