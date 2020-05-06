#!/usr/bin/env python
import exifread
from dateutil.parser import parse


def exif(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    return tags


def exif_time(path):
    ex = exif(path)
    dtstr = ex['EXIF DateTimeOriginal']
    dt = parse(dtstr.values)
    return dt


if __name__ == '__main__':
    t = exif_time('d:/a2.jpg')
    print(t)
