import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import *


CREATE_GRACZ = """
CREATE TABLE IF NOT EXISTS GRACZ
(id_gracza INTEGER PRIMARY KEY,
imie TEXT NOT NULL,
nazwisko TEXT NOT NULL,
rok_urodzenia integer NOT NULL);
"""


##### tutaj brakuje foreign key
CREATE_GRACZ_DRUZYNA = """
CREATE TABLE IF NOT EXISTS GRACZ_DRUZYNA
(id_gracz_druzyna INTEGER PRIMARY KEY,
id_gracza INTEGER NOT NULL,
FOREIGN KEY(id_gracza) REFERENCES GRACZ(id_gracza)
);
"""

CREATE_TABLE_SEZON = """
CREATE TABLE IF NOT EXISTS SEZON
(id_sezonu INTEGER PRIMARY KEY,
rok INTEGER NOT NULL, 
poczatek_sezonu DATE NOT NULL, 
koniec_sezonu DATE NOT NULL);
"""

CREATE_TABLE_LIGA = """
CREATE TABLE IF NOT EXISTS LIGA
(id_ligi INTEGER PRIMARY KEY, 
nazwa TEXT NOT NULL);
"""

CREATE_TABLE_szczebel = """
CREATE TABLE IF NOT EXISTS SZCZEBEL_ROZGRYWEK
(id_szczebla INTEGER PRIMARY KEY, 
nazwa_szczebla TEXT NOT NULL);
"""

CREATE_TABLE_SEZON_LIGA = """
CREATE TABLE IF NOT EXISTS SEZON_LIGA
(id_sezon_liga INTEGER PRIMARY KEY,
id_sezonu INTEGER NOT NULL,
id_ligi INTEGER NOT NULL,
id_szczebla INTEGER NOT NULL,
FOREIGN KEY(id_sezonu) REFERENCES SEZON(id_sezonu), 
FOREIGN KEY(id_ligi) REFERENCES LIGA(id_ligi), 
FOREIGN KEY(id_szczebla) REFERENCES SZCZEBEL_ROZGRYWEK(id_szczebla));
"""

KOLEJKA_ROZGRYWEK = """
CREATE TABLE IF NOT EXISTS KOLEJKA_ROZGRYWEK
(id_kolejki INTEGER PRIMARY KEY,
start_kolejki INTEGER NOT NULL,
koniec_kolejki INTEGER NOT NULL,
id_sezon_liga INTEGER NOT NULL,
FOREIGN KEY(id_sezon_liga) REFERENCES SEZON_LIGA(id_sezon_liga));
"""

CREATE_DRUZYNA = """
CREATE TABLE IF NOT EXISTS DRUZYNA
(id_druzyny INTEGER PRIMARY KEY,
nazwa_druzyny TEXT NOT NULL);
"""

CREATE_DRUZYNA_SZCZEBEL = """
CREATE TABLE IF NOT EXISTS DRUZYNA_SZCZEBEL
(id_druzyna_szczebel INTEGER PRIMARY KEY,
id_sezon_liga INTEGER NOT NULL,
id_druzyny INTEGER NOT NULL,
FOREIGN KEY(id_sezon_liga) REFERENCES SEZON_LIGA(id_sezon_liga),
FOREIGN KEY(id_druzyny) REFERENCES DRUZYNA(id_druzyny));
"""

CREATE_MECZ = """
CREATE TABLE IF NOT EXISTS MECZ
(id_meczu INTEGER PRIMARY KEY,
wynik TEXT NOT NULL,
FOREIGN KEY(id_druzyna_szczebel_1) REFERENCES SEZON_LIGA(id_druzyna_szczebel),
FOREIGN KEY(id_druzyna_szczebel_2) REFERENCES DRUZYNA(id_druzyna_szczebel));
"""

CREATE_SUGESTIE = """
CREATE TABLE IF NOT EXISTS SUGESTIE
(id_sugestii INTEGER PRIMARY KEY,
sugestia TEXT NOT NULL);
"""
# """ !!!!!!!!!!!!!!!!!!!!!!!

INSERT_SUGESTIA = "INSERT INTO SUGESTIE (sugestia) VALUES (?);"

INSERT_GRACZ = "INSERT INTO GRACZ (imie, nazwisko, rok_urodzenia) VALUES (?, ?, ?);"

##
INSERT_LIGA = "INSERT INTO LIGA (nazwa) VALUES (?);"

INSERT_SEZON ="INSERT INTO SEZON (rok, poczatek_sezonu, koniec_sezonu) VALUES (?, ?, ?);"

INSERT_SZCZEBEL = "INSERT INTO SZCZEBEL_ROZGRYWEK (nazwa_szczebla) VALUES (?);"

INSERT_KOLEJKA_ROZGRYWEK = "INSERT INTO KOLEJKA_ROZGRYWEK (start_kolejki, koniec_kolejki, id_sezon_liga) VALUES (?, ?, ?);"

INSERT_DRUZYNA = "INSERT INTO DRUZYNA (nazwa_druzyny) VALUES (?);"

##
SELECT_GRACZ = "SELECT * FROM GRACZ;"
SELECT_SZUKANE_GRACZE = "SELECT * FROM GRACZ WHERE imie = ? OR nazwisko = ? OR rok_urodzenia = ?"

SELECT_DRUZYNY = "SELECT * FROM DRUZYNA;"
SELECT_SEZONY = "SELECT * FROM SEZON;"
SELECT_LIGI = "SELECT * FROM LIGA;"
SELECT_KOLEJKI = "SELECT * FROM KOLEJKA_ROZGRYWEK;"
SELECT_SEZONY_LIGI = "SELECT * FROM SEZON_LIGA;"
SELECT_DRUZYNY_SZCZEBLE = "SELECT * FROM DRUZYNA_SZCZEBEL;"
SELECT_GRACZE_DRUZYNY = "SELECT * FROM GRACZ_DRUZYNA;"
SELECT_SZCZEBLE = "SELECT * FROM SZCZEBEL_ROZGRYWEK;"

