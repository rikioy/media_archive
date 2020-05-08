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
        MainWindow.resize(740, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 691, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.srcEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.srcEdit.setObjectName("srcEdit")
        self.gridLayout.addWidget(self.srcEdit, 0, 1, 1, 1)
        self.srcBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.srcBtn.setObjectName("srcBtn")
        self.gridLayout.addWidget(self.srcBtn, 0, 0, 1, 1)
        self.runBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.runBtn.setObjectName("runBtn")
        self.gridLayout.addWidget(self.runBtn, 2, 0, 1, 1)
        self.dstBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.dstBtn.setObjectName("dstBtn")
        self.gridLayout.addWidget(self.dstBtn, 1, 0, 1, 1)
        self.pBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.pBar.setProperty("value", 0)
        self.pBar.setObjectName("pBar")
        self.gridLayout.addWidget(self.pBar, 2, 1, 1, 1)
        self.dstEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.dstEdit.setObjectName("dstEdit")
        self.gridLayout.addWidget(self.dstEdit, 1, 1, 1, 1)
        self.tBro = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.tBro.setObjectName("tBro")
        self.gridLayout.addWidget(self.tBro, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 23))
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
        self.runBtn.setText(_translate("MainWindow", "PushButton"))
        self.dstBtn.setText(_translate("MainWindow", "PushButton"))
