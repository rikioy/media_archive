# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.srcBtn = QtWidgets.QPushButton(self.centralwidget)
        self.srcBtn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.srcBtn.setObjectName("srcBtn")
        self.srcEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.srcEdit.setGeometry(QtCore.QRect(100, 10, 311, 21))
        self.srcEdit.setObjectName("srcEdit")
        self.dstBtn = QtWidgets.QPushButton(self.centralwidget)
        self.dstBtn.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.dstBtn.setObjectName("dstBtn")
        self.dstEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dstEdit.setGeometry(QtCore.QRect(100, 50, 311, 21))
        self.dstEdit.setObjectName("dstEdit")
        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.runBtn.setObjectName("runBtn")
        self.pBar = QtWidgets.QProgressBar(self.centralwidget)
        self.pBar.setGeometry(QtCore.QRect(100, 90, 311, 31))
        self.pBar.setProperty("value", 0)
        self.pBar.setObjectName("pBar")
        self.tBro = QtWidgets.QTextBrowser(self.centralwidget)
        self.tBro.setGeometry(QtCore.QRect(10, 140, 271, 251))
        self.tBro.setObjectName("tBro")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.srcBtn.setText(_translate("MainWindow", "PushButton"))
        self.dstBtn.setText(_translate("MainWindow", "PushButton"))
        self.runBtn.setText(_translate("MainWindow", "PushButton"))
