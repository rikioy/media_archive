#!/usr/bin/env python
from dateutil.parser import parse
import ffmpeg


def meta_time(path):
    m = meta(path)
    dtstr = m['format']['tags']['creation_time']
    dt = parse(dtstr)
    return dt

def meta(path):
    j = ffmpeg.probe(path)
    return j


if __name__ == '__main__':
    m = meta_time('d:/v1.mp4')
    print(m)


