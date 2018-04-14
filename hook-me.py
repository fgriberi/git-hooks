#!/usr/bin/env python
"""
Python script to install git hooks from git-hooks repository

install
-------

curl -S https://raw.githubusercontent.com/fgriberi/git-hooks/master/hook-me.py | python
"""

import os
import sys
import stat
import shutil
import subprocess

BASE_URL = 'https://raw.githubusercontent.com/fgriberi/git-hooks/master'
GIT_HOOKS_PATH = '.git/hooks'
BACKUP_EXT = '.bkp'
SUCCESS_CODE = 0
ERROR_CODE = -1


def run_cmd(cmd):
    """Runs command as sub-process
    :param cmd: the command to execute
    :ptype cmd: str
    :return the process return code
    :raise subprocess.CalledProcessError: if call process fail
    """
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    try:
        stdout, stderr = proc.communicate()
    except subprocess.CalledProcessError as exc:
        error_msg = '\033[31m[ERROR]: output = {out}, error code = {code}\033[39m'
        sys.stderr.write(error_msg.format(out=exc.output, code=exc.returncode))

    if proc.returncode != 0:
        error_msg = '\033[31mFailed running "{cmd}"'
        error_msg += "\n{err}" if len(stderr) != 0 else ""
        error_msg += "\n{out}" if len(stdout) != 0 else ""
        print(error_msg.format(
            cmd=cmd,
            err=stderr.decode('utf-8'),
            out=stdout.decode('utf-8'))
        )
    return proc.returncode


def is_git_directory(path='.'):
    """Checks if given path is a git directory
    :param path: a specific path
    :ptype path: str
    """
    git_st_ret_code = run_cmd('git -C {path} status'.format(path=path))
    return git_st_ret_code == SUCCESS_CODE


def backup_hook(hook_file):
    """Creates a backup of given hook file
    :param hook_file: a git hook file path
    :ptype hook_file: str
    """
    backup_file = hook_file + BACKUP_EXT
    msg = "\033[33mBacking up {hook_file} in {backup_file}\033[39m"
    print(msg.format(hook_file=hook_file, backup_file=backup_file))
    shutil.copy2(hook_file, backup_file)


def remote_hook_file_exist(remote_file_path):
    """Checks if given remote file exists
    :param remote_file_path: a remote file path
    :ptype remote_file_path: str
    """
    curl_cmd = "curl -fs {remote_file}".format(remote_file=remote_file_path)
    status = run_cmd(curl_cmd)
    return status == SUCCESS_CODE


def download_hook(source, destination):
    """Downloads the hook from source and put it in a destination
    :param source: remote hook path
    :ptype source: str
    :param destination: local destination path
    :ptyoe destination: str
    """
    curl_cmd = "curl -s {remote_url} > {local_path}".format(
        remote_url=source, local_path=destination)
    run_cmd(curl_cmd)

    # set executable permissions
    st = os.stat(destination)
    os.chmod(destination, st.st_mode | stat.S_IEXEC)


def install_hook(hook_name):
    """Install a specific git hook from git-hook repository
    :param hook_name: the git hook name to install
    :ptype hook_name: str
    """
    remote_hook_file = os.path.join(BASE_URL, hook_name)
    if remote_hook_file_exist(remote_hook_file):

        local_hook_file = os.path.join(GIT_HOOKS_PATH, hook_name)
        if os.path.exists(local_hook_file):
            print("\033[31m{hook_name} already exist.\033[39m".format(hook_name=hook_name))
            backup_hook(local_hook_file)

        download_hook(remote_hook_file, local_hook_file)
        print("\033[32m{hook_name} hook installed.\033[39m".format(hook_name=hook_name))
    else:
        print("\033[31mRemote file not found {file_url}.\033[39m".format(file_url=remote_hook_file))


if is_git_directory():
    install_hook('pre-commit')
    install_hook('prepare-commit-msg')
