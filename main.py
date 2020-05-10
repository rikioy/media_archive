import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui import *
from process_thread import ProcessThread
from web_thread import WebThread


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.srcBtn.clicked.connect(self.setSrc)
        self.dstBtn.clicked.connect(self.setDst)
        self.runBtn.clicked.connect(self.run)
        self.webBtn.clicked.connect(self.runweb)


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

    def runweb(self):
        self.setLog("WebThread run")
        dst = self.dstEdit.text()
        if dst == '':
            dst = '/Users/fuqingrong/Downloads/dst'
        if os.path.exists(dst) is False:
            QMessageBox.information(self, '提示', '目标文件夹{}不存在'.format(dst), QMessageBox.Yes)
            return
        self.web_thread = WebThread(dst)
        self.web_thread.signal.connect(self.setLog)
        self.web_thread.start()

    def run(self):
        self.setLog("ProcessThread run")
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
        self.my_thread = ProcessThread(src, dst)
        self.my_thread.signal.connect(self.setLog)
        self.my_thread.psignal.connect(self.upPBar)
        self.my_thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())