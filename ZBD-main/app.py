import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import *
import database
import os

os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'


class MyGui(QMainWindow):
    
    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi("ui/logowanie.ui", self)
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
        uic.loadUi("ui/ADMINGLOWNY.ui", self)
        self.pushButton.clicked.connect(self.admin_insert)
        self.pushButton_2.clicked.connect(self.admin_delete)
        self.pushButton_4.clicked.connect(self.admin_wyswietl)
        #### ZMIANY
        # self.pushButton.clicked.connect(self.insert_gracz)
        # self.pushButton_2.clicked.connect(self.insert_sezon)
        # self.pushButton_3.clicked.connect(self.insert_liga)
        # self.pushButton_4.clicked.connect(self.insert_szczebel)
        # self.pushButton_5.clicked.connect(self.insert_kolejka_rozgrywek)
        # self.pushButton_6.clicked.connect(self.insert_druzyna)
    
    def admin_insert(self):
        uic.loadUi("ui/admin.ui", self)
        self.pushButton.clicked.connect(self.insert_gracz)
        #### ZMIANY
        self.pushButton.clicked.connect(self.insert_gracz)
        self.pushButton_2.clicked.connect(self.insert_sezon)
        self.pushButton_3.clicked.connect(self.insert_liga)
        self.pushButton_4.clicked.connect(self.insert_szczebel)
        self.pushButton_5.clicked.connect(self.insert_kolejka_rozgrywek)
        self.pushButton_6.clicked.connect(self.insert_druzyna)
    
    def admin_wyswietl(self):
        uic.loadUi("ui/admin_wyswietlanie.ui", self)
        self.pushButton.clicked.connect(self.loggedasadmin)
        self.pushButton_2.clicked.connect(self.admin_wyswietl2)
        
    def admin_wyswietl2(self):
        szukane = self.comboBox.currentText()
        if szukane == "GRACZ":
            self.print_gracze()
        elif szukane == "DRUŻYNA":
            self.print_druzyny()
        elif szukane == "SEZON":
            self.print_sezon()
        elif szukane == "LIGA":
            self.print_liga()
        elif szukane == "SZCZEBEL ROZGRYWEK":
            self.print_szczebel()
        elif szukane == "SEZON_LIGA":
            self.print_sezon_liga()
        elif szukane == "KOLEJKA_ROZGRYWEK":
            self.print_kolejka()
        elif szukane == "DRUŻYNA_SZCZEBEL":
            self.print_druzyna_szczebel()
        elif szukane == "GRACZ_DRUŻYNA":
            self.print_gracz_druzyna()
        elif szukane == "SUGESTIE":
            self.print_sugestie()

    def insert_gracz(self):
        uic.loadUi("ui/insert_gracz.ui", self)
        self.pushButton.clicked.connect(self.insert_gracz_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
    
    def insert_gracz_add(self):    
        imie = self.lineEdit.text()
        nazwisko = self.lineEdit_2.text()
        rok_urodzenia = int(self.lineEdit_3.text())
        database.add_gracz(connection, imie, nazwisko, rok_urodzenia)
        
    def insert_sezon(self):
        uic.loadUi("ui/insert_sezon.ui", self)
        self.pushButton.clicked.connect(self.insert_sezon_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)

    def insert_sezon_add(self):    
        rok = int(self.lineEdit.text())
        poczatek_sezonu = self.lineEdit_2.text()
        koniec_sezonu = self.lineEdit_3.text()
        database.add_sezon(connection, rok, poczatek_sezonu, koniec_sezonu)

    def insert_liga(self):
        uic.loadUi("ui/insert_liga.ui", self)
        self.pushButton.clicked.connect(self.insert_liga_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
        
    def insert_liga_add(self):    
        nazwa = self.lineEdit.text()
        database.add_liga(connection, nazwa)

    def insert_szczebel(self):
        uic.loadUi("ui/insert_szczebel.ui", self)
        self.pushButton.clicked.connect(self.insert_szczebel_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
        
    def insert_szczebel_add(self):    
        nazwa_szczebla = self.lineEdit.text()
        database.add_szczebel(connection, nazwa_szczebla)

    def insert_kolejka_rozgrywek(self):
        uic.loadUi("ui/insert_kolejka_rozgrywek.ui", self)
        self.pushButton.clicked.connect(self.insert_kolejka_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
        
    def insert_kolejka_add(self):    
        start_kolejki = self.lineEdit.text()
        koniec_kolejki = self.lineEdit_2.text()
        id_sezon_liga = int(self.lineEdit_3.text())
        try:
            database.add_kolejka_rozgrywek(connection, start_kolejki, koniec_kolejki, id_sezon_liga)
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
    
    def insert_druzyna(self):
        uic.loadUi("ui/insert_druzyna.ui", self)
        self.pushButton.clicked.connect(self.insert_druzyna_add)
        self.pushButton_2.clicked.connect(self.loggedasadmin)
        
    def insert_druzyna_add(self):    
        nazwa_druzyna = self.lineEdit.text()
        database.add_druzyna(connection, nazwa_druzyna)

    def loggedasuser(self):
        uic.loadUi("ui/co_robi_user.ui", self)
        self.pushButton.clicked.connect(self.user_gracze)
        self.pushButton_2.clicked.connect(self.loggedasuser)
        self.pushButton_3.clicked.connect(self.user_druzyny)
        self.pushButton_4.clicked.connect(self.user_sezon)
        self.pushButton_5.clicked.connect(self.user_liga)
        self.pushButton_6.clicked.connect(self.user_kolejka)
        self.pushButton_7.clicked.connect(self.user_sezon_liga)
        self.pushButton_8.clicked.connect(self.user_druzyna_szczebel)
        self.pushButton_9.clicked.connect(self.user_gracz_druzyna)
        self.pushButton_10.clicked.connect(self.user_szczebel)
        self.pushButton_11.clicked.connect(self.user_sugestie)
        #self.upushButton_2.clicked.connect(self.print_gracze)
        #self.setStyleSheet("background-color: blue;")

    def user_sugestie(self):
        uic.loadUi("ui/zmiany.ui", self)
        self.pushButton.clicked.connect(self.insert_sugestie_add)
        self.pushButton_2.clicked.connect(self.loggedasuser)

    def insert_sugestie_add(self):    
        sugestia = self.textEdit.toPlainText()
        database.insert_sugestia(connection, sugestia)

    ##### GRACZE
    def user_gracze(self):
        uic.loadUi("ui/user.ui", self)
        self.upushButton_2.clicked.connect(self.print_gracze)
        self.pushButton.clicked.connect(self.loggedasuser)
        self.upushButton.clicked.connect(self.print_szukane)

    def print_gracze(self):
        gracze = database.select_gracz(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_GRACZA   |    IMIE    |    NAZWISKO    |    ROK_URODZENIA\n")
        for gracz in gracze:
            print(gracz)
            self.textBrowser.append(" | ".join(map(str,gracz)))

    def print_sugestie(self):
        sugestie = database.select_sugestia(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_SUGESTII   |    SUGESESTIA\n")
        for sugestia in sugestie:
            print(sugestia)
            self.textBrowser.append(" | ".join(map(str,sugestia)))

    def print_szukane(self):
        #print("asdasd")
        wartosc = self.lineEditx.text()
        data = self.lineEditx.text()
        print(wartosc)
        self.textBrowser.clear()
        gracze = database.select_szukane_gracze(connection, wartosc, data)
        for gracz in gracze:
            print(gracz)
            self.textBrowser.append(" | ".join(map(str,gracz)))

    ##### DRUZYNY
    def user_druzyny(self):
        uic.loadUi("ui/user_druzyny.ui", self)
        self.pushButton.clicked.connect(self.print_druzyny)
        self.pushButton_2.clicked.connect(self.loggedasuser) 
    def print_druzyny(self):
        druzyny = database.select_druzyny(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_DRUZYNY   |    NAZWA DRUZYNY\n")
        for druzyna in druzyny:
            print(druzyna)
            self.textBrowser.append(" | ".join(map(str,druzyna)))

    #### SEZON
    def user_sezon(self):
        uic.loadUi("ui/user_sezon.ui", self)
        self.pushButton.clicked.connect(self.print_sezon)
        self.pushButton_2.clicked.connect(self.loggedasuser)
    def print_sezon(self):
        sezony = database.select_sezon(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_SEZONU   |    ROK    |    POCZATEK    |    KONIEC\n")
        for sezon in sezony:
            print(sezon)
            self.textBrowser.append(" | ".join(map(str,sezon)))

    ### LIGA
    def user_liga(self):
        uic.loadUi("ui/user_liga.ui", self)
        self.pushButton.clicked.connect(self.print_liga)
        self.pushButton_2.clicked.connect(self.loggedasuser)
    def print_liga(self):
        ligi = database.select_liga(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_LIGI   |    NAZWA\n")
        for liga in ligi:
            print(liga)
            self.textBrowser.append(" | ".join(map(str,liga)))

    ### KOLEJKA_ROZGRYWEK
    def user_kolejka(self):
        uic.loadUi("ui/user_kolejka.ui", self)
        self.pushButton.clicked.connect(self.print_kolejka)
        self.pushButton_2.clicked.connect(self.loggedasuser)
    def print_kolejka(self):
        kolejki = database.select_kolejka(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_KOLEJKI   |    START KOLEJKI    |    KONIEC KOLEJKI     |    ID_SEZON_LIGA\n")
        for kolejka in kolejki:
            print(kolejka)
            self.textBrowser.append(" | ".join(map(str,kolejka)))

    def user_sezon_liga(self):
        uic.loadUi("ui/user_sezon_liga.ui", self)
        self.pushButton.clicked.connect(self.print_sezon_liga)
        self.pushButton_2.clicked.connect(self.loggedasuser)
    def print_sezon_liga(self):
        sezony_liga = database.select_sezon_liga(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_SEZON_LIGA   |    ID_SEZONU    |    ID_LIGI     |    ID_SZCZEBLA\n")
        for sezon_liga in sezony_liga:
            print(sezon_liga)
            self.textBrowser.append(" | ".join(map(str,sezon_liga)))

    def user_druzyna_szczebel(self):
        uic.loadUi("ui/user_druzyna_szczebel.ui", self)
        self.pushButton.clicked.connect(self.print_druzyna_szczebel)
        self.pushButton_2.clicked.connect(self.loggedasuser)
    def print_druzyna_szczebel(self):
        druzyna_szczeble = database.select_druzyna_szczebel(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_DRUZYNA_SZCZEBEL   |    ID_DRUZYNY    |    ID_SEZON_LIGA\n")
        for x in druzyna_szczeble:
            print(x)
            self.textBrowser.append(" | ".join(map(str,x)))

    def user_gracz_druzyna(self):
        uic.loadUi("ui/user_gracz_druzyna.ui", self)
        self.pushButton.clicked.connect(self.print_gracz_druzyna)
        self.pushButton_2.clicked.connect(self.loggedasuser)
    def print_gracz_druzyna(self):
        dane = database.select_gracz_druzyna(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_GRACZ_DRUZYNA   |    ID_GRACZ    |    ID_DRUZYNA_SZCZEBEL\n")
        for x in dane:
            print(x)
            self.textBrowser.append(" | ".join(map(str,x)))
    
    def user_szczebel(self):
        uic.loadUi("ui/user_szczebel.ui", self)
        self.pushButton.clicked.connect(self.print_szczebel)
        self.pushButton_2.clicked.connect(self.loggedasuser)
    def print_szczebel(self):
        dane = database.select_szczebel(connection)
        self.textBrowser.clear()
        self.textBrowser.append("ID_SZCZEBLA_ROZGRYWEK   |    NAZWA SZCZEBLA\n")
        for x in dane:
            print(x)
            self.textBrowser.append(" | ".join(map(str,x)))

###########################################################################################################################################################################

    def admin_delete(self):
        uic.loadUi("ui/mwdelete.ui", self)
        self.pushButton_4.clicked.connect(self.delete_gracz)
        self.pushButton.clicked.connect(self.delete_sezon)
        self.pushButton_2.clicked.connect(self.delete_liga)
        self.pushButton_3.clicked.connect(self.delete_szczebel)
        self.pushButton_5.clicked.connect(self.delete_kolejka_rozgrywek)
        self.pushButton_6.clicked.connect(self.delete_druzyna)
        self.pushButton_7.clicked.connect(self.loggedasadmin)

    def delete_gracz(self):
        uic.loadUi("ui/delete_gracz.ui", self)
        self.pushButton.clicked.connect(self.delete_gracz_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
    
    def delete_gracz_add(self):    
        imie = self.lineEdit.text()
        nazwisko = self.lineEdit_2.text()
        rok_urodzenia = int(self.lineEdit_3.text())
        database.delete_gracz(connection, imie, nazwisko, rok_urodzenia)
        
    def delete_sezon(self):
        uic.loadUi("ui/delete_sezon.ui", self)
        self.pushButton.clicked.connect(self.delete_sezon_add)
        self.pushButton_2.clicked.connect(self.admin_delete)

    def delete_sezon_add(self):    
        rok = int(self.lineEdit.text())
        poczatek_sezonu = self.lineEdit_2.text()
        koniec_sezonu = self.lineEdit_3.text()
        database.delete_sezon(connection, rok, poczatek_sezonu, koniec_sezonu)

    def delete_liga(self):
        uic.loadUi("ui/delete_liga.ui", self)
        self.pushButton.clicked.connect(self.delete_liga_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
        
    def delete_liga_add(self):    
        nazwa = self.lineEdit.text()
        database.delete_liga(connection, nazwa)

    def delete_szczebel(self):
        uic.loadUi("ui/delete_szczebel.ui", self)
        self.pushButton.clicked.connect(self.delete_szczebel_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
        
    def delete_szczebel_add(self):    
        nazwa_szczebla = self.lineEdit.text()
        database.delete_szczebel(connection, nazwa_szczebla)

    def delete_kolejka_rozgrywek(self):
        uic.loadUi("ui/delete_kolejka_rozgrywek.ui", self)
        self.pushButton.clicked.connect(self.delete_kolejka_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
        
    def delete_kolejka_add(self):    
        start_kolejki = self.lineEdit.text()
        koniec_kolejki = self.lineEdit_2.text()
        id_sezon_liga = int(self.lineEdit_3.text())
        database.delete_kolejka_rozgrywek(connection, start_kolejki, koniec_kolejki, id_sezon_liga)
        
    
    def delete_druzyna(self):
        uic.loadUi("ui/delete_druzyna.ui", self)
        self.pushButton.clicked.connect(self.delete_druzyna_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
        
    def delete_druzyna_add(self):    
        nazwa_druzyna = self.lineEdit.text()
        database.delete_druzyna(connection, nazwa_druzyna)

def main():
    global connection
    connection = database.connect()
    connection.execute("PRAGMA foreign_keys = 1")
    database.create_tables(connection)
    app = QApplication([])
    window = MyGui()
    app.exec_()

if __name__ == '__main__':
    main()