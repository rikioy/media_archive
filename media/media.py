#!/usr/bin/env python
from dateutil.parser import parse
from dateutil import tz
import ffmpeg


def meta_time(path):
    m = meta(path)
    dtstr = m.get('format').get('tags').get('creation_time')
    if dtstr is None:
        return None
    else:
        dt = parse(dtstr)
        dt = dt.astimezone(tz.tzlocal())
        return dt


def meta(path):
    j = ffmpeg.probe(path)
    return j


if __name__ == '__main__':
    m = meta_time('d:/v1.mp4')
    print(m.__str__())


