import sys
import os
from core.db_image import Image
from util.md5 import md5file
from core.dir import mkdir_by_date, copyfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from ui import *
from util.path import walk
from media.exif import exif_time
from media.media import meta_time


class MyThread(QThread):
    signal = pyqtSignal(str)
    psignal = pyqtSignal(int)

    def __init__(self, src, dst):
        super(MyThread, self).__init__()
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


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.srcBtn.clicked.connect(self.setSrc)
        self.dstBtn.clicked.connect(self.setDst)
        self.runBtn.clicked.connect(self.run)


    def setSrc(self):
        get_dir_path = QFileDialog.getExistingDirectory(self, 'select dir', '/')
        self.srcEdit.setText(str(get_dir_path))
        self.tBro.append("select src dir: " + self.srcEdit.text())

    def setDst(self):
        get_dir_path = QFileDialog.getExistingDirectory(self, 'select dir', '/')
        self.dstEdit.setText(str(get_dir_path))

    def setLog(self, msg):
        self.tBro.append(msg)

    def upPBar(self, count):
        self.pBar.setValue(count)

    def run(self):
        self.setLog("run")
        src = self.srcEdit.text()
        dst = self.dstEdit.text()
        self.setLog(src)
        self.setLog(dst)

        if src == '':
            src = '/Users/fuqingrong/Downloads/src'
        if dst == '':
            dst = '/Users/fuqingrong/Downloads/dst'

        #src = 'd:/src'
        #dst = 'd:/dst'

        if os.path.exists(src) is False:
            QMessageBox.information(self, '提示', '来源文件夹{}不存在'.format(src), QMessageBox.Yes)
            return
        if os.path.exists(dst) is False:
            QMessageBox.information(self, '提示', '目标文件夹{}不存在'.format(dst), QMessageBox.Yes)
            return
        self.my_thread = MyThread(src, dst)
        self.my_thread.signal.connect(self.setLog)
        self.my_thread.psignal.connect(self.upPBar)
        self.my_thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())