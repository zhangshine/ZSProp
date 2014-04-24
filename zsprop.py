#!/usr/bin/env python
import os
import sys
import shutil

HOME_PATH = os.path.expanduser('~')
HOME_PATH_LEN = len(HOME_PATH)
EXE_PATH, EXE_NAME = os.path.split(os.path.abspath(sys.argv[0]))
EXE_NAME = os.path.basename(EXE_NAME)
FILE_LIST_FILE_PATH = 'file_list.conf'


def __file_path(file_path):
    src_file_path = os.path.expanduser(file_path.strip())
    bak_file_path = os.path.join(EXE_PATH, 'files', src_file_path[HOME_PATH_LEN+1:])
    return src_file_path, bak_file_path


def update():
    with open(FILE_LIST_FILE_PATH) as f:
        for file_path in f:
            src_file_path, bak_file_path = __file_path(file_path)
            shutil.copy(src_file_path, bak_file_path)


def install():
    with open(FILE_LIST_FILE_PATH) as f:
        for file_path in f:
            dst_file_path, bak_file_path = __file_path(file_path)
            shutil.copy(bak_file_path, dst_file_path)


def usage():
    print('Usage:')
    print('    {exe_name} [install|update]'.format(exe_name=EXE_NAME))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(-1)

    fn = {
        'update': update,
        'install': install
    }

    cmd = sys.argv[1]
    fn.get(cmd, usage)()