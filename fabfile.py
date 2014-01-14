import os

from fabric.api import run, cd
from fabric.api import local

def host_type():
    run('uname -s')
    run('uptime')

def deploy_keystone():
    if not os.path.exists("/opt/stack/"):
        with cd("/opt/stack/"):
            local("git clone http://github.com/openstack/keystone.git")
    cd("keystone")
    local("virtualenv keystone")
    local("source /opt/stack/keystone/venv/bin/activate && pip install -r requirements.txt")