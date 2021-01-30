import sys,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from mw import Ui_MainWindow
x = 2354



class Pararel (QThread):
    def __init__(self, mianwindow, parent=None):
        super().__init__()
        self.mianwindow = mianwindow

    def run(self):
        y = 1
        for i in range(500):
            time.sleep(0.01)
            y += 1
            u = y/2.5
            print(str(y)+"  "+str(u))

class Hoodoo(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.knopka)
        self.pushButton_2.clicked.connect(self.knopka2)
        self.lineEdit_2.textEdited.connect(self.teep)
        self.lineEdit_2.returnPressed.connect(self.knopka2)
        self.lineEdit_2.editingFinished.connect(self.ushov)
        self.gopstop = Pararel(mianwindow=self)

    def run(self):
        self.gopstop.start()

    def ushov(self):
        global x
        self.lineEdit_4.setText('gud' + str(x))

    def teep(self):
        global x
        x += 1
        print("teep")

    def knopka2 (self):
        global x
        self.lineEdit_3.setText(self.lineEdit_2.text())
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        print("robotae")


    def knopka(self):
        global x
        self.lineEdit.setText(str(x))
        x += 1
        self.run()
        print(str(x))

    def pechat(self):
        self.lineEdit.setText("64785")

def main():

    app = QtWidgets.QApplication(sys.argv)
    window = Hoodoo()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
