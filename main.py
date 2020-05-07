import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from ui import *
from util.path import walk


class MyThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, src, dst):
        super(MyThread, self).__init__()
        self.src = src
        self.dst = dst

    def run(self):
        filelist = walk(self.src)
        for f in filelist:
            self.signal.emit(f[1])


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
        #self.tBro.append(msg)
        print(msg)

    def run(self):
        self.setLog("run")
        src = self.srcEdit.text()
        dst = self.dstEdit.text()
        self.setLog(src)
        self.setLog(dst)

        self.my_thread = MyThread( src, dst)
        self.my_thread.signal.connect(self.setLog)
        self.my_thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())