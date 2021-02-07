from PyQt5 import QtWidgets,QtCore,QtGui
import os,sys
from ayarlar import Ui_Ayarlar



class settings(QtWidgets.QDialog):
    def __init__(self):
        super(settings,self).__init__()
        self.ui = Ui_Ayarlar()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet(open("style.css","r").read())  
        
        self.selectRadio()
        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.pushButton.clicked.connect(self.saved)

        self.ui.TRY.toggled.connect(self.selected)
        self.ui.EUR.toggled.connect(self.selected)
        self.ui.USD.toggled.connect(self.selected)



    def selected(self):
        self.sender()

    def saved(self):
        items = self.ui.groupBox.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if i.isChecked():
                with open("config.txt","w+",encoding="UTF-8") as file :
                    file.write("Kur:"+i.text())
                    self.close()


    def cancel(self):
        self.close() 


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


    def selectRadio(self):
        with open("config.txt","r") as file :
            x = file.read()
            text = x.split(":")[1]
            if text == "TRY":
                self.ui.TRY.setChecked(True)
            elif text == "USD":
                self.ui.USD.setChecked(True)
            elif text == "EUR":
                self.ui.EUR.setChecked(True)


    def btnStyle(self):
        self.ui.pushButton.setStyleSheet("border-image: url('icons/minimizeIcon.png');")


