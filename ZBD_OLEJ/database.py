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

# CREATE_MECZ = """
# """ !!!!!!!!!!!!!!!!!!!!!!!

INSERT_GRACZ = "INSERT INTO GRACZ (imie, nazwisko, rok_urodzenia) VALUES (?, ?, ?);"

INSERT_LIGA = "INSERT INTO LIGA (nazwa) VALUES (?);"

INSERT_SEZON ="INSERT INTO SEZON (rok, poczatek_sezonu, koniec_sezonu) VALUES (?, ?, ?);"

INSERT_SZCZEBEL = "INSERT INTO SZCZEBEL_ROZGRYWEK (nazwa_szczebla) VALUES (?);"

INSERT_KOLEJKA_ROZGRYWEK = "INSERT INTO KOLEJKA_ROZGRYWEK (start_kolejki, koniec_kolejki, id_sezon_liga) VALUES (?, ?, ?);"

INSERT_DRUZYNA = "INSERT INTO DRUZYNA (nazwa_druzyny) VALUES (?);"

SELECT_GRACZ = "SELECT * FROM GRACZ;"
SELECT_SZUKANE_GRACZE = "SELECT * FROM GRACZ WHERE imie = ? OR nazwisko = ? OR rok_urodzenia = ?"

SELECT_DRUZYNY = "SELECT * FROM DRUZYNA;"
SELECT_SEZONY = "SELECT * FROM SEZON;"
SELECT_LIGI = "SELECT * FROM LIGA;"

lista_tabel = [CREATE_GRACZ, CREATE_GRACZ_DRUZYNA, CREATE_TABLE_LIGA, CREATE_TABLE_szczebel, CREATE_TABLE_SEZON_LIGA, KOLEJKA_ROZGRYWEK, CREATE_DRUZYNA, CREATE_DRUZYNA_SZCZEBEL, CREATE_TABLE_SEZON]

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