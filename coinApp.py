################################################
################################################
################################################
#########*******###*******####**********########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**********########
########**#####**#**#####**###**################
########**#####**#**#####**###**################
########**######***######**###**################
########**###############**###**################
########**###############**###**################
################################################
########Copyright © Maresal Programming#########
################################################

from PyQt5 import QtWidgets,QtCore
import os,sys
from coin import Ui_MainWindow
from dataInsert import *
from settingMenu import *


class coinsApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(coinsApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet(open("style.css","r").read())  
        self.setLabelText()
        self.setLabel()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.AllStart)
        self.timer.start(5000)

        self.ui.exitBtn.clicked.connect(self.exit)
        self.ui.minimizeBtn.clicked.connect(self.minimize)
        self.ui.settingBtn.clicked.connect(self.settingOpen)

    def setLabelText(self):
        text = self.getSetting()
        self.ui.btcCurrentPrice.setText(getData(f"Bitcoin{text}")[-1][1]+f" {text}")
        self.ui.btcPrice.setText(getData(f"Bitcoin{text}")[-2][1]+f" {text}")
        self.ui.BtcLowPrice.setText("24h↓/"+getData(f"Bitcoin{text}")[-1][2]+f" {text}")
        self.ui.btcHighPrice.setText("24h↑/"+getData(f"Bitcoin{text}")[-1][3]+f" {text}")
        self.ui.dogeCurrentPrice.setText(getData(f"Doge{text}")[-1][1]+f" {text}")
        self.ui.dogePrice.setText(getData(f"Doge{text}")[-2][1]+f" {text}")
        self.ui.dogeLowPrice.setText("24h↓/"+getData(f"Doge{text}")[-1][2]+f" {text}")
        self.ui.dogeHighPrice.setText("24h↑/"+getData(f"Doge{text}")[-1][3]+f" {text}")
        self.ui.xrpCurrentPrice.setText(getData(f"Ripple{text}")[-1][1]+f" {text}")
        self.ui.xrpPrice.setText(getData(f"Ripple{text}")[-2][1]+f" {text}")
        self.ui.xrpLowPrice.setText("24h↓/"+getData(f"Ripple{text}")[-1][2]+f" {text}")
        self.ui.xrpHighPrice.setText("24h↑/"+getData(f"Ripple{text}")[-1][3]+f" {text}")

    def ImageSetLabel(self,label,LastPrice):
        try:
            ltext = label.text().split(" ")
            if float(ltext[0]) > float(LastPrice):
                label.setStyleSheet(
                    "color: rgb(0, 255, 0);"'\nborder-image: url("icons/up.png");')
            elif float(ltext[0]) < float(LastPrice):
                label.setStyleSheet(
                    "color: rgb(255, 0, 0);"'border-image: url("icons/down.png");')
            else:
                label.setStyleSheet(
                    "color: rgb(255, 255, 255);"'\nborder-image: url("icons/natural.png");')

        except Exception as err:
            print(err)

    def setLabel(self):
        text = self.getSetting()
        self.ImageSetLabel(self.ui.btcCurrentPrice,getData(f"Bitcoin{text}")[-2][1])
        self.ImageSetLabel(self.ui.dogeCurrentPrice,getData(f"Doge{text}")[-2][1])
        self.ImageSetLabel(self.ui.xrpCurrentPrice,getData(f"Ripple{text}")[-2][1])


    def AllStart(self):
        self.workerStarted()
        self.setLabelText()
        self.setLabel()

    def workerStarted(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.workerStop)

    def workerStop(self):
        print("işlem bitti")

# Windows Ayarları
    def settingOpen(self):
        self.st = settings()
        self.st.show()

    def mousePressEvent(self, event):
        try:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.dragPos = event.globalPos()
                event.accept()
        except :
            pass

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        except :
            pass

    def minimize(self):
        self.showMinimized()

    def exit(self):
        self.close()

    def getSetting(self):
        with open("config.txt","r") as file :
            x = file.read()
            text = x.split(":")[1]
            return text


class WorkerThread(QtCore.QThread):
    def run(self):
        InsertData()








if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = coinsApp()
    main.show()
    app.exit(app.exec_())