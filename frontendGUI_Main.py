# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\frontendGUI_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from email.message import Message
import escaperoom

import threading
import socket
import time

from suspectwindow import Ui_SuspectWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtCore import QObject, QTime, QTimer, QThread, pyqtSignal
import datetime
from playsound import playsound
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

TIMER = os.environ.get("TIMER")
print(TIMER) #TODO put the admin panel together to create the winner and the timer



class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.count = 1
 
        self.worker = WorkerThread()
        self.worker.start()
        # self.worker.finished.connect(self.event_timer_finished())
        
    def event_timer_finished(self):
        pass


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1728, 969)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(690, 0, 311, 131))
        self.worker.update_progress.connect(self.find_current_timer)
        
        self.lcdNumber.display(str(TIMER))
        # self.lcdNumber.setProperty("value", 3000.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1420, 30, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(100, 100, 461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1150, 80, 531, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(570, 10, 20, 691))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1140, 0, 20, 861))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, 90, 481, 751))


        font = QtGui.QFont()
        font.setPointSize(20)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(1150, 90, 531, 751))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 140, 551, 631))
        self.label_3.setStyleSheet("image: url(:/images/bloodquestion.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(572, 770, 581, 81))
        font = QtGui.QFont()
        font.setFamily("Bodoni Bd BT")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 700, 581, 81))
        font = QtGui.QFont()
        font.setFamily("Bodoni Bd BT")
        font.setPointSize(36)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_3.clicked.connect(self.on_pushButton_clicked3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1728, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def find_current_timer(self, val):
        print(val)
        x = time.strftime('%M:%S', time.gmtime(val))
        self.lcdNumber.display(x)



    def on_pushButton_clicked(self):
        print("show the suspects")
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SuspectWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def on_pushButton_clicked3(self):
        
        if self.count == 1:
            with open('hint1.txt') as help:
                lines = help.readlines()
                lines = str(lines[0])
                self.plainTextEdit_2.setPlainText(lines)
        if self.count == 2:
            with open('hint2.txt') as help:
                lines = help.readlines()
                lines = str(lines[0])
                self.plainTextEdit_2.setPlainText(lines)
        if self.count == 3:
            with open('hint3.txt') as help:
                lines = help.readlines()
                lines = str(lines[0])
                self.plainTextEdit_2.setPlainText(lines)
        if self.count == 4:
            with open('hint4.txt') as help:
                lines = help.readlines()
                lines = str(lines[0])
                self.plainTextEdit_2.setPlainText(lines)
        if self.count == 5:
            with open('hint5.txt') as help:
                lines = help.readlines()
                lines = str(lines[0])
                self.plainTextEdit_2.setPlainText(lines)
        if self.count == 6:
            with open('hint6.txt') as help:
                lines = help.readlines()
                lines = str(lines[0])
                self.plainTextEdit_2.setPlainText(lines)
        self.count += 1


        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Clues"))
        self.label_2.setText(_translate("MainWindow", "Story"))
        # self.plainTextEdit.setPlainText(_translate("MainWindow", "This is where the story text will go"))
        with open('story.txt') as f:
            lines = f.readlines()
            lines = str(lines[0])
            self.plainTextEdit.setPlainText(lines)


        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "This is where we will send clues. Each clue is used for the puzzle you are on. Do not skip clues!!"
"\n"
""))
        self.pushButton.setText(_translate("MainWindow", "See Suspects-Identify"))
        self.pushButton_3.setText(_translate("MainWindow", "Need Clue"))
        
class WorkerThread(QThread):
    update_progress = pyqtSignal(int)
    minute = int(TIMER)
    t = minute *60
    def run(self):
        while self.t:
            mins, secs = divmod(self.t, 60)
            timer_time = '{:02d}:{:02d}'.format(mins, secs)
            print(timer_time, end="\r")
            time.sleep(1)
            self.t -= 1
            self.update_progress.emit(self.t)
            if self.t == 0:
                playsound('audio.mp3')# TODO change this to a good audio file

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