SELECT_SUGESTIA = "SELECT * FROM SUGESTIE;"


DELETE_SEZON = "DELETE FROM SEZON WHERE (rok = ?) AND (poczatek_sezonu = ?) AND (koniec_sezonu = ?);"

DELETE_LIGA = "DELETE FROM LIGA WHERE nazwa = ?;"

DELETE_SZCZEBEL = "DELETE FROM SZCZEBEL_ROZGRYWEK WHERE nazwa_szczebla = ?;"

DELETE_KOLEJKA_ROZGRYWEK = "DELETE FROM KOLEJKA_ROZGRYWEK WHERE (start_kolejki = ?) AND (koniec_kolejki = ?) AND (id_sezon_liga = ?);"

DELETE_DRUZYNA = "DELETE FROM DRUZYNA WHERE (nazwa_druzyny = ?);"

DELETE_GRACZ = "DELETE FROM GRACZ WHERE (imie = ?) AND (nazwisko = ?) AND (rok_urodzenia = ?);"


lista_tabel = [CREATE_GRACZ, CREATE_GRACZ_DRUZYNA, CREATE_TABLE_LIGA, CREATE_TABLE_szczebel, CREATE_TABLE_SEZON_LIGA, KOLEJKA_ROZGRYWEK, CREATE_DRUZYNA, CREATE_DRUZYNA_SZCZEBEL, CREATE_TABLE_SEZON, CREATE_SUGESTIE]

def connect():
    return sqlite3.connect("database.db")

def create_tables(connection):
    with connection:
        for tabela in lista_tabel:
            connection.execute(tabela)

def add_gracz(connection, imie, nazwisko, rok_urodzenia):
    with connection:
        connection.execute(INSERT_GRACZ, (imie, nazwisko, rok_urodzenia))

def add_liga(connection, nazwa):
    with connection:
        connection.execute(INSERT_LIGA, (nazwa,))

def add_sezon(connection, rok, poczatek_sezonu, koniec_sezonu):
    with connection:
        connection.execute(INSERT_SEZON, (rok, poczatek_sezonu, koniec_sezonu))

def add_szczebel(connection, nazwa_szczebla):
    with connection:
        connection.execute(INSERT_SZCZEBEL, (nazwa_szczebla,))

def add_kolejka_rozgrywek(connection, start_kolejki, koniec_kolejki, id_sezon_liga):
    with connection:
        connection.execute(INSERT_KOLEJKA_ROZGRYWEK, (start_kolejki, koniec_kolejki, id_sezon_liga))

def add_druzyna(connection, nazwa_druzyny):
    with connection:
        connection.execute(INSERT_DRUZYNA, (nazwa_druzyny,))

def select_gracz(connection):
    with connection:
        return connection.execute(SELECT_GRACZ).fetchall()

# zaczynam dodawac  
def select_szukane_gracze(connection, wartosc, rok):
    with connection:
        return connection.execute(SELECT_SZUKANE_GRACZE, (wartosc, wartosc, rok)).fetchall()
    

#DRUZYNY
def select_druzyny(connection):
    with connection:
        return connection.execute(SELECT_DRUZYNY).fetchall()
    
#sezony
def select_sezon(connection):
    with connection:
        return connection.execute(SELECT_SEZONY).fetchall()
    
def select_liga(connection):
    with connection:
        return connection.execute(SELECT_LIGI).fetchall()
    
def select_kolejka(connection):
    with connection:
        return connection.execute(SELECT_KOLEJKI).fetchall()

def select_sezon_liga(connection):
    with connection:
        return connection.execute(SELECT_SEZONY_LIGI).fetchall()

def select_druzyna_szczebel(connection):
    with connection:
        return connection.execute(SELECT_DRUZYNY_SZCZEBLE).fetchall()   

def select_gracz_druzyna(connection):
    with connection:
        return connection.execute(SELECT_GRACZE_DRUZYNY).fetchall() 

def select_szczebel(connection):
    with connection:
        return connection.execute(SELECT_SZCZEBLE).fetchall()
    
def select_sugestia(connection):
    with connection:
        return connection.execute(SELECT_SUGESTIA).fetchall()
    


def delete_sezon(connection, rok, poczatek_sezonu, koniec_sezonu):
    with connection:
        connection.execute(DELETE_SEZON, (rok, poczatek_sezonu, koniec_sezonu))



def delete_gracz(connection, imie, nazwisko, rok_urodzenia):
    with connection:
        connection.execute(DELETE_GRACZ, (imie, nazwisko, rok_urodzenia))

def delete_liga(connection, nazwa):
    with connection:
        connection.execute(DELETE_LIGA, (nazwa,))


def delete_szczebel(connection, nazwa_szczebla):
    with connection:
        connection.execute(DELETE_SZCZEBEL, (nazwa_szczebla,))

def delete_kolejka_rozgrywek(connection, start_kolejki, koniec_kolejki, id_sezon_liga):
    with connection:
        connection.execute(DELETE_KOLEJKA_ROZGRYWEK, (start_kolejki, koniec_kolejki, id_sezon_liga))

def delete_druzyna(connection, nazwa_druzyny):
    with connection:
        connection.execute(DELETE_DRUZYNA, (nazwa_druzyny,))

def insert_sugestia(connection, sugestia):
    with connection:
        connection.execute(INSERT_SUGESTIA, (sugestia,))
