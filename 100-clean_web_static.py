#!/usr/bin/python3
'''Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives'''
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['54.86.220.207', '54.175.137.217']


@runs_once
def do_pack():
    """Create a compressed archive of the web_static directory.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cu_ti = datetime.now()
    opt = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cu_ti.year,
        cu_ti.month,
        cu_ti.day,
        cu_ti.hour,
        cu_ti.minute,
        cu_ti.second
    )
    try:
        print("Packing web_static to {}".format(opt))
        local("tar -cvzf {} web_static".format(opt))
        arc_si = os.stat(opt).st_size
        print("web_static packed: {} -> {} Bytes".format(opt, arc_si))
    except Exception:
        opt = None
    return opt


def do_deploy(archive_path):
    """Deploy the web files to a remote server.

    Args:
        archive_path (str): Path to the web archive file.
    """
    if not os.path.exists(archive_path):
        return False
    file_n = os.path.basename(archive_path)
    folder_n = file_n.replace(".tgz", "")
    folder_p = "/data/web_static/releases/{}/".format(folder_n)
    suc = False
    try:
        put(archive_path, "/tmp/{}".format(file_n))
        run("mkdir -p {}".format(folder_p))
        run("tar -xzf /tmp/{} -C {}".format(file_n, folder_p))
        run("rm -rf /tmp/{}".format(file_n))
        run("mv {}web_static/* {}".format(folder_p, folder_p))
        run("rm -rf {}web_static".format(folder_p))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_p))
        print('New version deployed!')
        suc = True
    except Exception:
        suc = False
    return suc


def deploy():
    """Package and deploy web files.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False


def do_clean(number=0):
    """Remove old versions of web_static archives and releases.
    """
    arch = os.listdir('versions/')
    arch.sort(reverse=True)
    start = int(number)
    if not start:
        start += 1
    if start < len(arch):
        arch = arch[start:]
    else:
        arch = []
    for ar in arch:
        os.unlink('versions/{}'.format(ar))
    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    ]
    run(''.join(cmd_parts))
