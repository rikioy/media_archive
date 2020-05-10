from util.md5 import md5file
from core.dir import mkdir_by_date, copyfile
from core.db_image import Image
from PyQt5.QtCore import QThread, pyqtSignal
from util.path import walk
from media.exif import exif_time
from media.media import meta_time

class ProcessThread(QThread):
    signal = pyqtSignal(str)
    psignal = pyqtSignal(int)

    def __init__(self, src, dst):
        super(ProcessThread, self).__init__()
        self.src = src
        self.dst = dst

    def run(self):
        db = Image(self.dst)
        filelist = walk(self.src)
        succ_count = 0
        total_count = len(filelist)
        img_count = 0
        video_count = 0
        skip_count = 0
        for f in filelist:
            dt = None
            if f[2].lower() in ['.jpg', '.bmp', '.jpeg', '.png']:
                img_count += 1
                dt = exif_time(f[0])
            elif f[2].lower() in ['.mp4', '.mov']:
                video_count += 1
                dt = meta_time(f[0])
            if dt is not None:
                self.signal.emit(f[0] + " 处理中...")
                dst_path = mkdir_by_date(self.dst, dt)
                md5 = md5file(f[0])
                if db.md5_exists(md5) is False:
                    copyfile(f[0], dst_path, f[1], f[2])
                    db.insert((f[1] + f[2], md5, '', dt.strftime("%Y-%m-%d %H:%M:%S"), dt.year, dt.month, dt.day))
                else:
                    skip_count += 1
            succ_count = succ_count + 1
            bar_count = int(succ_count/total_count*100)
            self.psignal.emit(bar_count)
        end_msg = '总计: {}, 图片: {}, 视频: {}, 略过: {}'.format(total_count, img_count, video_count, skip_count)
        self.signal.emit(end_msg)
        db.close()