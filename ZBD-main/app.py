import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import *
import database
import os
import re

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
        self.pushButton_3.clicked.connect(self.admin_update)
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
        self.pushButton_7.clicked.connect(self.insert_sezon_liga)
        self.pushButton_8.clicked.connect(self.insert_druzyna_szczebel)
        self.pushButton_9.clicked.connect(self.insert_gracz_druzyna)
        self.pushButton_10.clicked.connect(self.loggedasadmin)
        self.pushButton_11.clicked.connect(self.insert_mecz)

        
    
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

        # self.pushButton_7.clicked.connect(self.insert_sezon_liga)
        # self.pushButton_8.clicked.connect(self.insert_druzyna_szczebel)
        # self.pushButton_9.clicked.connect(self.insert_gracz_druzyna)
        # self.pushButton_11.clicked.connect(self.insert_mecz)

    def insert_sezon_liga(self):
        uic.loadUi("ui/insert_sezon_liga.ui", self)
        self.pushButton.clicked.connect(self.insert_sezon_liga_add)
        self.pushButton_2.clicked.connect(self.admin_insert)
    def insert_sezon_liga_add(self):
        id_sezonu = self.lineEdit.text()
        id_ligi = self.lineEdit_2.text()
        id_szczebla = self.lineEdit_3.text()
        self.label.setText(" ")
        try:
            if id_sezonu.isnumeric() and id_ligi.isnumeric() and id_szczebla.isnumeric():
                database.insert_sezon_liga(connection, id_sezonu, id_ligi, id_szczebla)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                self.label.setText("Upewnij się że id_sezonu, _id_ligi oraz id_szczebla to wartości liczbowe całkowite")
                self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_sezonu, id_ligi, id_szczebla istnieją!")
            self.label.adjustSize()

    def insert_druzyna_szczebel(self):
        uic.loadUi("ui/insert_druzyna_szczebel.ui", self)
        self.pushButton.clicked.connect(self.insert_druzyna_szczebel_add)
        self.pushButton_2.clicked.connect(self.admin_insert)
    def insert_druzyna_szczebel_add(self):
        id_sezon_liga = self.lineEdit.text()
        id_druzyny = self.lineEdit_2.text()
        self.label.setText(" ")
        try:
            if id_sezon_liga.isnumeric() and id_druzyny.isnumeric():
                database.insert_druzyna_szczebel(connection, id_sezon_liga, id_druzyny)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                self.label.setText("Upewnij się że id_sezon_liga oraz id_drużyny to wartości liczbowe całkowite")
                self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_sezon_liga, id_druzyny istnieją!")
            self.label.adjustSize()
    
    def insert_gracz_druzyna(self):
        uic.loadUi("ui/insert_gracz_druzyna.ui", self)
        self.pushButton.clicked.connect(self.insert_gracz_druzyna_add)
        self.pushButton_2.clicked.connect(self.admin_insert)
    def insert_gracz_druzyna_add(self):
        id_gracza = self.lineEdit.text()
        id_druzyna_szczebel = self.lineEdit_2.text()
        self.label.setText(" ")
        self.label.adjustSize()
        try:
            if id_gracza.isnumeric() and id_druzyna_szczebel.isnumeric():
                database.insert_gracz_druzyna(connection, id_gracza, id_druzyna_szczebel)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                self.label.setText("Upewnij się że id_gracza oraz id_druzyna_szczebel to wartości liczbowe całkowite")
                self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_gracza, id_druzyna_szczebel istnieją!")
            self.label.adjustSize()


    def insert_mecz(self):
        uic.loadUi("ui/insert_mecz.ui", self)
        self.pushButton.clicked.connect(self.insert_mecz_add)
        self.pushButton_2.clicked.connect(self.admin_insert)
    def insert_mecz_add(self):
        wynik = self.lineEdit.text()
        id_druzyna_szczebel_1 = self.lineEdit_2.text()
        id_druzyna_szczebel_2 = self.lineEdit_3.text()
        self.label.setText(" ")
        self.label.adjustSize()
        try:
            if id_druzyna_szczebel_1.isnumeric() and id_druzyna_szczebel_2.isnumeric() and (id_druzyna_szczebel_1 != id_druzyna_szczebel_2) and (re.match('^\d:\d', wynik)):
                database.insert_mecz(connection, wynik, id_druzyna_szczebel_1, id_druzyna_szczebel_2)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                 self.label.setText("Upewnij się że wprowadzone id obu drużyn to różniące się liczbowe wartości całkowite\n a wynik zapisany jest w formacie gole_1:gole_2")
                 self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_druzyna_szczebel_1, id_druzyna_szczebel_2 istnieją!")
            self.label.adjustSize()

    
    ##################################################################
    def insert_gracz(self):
        uic.loadUi("ui/insert_gracz.ui", self)
        self.pushButton.clicked.connect(self.insert_gracz_add)
        self.pushButton_2.clicked.connect(self.admin_insert)
    
    def insert_gracz_add(self):    
        imie = self.lineEdit.text()
        nazwisko = self.lineEdit_2.text()
        rok_urodzenia = int(self.lineEdit_3.text())
        try:
            database.add_gracz(connection, imie, nazwisko, rok_urodzenia)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("NARUSZONO KLUCZE!")
            self.label.adjustSize()
        
        
    def insert_sezon(self):
        uic.loadUi("ui/insert_sezon.ui", self)
        self.pushButton.clicked.connect(self.insert_sezon_add)
        self.pushButton_2.clicked.connect(self.admin_insert)

    def insert_sezon_add(self):    
        rok = int(self.lineEdit.text())
        poczatek_sezonu = self.lineEdit_2.text()
        koniec_sezonu = self.lineEdit_3.text()
        try:
            database.add_sezon(connection, rok, poczatek_sezonu, koniec_sezonu)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("NARUSZONO KLUCZE!")
            self.label.adjustSize()
        
        

    def insert_liga(self):
        uic.loadUi("ui/insert_liga.ui", self)
        self.pushButton.clicked.connect(self.insert_liga_add)
        self.pushButton_2.clicked.connect(self.admin_insert)
        
    def insert_liga_add(self):    
        nazwa = self.lineEdit.text()
        try:
            database.add_liga(connection, nazwa)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("NARUSZONO KLUCZE!")
            self.label.adjustSize()
        

    def insert_szczebel(self):
        uic.loadUi("ui/insert_szczebel.ui", self)
        self.pushButton.clicked.connect(self.insert_szczebel_add)
        self.pushButton_2.clicked.connect(self.admin_insert)
        
    def insert_szczebel_add(self):    
        nazwa_szczebla = self.lineEdit.text()
        try:
            database.add_szczebel(connection, nazwa_szczebla)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("NARUSZONO KLUCZE!")
            self.label.adjustSize()

    def insert_kolejka_rozgrywek(self):
        uic.loadUi("ui/insert_kolejka_rozgrywek.ui", self)
        self.pushButton.clicked.connect(self.insert_kolejka_add)
        self.pushButton_2.clicked.connect(self.admin_insert)
        
    def insert_kolejka_add(self):    
        start_kolejki = self.lineEdit.text()
        koniec_kolejki = self.lineEdit_2.text()
        id_sezon_liga = self.lineEdit_3.text()
        self.label.setText(" ")
        self.label.adjustSize()
        try:
            if id_sezon_liga.isnumeric():
                database.add_kolejka_rozgrywek(connection, start_kolejki, koniec_kolejki, id_sezon_liga)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                self.label.setText("Upewnij się że wprowadzone id_sezon_liga jest całkowitą wartością liczbową")
                self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_sezon_liga istnieją")
            self.label.adjustSize()
    
    def insert_druzyna(self):
        uic.loadUi("ui/insert_druzyna.ui", self)
        self.pushButton.clicked.connect(self.insert_druzyna_add)
        self.pushButton_2.clicked.connect(self.admin_insert)
        
    def insert_druzyna_add(self):    
        nazwa_druzyna = self.lineEdit.text()
        try:
            database.add_druzyna(connection, nazwa_druzyna)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("NARUSZONO KLUCZE!")
            self.label.adjustSize()

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
        self.pushButton_8.clicked.connect(self.delete_sezon_liga)
        self.pushButton_9.clicked.connect(self.delete_druzyna_szczebel)
        self.pushButton_10.clicked.connect(self.delete_gracz_druzyna)
        self.pushButton_11.clicked.connect(self.delete_mecz)
        self.pushButton_7.clicked.connect(self.loggedasadmin)
