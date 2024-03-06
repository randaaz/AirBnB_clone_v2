#!/usr/bin/python3
"""Fabric script for deploying web files to a server.
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.86.220.207', '54.175.137.217']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
        """Deploy web files to the server using rsync.
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                put(archive_path, '/tmp/')

                tt = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(tt))

                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(tt, tt))

                run('sudo rm /tmp/web_static_{}.tgz'.format(tt))

                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(tt, tt))

                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(tt))

                run('sudo rm -rf /data/web_static/current')

                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(tt))
        except:
                return False

        return True
