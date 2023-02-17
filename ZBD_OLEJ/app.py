import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import *
import database
import os

os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'


class MyGui(QMainWindow):
    
    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi("logowanie.ui", self)
        self.show()
        self.pushButton.clicked.connect(self.zalogowanie)
        
    
    def zalogowanie(self):
        
        message = self.lineEdit.text()
        print(message)

        if message == "admin":
            self.loggedasadmin()

        elif message == "user":
            self.loggedasuser()
        
        else:
            self.label.setText("Błędne dane logowania!")
            self.update()

    def update(self):
        self.label.adjustSize()

    def loggedasadmin(self):
        uic.loadUi("admin.ui", self)
        self.pushButton.clicked.connect(self.insert_gracz)
        self.pushButton_2.clicked.connect(self.insert_sezon)
        self.pushButton_3.clicked.connect(self.insert_liga)
        self.pushButton_4.clicked.connect(self.insert_szczebel)
        self.pushButton_5.clicked.connect(self.insert_kolejka_rozgrywek)
        self.pushButton_6.clicked.connect(self.insert_druzyna)
    
    def insert_gracz(self):
        uic.loadUi("insert_gracz.ui", self)
        self.pushButton.clicked.connect(self.insert_gracz_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)

    def insert_gracz_add(self):    
        imie = self.lineEdit.text()
        nazwisko = self.lineEdit_2.text()
        rok_urodzenia = int(self.lineEdit_3.text())

        database.add_gracz(connection, imie, nazwisko, rok_urodzenia)
    ######################################################
    def insert_sezon(self):
        uic.loadUi("insert_sezon.ui", self)
        self.pushButton.clicked.connect(self.insert_sezon_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
        
    def insert_sezon_add(self):    
        rok = int(self.lineEdit.text())
        poczatek_sezonu = self.lineEdit_2.text()
        koniec_sezonu = self.lineEdit_3.text()

        database.add_sezon(connection, rok, poczatek_sezonu, koniec_sezonu)
    ######################################################################
    def insert_liga(self):
        uic.loadUi("insert_liga.ui", self)
        self.pushButton.clicked.connect(self.insert_liga_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
        
    def insert_liga_add(self):    
        nazwa = self.lineEdit.text()

        database.add_liga(connection, nazwa)

#############################################################################
    def insert_szczebel(self):
        uic.loadUi("insert_szczebel.ui", self)
        self.pushButton.clicked.connect(self.insert_szczebel_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
        
    def insert_szczebel_add(self):    
        nazwa_szczebla = self.lineEdit.text()

        database.add_szczebel(connection, nazwa_szczebla)

##########################################################################
    def insert_kolejka_rozgrywek(self):
        uic.loadUi("insert_kolejka_rozgrywek.ui", self)
        self.pushButton.clicked.connect(self.insert_kolejka_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
        
    def insert_kolejka_add(self):    
        start_kolejki = self.lineEdit.text()
        koniec_kolejki = self.lineEdit_2.text()
        id_sezon_liga = int(self.lineEdit_3.text())

        database.add_kolejka_rozgrywek(connection, start_kolejki, koniec_kolejki, id_sezon_liga)
########################################################################

    def insert_druzyna(self):
        uic.loadUi("insert_druzyna.ui", self)
        self.pushButton.clicked.connect(self.insert_druzyna_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
        
    def insert_druzyna_add(self):    
        nazwa_druzyna = self.lineEdit.text()

        database.add_druzyna(connection, nazwa_druzyna)

        
    def loggedasuser(self):
        uic.loadUi("user.ui", self)
        self.upushButton_2.clicked.connect(self.print_gracze)
        #self.setStyleSheet("background-color: blue;")
    
    def print_gracze(self):
        gracze = database.select_gracz(connection)
        for gracz in gracze:
            print(gracz)
            self.textBrowser.append(" | ".join(map(str,gracz)))


def main():
    global connection
    connection = database.connect()
    database.create_tables(connection)
    app = QApplication([])
    window = MyGui()
    app.exec_()

if __name__ == '__main__':
    main()