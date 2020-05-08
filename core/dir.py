import os
import datetime
import util.str
import shutil


def mkdir_by_date(dst, dt):
    path = os.path.join(dst, str(dt.year), str(dt.month), str(dt.day))
    os.makedirs(path, exist_ok=True)
    return path


def copyfile(src, dst, filename, ext):
    path = os.path.join(dst, filename + ext)
    while os.path.exists(path):
        path = os.path.join(dst, filename + '-' + util.str.rand_str(4) + ext)
    shutil.copyfile(src, path)


if __name__ == '__main__':
    mkdir_by_date('d:/test/', datetime.datetime.now())
