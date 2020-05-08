import hashlib
import os
from util.log import Log


def md5file(path, size=5000000):
    stat = os.stat(path)
    data = b''
    f = open(path, 'rb')
    if stat.st_size > size:
        data = f.read(size)
    else:
        data = f.read()
    f.close()
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()


def md5str(s_md5):
    m = hashlib.md5()
    m.update(s_md5.encode("utf-8"))
    token = m.hexdigest()
    return token


if __name__ == '__main__':
    log = Log()
    log.debug("testlog")

    print(md5file('d:/v1.mp4'))
    print(md5str("aaa"))
