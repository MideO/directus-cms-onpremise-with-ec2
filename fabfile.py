# -*- coding: utf-8 -*-
# Fabric  deploy script
# Supported Python version python 2.X
# Prerequisites
# pip see: https://pip.pypa.io/en/latest/installing/#install-or-upgrade-pip
# fabric see: http://www.fabfile.org/
# Amazon AWS Docker Image - aws-elasticbeanstalk-amzn-2016.09.1.x86_64-docker-hvm-201703022213 - ami-0cf1e468
# Helper shell scripts in bin directory at project root
#   bin
#   ├── kill-all-dockers
#   ├── start
#   └── store-archive
#  
# Environment variables of ec2 instanecs host names
# SSH_USER - ec2 user
# SSH_HOSTS - ec2 instances as a comma seperated string
# SSH_KEY_FILE_NAME  - Path to ssh key(pem file usually)


from fabric.api import local, cd, env, parallel
from fabric.operations import run, put, sudo
import os


APP = 'directus' #Name of app to be deployed

APP_ARTIFACT = '{0}.zip'.format(APP)
APP_ARTIFACT_DIST = 'dist/{0}'.format(APP_ARTIFACT)
CREATE_ARCHIVE_COMMAND = "./bin/store-archive"
REMOVE_APP_FILES = 'rm -rf {0}/*'.format(APP)
REMOVE_APP_ARTIFACT = 'rm {0}'.format(APP_ARTIFACT)

EC_USER_HOME = '~'
EC_UNZIP_APP = 'unzip {0} -d {0}'.format(APP)
EC_MAKE_APP_DIRECTORY = 'mkdir -p {0}'.format(APP)

EC_KILL_DOCKERS_COMMAND = 'bin/kill-all-dockers'
EC_START_APP = 'bin/start'

env.user = os.getenv('SSH_USER', 'ec2-user')
hosts = os.getenv('SSH_HOSTS')
if hosts != None:
    env.hosts = hosts

env.key_filename = os.getenv('SSH_KEY_FILE_NAME')

def deploy():
    local(CREATE_ARCHIVE_COMMAND)
    run(EC_MAKE_APP_DIRECTORY)
    put(APP_ARTIFACT_DIST, EC_USER_HOME)
    run(REMOVE_APP_FILES)
    run(EC_UNZIP_APP)
    run(REMOVE_APP_ARTIFACT)

    with cd(APP):
        sudo(EC_KILL_DOCKERS_COMMAND)    
        sudo(EC_START_APP)