####################################################################################3
        # self.pushButton_8.clicked.connect(self.delete_sezon_liga)
        # self.pushButton_9.clicked.connect(self.delete_druzyna_szczebel)
        # self.pushButton_10.clicked.connect(self.delete_gracz_druzyna)
        # self.pushButton_11.clicked.connect(self.delete_mecz)
    def delete_sezon_liga(self):
        uic.loadUi("ui/delete_sezon_liga.ui", self)
        self.pushButton.clicked.connect(self.delete_sezon_liga_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
    def delete_sezon_liga_add(self):
        id_sezonu = self.lineEdit.text()
        id_ligi = self.lineEdit_2.text()
        id_szczebla = int(self.lineEdit_3.text())
        try:
            database.delete_sezon_liga(connection, id_sezonu, id_ligi, id_szczebla)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_sezonu, id_ligi, id_szczebla nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()

    def delete_druzyna_szczebel(self):
        uic.loadUi("ui/delete_druzyna_szczebel.ui", self)
        self.pushButton.clicked.connect(self.delete_druzyna_szczebel_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
    def delete_druzyna_szczebel_add(self):
        id_sezon_liga = self.lineEdit.text()
        id_druzyny = self.lineEdit_2.text()
        try:
            database.delete_druzyna_szczebel(connection, id_sezon_liga, id_druzyny)
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_sezon_liga, id_druzyny nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()
    
    def delete_gracz_druzyna(self):
        uic.loadUi("ui/delete_gracz_druzyna.ui", self)
        self.pushButton.clicked.connect(self.delete_gracz_druzyna_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
    def delete_gracz_druzyna_add(self):
        id_gracza = self.lineEdit.text()
        id_druzyna_szczebel = self.lineEdit_2.text()
        try:
            database.delete_gracz_druzyna(connection, id_gracza, id_druzyna_szczebel)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się, że wprowadzanie przez ciebie dane: id_gracza, id_druzyna_szczebel nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()


    def delete_mecz(self):
        uic.loadUi("ui/delete_mecz.ui", self)
        self.pushButton.clicked.connect(self.delete_mecz_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
    def delete_mecz_add(self):
        wynik = self.lineEdit.text()
        id_druzyna_szczebel_1 = self.lineEdit.text()
        id_druzyna_szczebel_2 = self.lineEdit.text()
        try:
            database.delete_mecz(connection, wynik, id_druzyna_szczebel_1, id_druzyna_szczebel_2)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_druzyna_szczebel_1, id_druzyna_szczebel_2 nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()


#######################################################################################
    def delete_gracz(self):
        uic.loadUi("ui/delete_gracz.ui", self)
        self.pushButton.clicked.connect(self.delete_gracz_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
    
    def delete_gracz_add(self):    
        imie = self.lineEdit.text()
        nazwisko = self.lineEdit_2.text()
        rok_urodzenia = int(self.lineEdit_3.text())
        try:
            database.delete_gracz(connection, imie, nazwisko, rok_urodzenia)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że id_gracz o wprowadzanych \n przez ciebie danych: imie, nazwisko, rok_urodzenia nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()
        
    def delete_sezon(self):
        uic.loadUi("ui/delete_sezon.ui", self)
        self.pushButton.clicked.connect(self.delete_sezon_add)
        self.pushButton_2.clicked.connect(self.admin_delete)

    def delete_sezon_add(self):    
        rok = int(self.lineEdit.text())
        poczatek_sezonu = self.lineEdit_2.text()
        koniec_sezonu = self.lineEdit_3.text()
        try:
            database.delete_sezon(connection, rok, poczatek_sezonu, koniec_sezonu)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że id_sezonu o wprowadzanych \n przez ciebie danych: rok, poczatek_sezonu, koniec_sezonu nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()

    def delete_liga(self):
        uic.loadUi("ui/delete_liga.ui", self)
        self.pushButton.clicked.connect(self.delete_liga_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
        
    def delete_liga_add(self):    
        nazwa = self.lineEdit.text()
        try:
            database.delete_liga(connection, nazwa)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że id_ligi o wprowadzanych \n przez ciebie danych: nazwa nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()


    def delete_szczebel(self):
        uic.loadUi("ui/delete_szczebel.ui", self)
        self.pushButton.clicked.connect(self.delete_szczebel_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
        
    def delete_szczebel_add(self):    
        nazwa_szczebla = self.lineEdit.text()
        
        try:
            database.delete_szczebel(connection, nazwa_szczebla)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że id_szczebla o wprowadzanych \n przez ciebie danych: nazwa_szczebla nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()

    def delete_kolejka_rozgrywek(self):
        uic.loadUi("ui/delete_kolejka_rozgrywek.ui", self)
        self.pushButton.clicked.connect(self.delete_kolejka_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
        
    def delete_kolejka_add(self):    
        start_kolejki = self.lineEdit.text()
        koniec_kolejki = self.lineEdit_2.text()
        id_sezon_liga = int(self.lineEdit_3.text())
        try:
            database.delete_kolejka_rozgrywek(connection, start_kolejki, koniec_kolejki, id_sezon_liga)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_sezonu_liga nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()
        
    
    def delete_druzyna(self):
        uic.loadUi("ui/delete_druzyna.ui", self)
        self.pushButton.clicked.connect(self.delete_druzyna_add)
        self.pushButton_2.clicked.connect(self.admin_delete)
        
    def delete_druzyna_add(self):    
        nazwa_druzyna = self.lineEdit.text()
        try:
            database.delete_druzyna(connection, nazwa_druzyna)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że id_druzyny o wprowadzanych \n przez ciebie danych: nazwa_druzyny nie są wykorzystywane przez inną tabele!")
            self.label.adjustSize()


    
    ############################################33 OLEJNIK        
    def admin_update(self):
        modyfikowane = self.comboBox.currentText()
        if modyfikowane == "GRACZ":
            #uic.loadUi("admin_update_gracz.ui", self)
            self.admin_update_gracz()
        elif modyfikowane == "SEZON":
            self.admin_update_sezon()
        elif modyfikowane == "SEZON_LIGA":
            self.admin_update_sezon_liga()
        elif modyfikowane == "KOLEJKA_ROZGRYWEK":
            self.admin_update_kolejka_rozgrywek()
        elif modyfikowane == "DRUZYNA":
            self.admin_update_druzyna()
        elif modyfikowane == "DRUZYNA_SZCZEBEL":
            self.admin_update_druzyna_szczebel()
        elif modyfikowane == "LIGA":
            self.admin_update_liga()
        elif modyfikowane == "SZCZEBEL_ROZGRYWEK":
            self.admin_update_szczebel()
        elif modyfikowane == "GRACZ_DRUZYNA":
            self.admin_update_graczdruzyna()
        elif modyfikowane == "MECZ":
            self.admin_update_mecz()
        else:
            print("wybierz co chcesz modyfkiowac")

    def admin_update_gracz(self):
        uic.loadUi("ui/admin_update_gracz.ui", self)
        self.pushButton.clicked.connect(self.print_gracze_id)
        self.pushButton_2.clicked.connect(self.update_gracz)
        self.pushButton_3.clicked.connect(self.loggedasadmin)
    def update_gracz(self):
        tekst = self.lineEdit.text()
        nowe_imie = self.lineEdit_2.text()
        nowe_nazwisko = self.lineEdit_3.text()
        nowy_rok = self.lineEdit_4.text()
        self.label.setText(" ")
        self.label.adjustSize()
        try:
            if nowy_rok.isnumeric():
                database.update_gracz_id(connection, nowe_imie, nowe_nazwisko, nowy_rok, tekst)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                self.label.setText("Upewnij się że wprowadzony rok jest liczbą całkowitą np. 1999")
                self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("NARUSZONO KLUCZE!")
            self.label.adjustSize()
        
    def print_gracze_id(self): # printuje gracza o ID podanym w lineEdit
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_GRACZA   |    IMIE    |    NAZWISKO    |    ROK_URODZENIA\n")
        gracz = database.select_gracz_id_admin(connection, tekst)
        try:
            self.textBrowser.append(" | ".join(map(str,gracz)))
        except TypeError as err:
            self.textBrowser.append("Podaj istniejące ID_GRACZA")

    def admin_update_sezon(self):
        uic.loadUi("ui/admin_update_sezon.ui", self)
        self.pushButton.clicked.connect(self.print_sezon_id)
        self.pushButton_2.clicked.connect(self.update_sezon)
        self.pushButton_3.clicked.connect(self.loggedasadmin)
    def update_sezon(self):
        tekst = self.lineEdit.text()
        nowe_rok = self.lineEdit_2.text()
        nowe_paczatek = self.lineEdit_3.text()
        nowy_koniec = self.lineEdit_4.text()
        self.label.setText(" ")
        self.label.adjustSize()
        try:
            if nowe_rok.isnumeric():
                database.update_sezon_id(connection, nowe_rok, nowe_paczatek, nowy_koniec, tekst)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                self.label.setText("Upewnij się że rok się całkowitą liczbą np. 1999")
                self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("NARUSZONO KLUCZE!")
            self.label.adjustSize()
        
    def print_sezon_id(self):
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_SEZONU   |    ROK    |    POCZATEK    |    KONIEC\n")
        sezon = database.select_sezon_id_admin(connection, tekst)
        try:
            self.textBrowser.append(" | ".join(map(str,sezon)))
        except TypeError as err:
            self.textBrowser.append("Podaj istniejące ID_SEZONU")

    # def admin_update_liga(self):
    #     uic.loadUi("ui/admin_update_liga.ui", self)
    #     self.pushButton.clicked.connect(self.print_sezon_id)
    #     self.pushButton_2.clicked.connect(self.update_sezon)
        ##########################################################################################################33
    def admin_update_sezon_liga(self):
        uic.loadUi("ui/admin_update_sezon_liga.ui", self)
        self.pushButton.clicked.connect(self.print_sezon_liga_id)
        self.pushButton_2.clicked.connect(self.update_sezon_liga)
        self.pushButton_3.clicked.connect(self.loggedasadmin)
    def update_sezon_liga(self):
        tekst = self.lineEdit.text()
        id_sezonu = self.lineEdit_2.text()
        id_ligi = self.lineEdit_3.text()
        id_szczebla = self.lineEdit_4.text()
        self.label.setText(" ")
        self.label.adjustSize()
        try:
            if id_sezonu.isnumeric() and id_ligi.isnumeric() and id_szczebla.isnumeric():
                database.update_sezon_liga_id(connection, id_sezonu, id_ligi, id_szczebla, tekst)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                self.label.setText("Upewnij się że id_sezonu ligi oraz szczeble to wartości liczbowe całkowite")
                self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_sezonu, id_ligi, id_szczebla istnieją!")
            self.label.adjustSize()
    def print_sezon_liga_id(self):
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_SEZON_LIGA   |    ID_SEZONU    |    ID_LIGI     |    ID_SZCZEBLA\n")
        sezon = database.select_sezon_liga_id_admin(connection, tekst)
        try:
            self.textBrowser.append(" | ".join(map(str,sezon)))
        except TypeError as err:
            self.textBrowser.append("Podaj istniejące ID_SEZON_LIGA")
        ################################################################################3
    def admin_update_kolejka_rozgrywek(self):
        uic.loadUi("ui/admin_update_kolejka_rozgrywek.ui", self)
        self.pushButton.clicked.connect(self.print_kolejka_rozgrywek_id)
        self.pushButton_2.clicked.connect(self.update_kolejka_rozgrywek)
        self.pushButton_3.clicked.connect(self.loggedasadmin)
    def update_kolejka_rozgrywek(self):
        tekst = self.lineEdit.text()
        start_kolejki = self.lineEdit_2.text()
        koniec_kolejki = self.lineEdit_3.text()
        id_sezon_liga = self.lineEdit_4.text()
        self.label.setText(" ")
        self.label.adjustSize()
        try:
            if id_sezon_liga.isnumeric():
                database.update_kolejka_rozgrywek_id(connection, start_kolejki, koniec_kolejki, id_sezon_liga, tekst)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                self.label.setText("Upewnij się że id_sezon_liga jest calkowita liczba")
                self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_sezon_liga istnieją!")
            self.label.adjustSize()
    def print_kolejka_rozgrywek_id(self):
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_KOLEJKI   |    START KOLEJKI    |    KONIEC KOLEJKI     |    ID_SEZON_LIGA\n")
        sezon = database.select_kolejka_rozgrywek_id_admin(connection, tekst)
        try:
            self.textBrowser.append(" | ".join(map(str,sezon)))
        except TypeError as err:
            self.textBrowser.append("Podaj istniejące ID_KOLEJKA_ROZGRYWEK")

    #########################################################################
    def admin_update_druzyna(self):
        uic.loadUi("ui/admin_update_druzyna.ui", self)
        self.pushButton.clicked.connect(self.print_druzyna_id)
        self.pushButton_2.clicked.connect(self.update_druzyna)
        self.pushButton_3.clicked.connect(self.loggedasadmin)
    def update_druzyna(self):
        tekst = self.lineEdit.text()
        nazwa_druzyna = self.lineEdit_2.text()
        try:
            database.update_druzyna_id(connection, nazwa_druzyna, tekst)
            self.label.setText(" ")
            self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("NARUSZONO KLUCZE!")
            self.label.adjustSize()
        
    def print_druzyna_id(self):
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_DRUZYNY   |    NAZWA DRUZYNY\n")
        sezon = database.select_druzyna_id_admin(connection, tekst)
        try:
            self.textBrowser.append(" | ".join(map(str,sezon)))
        except TypeError as err:
            self.textBrowser.append("Podaj istniejące ID_DRUZYNA")

    ###############################################################
    def admin_update_druzyna_szczebel(self):
        uic.loadUi("ui/admin_update_druzyna_szczebel.ui", self)
        self.pushButton.clicked.connect(self.print_druzyna_szczebel_id)
        self.pushButton_2.clicked.connect(self.update_druzyna_szczebel)
        self.pushButton_3.clicked.connect(self.loggedasadmin)
    def update_druzyna_szczebel(self):
        tekst = self.lineEdit.text()
        id_sezon_liga = self.lineEdit_2.text()
        id_druzyny = self.lineEdit_3.text()
        self.label.setText(" ")
        self.label.adjustSize()
        try:
            if id_sezon_liga.isnumeric() and id_druzyny.isnumeric():
                database.update_druzyna_szczebel_id(connection, id_sezon_liga, id_druzyny, tekst)
                self.label.setText(" ")
                self.label.adjustSize()
            else:
                self.label.setText("Upewnij się że podane id_sezon_liga oraz id_druzyny to liczby calkowite")
                self.label.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucze !!!!!!")
            self.label.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_sezon_liga, id_druzyny istnieją!")
            self.label.adjustSize()
    def print_druzyna_szczebel_id(self):
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_DRUZYNA_SZCZEBEL   |    ID_DRUZYNY    |    ID_SEZON_LIGA\n")
        
        sezon = database.select_druzyna_szczebel_id_admin(connection, tekst)
        
        try:
            self.textBrowser.append(" | ".join(map(str,sezon)))
        except TypeError as err:
            self.textBrowser.append("Podaj istniejące ID_DRUZYNA_SZCZEBEL")
    ####################################################################################################################

    def admin_update_liga(self):
        uic.loadUi("ui/admin_update_liga.ui", self)
        self.pushButton.clicked.connect(self.print_liga_id)
        self.pushButton_2.clicked.connect(self.update_liga)
        self.pushButton_x.clicked.connect(self.loggedasadmin)
    def update_liga(self):
        tekst = self.lineEdit.text()
        nowe_nazwa = self.lineEdit_2.text()
        try:
            database.update_liga_id(connection, nowe_nazwa, tekst)
            self.label_x.setText(" ")
        except sqlite3.IntegrityError as er:
            self.label_x.setText("NARUSZONO KLUCZ OBCY")
            self.label_x.adjustSize()
            print("naruszono klucz obcy")
    def print_liga_id(self):
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_LIGI   |    NAZWA\n")
        liga = database.select_liga_id_admin(connection, tekst)
        try:
            self.textBrowser.append(" | ".join(map(str,liga)))
        except TypeError as err:
            self.textBrowser.append("Podaj istniejące ID_LIGI")

    def admin_update_szczebel(self):
        uic.loadUi("ui/admin_update_szczebel.ui", self)
        self.pushButton.clicked.connect(self.print_szczebel_id)
        self.pushButton_2.clicked.connect(self.update_szczebel)
        self.pushButton_3.clicked.connect(self.loggedasadmin)
    def update_szczebel(self):
        tekst = self.lineEdit.text()
        nowe_nazwa = self.lineEdit_2.text()
        try:
            database.update_szczebel_id(connection, nowe_nazwa, tekst)
            self.label_4.setText(" ")
        except sqlite3.IntegrityError as er:
            self.label_4.setText("NARUSZONO KLUCZ OBCY")
            self.label_4.adjustSize()
            print("naruszono klucz obcy")
    def print_szczebel_id(self):
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_SZCZEBLA   |    NAZWA SZCZEBLA\n")
        szczebel = database.select_szczebel_id_admin(connection, tekst)
        try:
            self.textBrowser.append(" | ".join(map(str,szczebel)))
        except TypeError as err:
            self.textBrowser.append("Podaj istniejące ID_SZCZEBLA")

    def admin_update_graczdruzyna(self):
        uic.loadUi("ui/admin_update_graczdruzyna.ui", self)
        self.pushButton.clicked.connect(self.print_graczdruzyna_id)
        self.pushButton_2.clicked.connect(self.update_graczdruzyna)
        self.pushButton_x.clicked.connect(self.loggedasadmin)
    def update_graczdruzyna(self):
        tekst = self.lineEdit.text()
        nowe_id_gracza = self.lineEdit_2.text()
        nowe_id_druzyna_szczebel = self.lineEdit_3.text()
        self.label_x.setText(" ")
        self.label_x.adjustSize()
        try:
            if nowe_id_gracza.isnumeric() and nowe_id_druzyna_szczebel.isnumeric():
                database.update_graczdruzyna_id(connection, nowe_id_gracza, nowe_id_druzyna_szczebel, tekst)
                self.label_x.setText(" ")
                self.label_x.adjustSize()
            else:
                self.label_x.setText("Upewnij się że podane id_gracza oraz id_gracz_druzyna to liczby całkowite")
                self.label_x.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucz obcy")
            self.label_x.setText("NARUSZONO KLUCZ OBCY")
            self.label_x.adjustSize()
    def print_graczdruzyna_id(self):
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_GRACZ_DRUZYNA   |    ID_GRACZA    |     ID_DRUZYNA_SZCZEBEL\n")
        x = database.select_graczdruzyna_id_admin(connection, tekst)
        try:
            self.textBrowser.append(" | ".join(map(str,x)))
        except TypeError as err:
            self.textBrowser.append("Naruszono klucz obcy! Upewnij się, że wprowadzanie przez ciebie dane: id_gracza, id_druzyna_szczebel istnieją!")

    def admin_update_mecz(self):
        uic.loadUi("ui/admin_update_mecz.ui", self)
        self.pushButton.clicked.connect(self.print_mecz_id)
        self.pushButton_2.clicked.connect(self.update_mecz)
        self.pushButton_3.clicked.connect(self.loggedasadmin)
    def update_mecz(self):
        tekst = self.lineEdit.text()
        nowe_wynik = self.lineEdit_2.text()
        nowe_id_druzyna_szczebel1 = self.lineEdit_3.text()
        nowe_id_druzyna_szczebel2 = self.lineEdit_4.text()
        self.label_6.setText(" ")
        self.label_6.adjustSize()
        try:
            if nowe_id_druzyna_szczebel1.isnumeric() and nowe_id_druzyna_szczebel2.isnumeric() and (re.match('^\d:\d', nowe_wynik)):
                database.update_mecz_id(connection, nowe_wynik, nowe_id_druzyna_szczebel1, nowe_id_druzyna_szczebel2, tekst)
                self.label_6.setText(" ")
                self.label_6.adjustSize()
            else:
                self.label_6.setText("Upewnij się że id_druzyn są liczbami oraz wynik jest w formacie gol_1:gol_2")
                self.label_6.adjustSize()
        except sqlite3.IntegrityError as er:
            print("naruszono klucz obcy")
            self.label_6.setText("Naruszono klucz obcy! Upewnij się że wprowadzane \n przez ciebie dane: id_druzyna_szczebel_1, id_druzyna_szczebel_2 istnieją!")
            self.label_6.adjustSize()
    def print_mecz_id(self):
        tekst = self.lineEdit.text()
        self.textBrowser.clear()
        self.textBrowser.append("ID_MECZU   |    WYNIK    |     ID_DRUZYNA_SZCZEBEL1    |    ID_DRUZYNA_SZCZEBEL2\n")
        x = database.select_mecz_id_admin(connection, tekst)
        try:
            self.textBrowser.append(" | ".join(map(str,x)))
        except TypeError as err:
            self.textBrowser.append("Podaj istniejące ID_MECZU")

    

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