#!/usr/bin/env python
import exifread
from dateutil.parser import parse
import datetime
from dateutil import tz


def exif(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    return tags


def exif_time(path):
    ex = exif(path)
    dtstr = ex.get('Image DateTime')
    if dtstr is None:
        return None
    else:
        dt = datetime.datetime.strptime(dtstr.values, "%Y:%m:%d %H:%M:%S")
        dt = dt.astimezone(tz.tzlocal())
        return dt


if __name__ == '__main__':
    t = exif_time('d:/a2.jpg')
    print(t)
