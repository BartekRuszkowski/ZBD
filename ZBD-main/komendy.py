import sqlite3

lista = ["insert into sezon (rok, poczatek_sezonu, koniec_sezonu) values (1999, 01/09/1999, 01/06/1999);",
"insert into sezon (rok, poczatek_sezonu, koniec_sezonu) values (2000, 01/09/2000, 01/06/2001);",
"insert into sezon (rok, poczatek_sezonu, koniec_sezonu) values (2001, 01/09/2001, 01/06/2002);",
"insert into sezon (rok, poczatek_sezonu, koniec_sezonu) values (2002, 01/09/2002, 01/06/2003);",
"insert into sezon (rok, poczatek_sezonu, koniec_sezonu) values (2003, 01/09/2003, 01/06/2004);",
'INSERT INTO LIGA (nazwa) values ("Ekstraklasa");',
'INSERT INTO LIGA (nazwa) values ("Premier League");',
'INSERT INTO LIGA (nazwa) values ("Premiership");',
'INSERT INTO LIGA (nazwa) values ("Serie A");',
'INSERT INTO LIGA (nazwa) values ("Serie B");',
'INSERT INTO SZCZEBEL_ROZGRYWEK (nazwa_szczebla) VALUES ("Pierwsza Liga");',
'INSERT INTO SZCZEBEL_ROZGRYWEK (nazwa_szczebla) VALUES ("Druga Liga");',
"INSERT INTO SEZON_LIGA (id_sezonu, id_ligi, id_szczebla) VALUES (1, 1, 1);",
"INSERT INTO SEZON_LIGA (id_sezonu, id_ligi, id_szczebla) VALUES (1, 2, 1);",
"INSERT INTO SEZON_LIGA (id_sezonu, id_ligi, id_szczebla) VALUES (1, 3, 2);",
"INSERT INTO SEZON_LIGA (id_sezonu, id_ligi, id_szczebla) VALUES (1, 4, 1);",
"INSERT INTO SEZON_LIGA (id_sezonu, id_ligi, id_szczebla) VALUES (1, 5, 2);",
"INSERT INTO KOLEJKA_ROZGRYWEK (start_kolejki, koniec_kolejki, id_sezon_liga) VALUES ('01/09', '08/09', 1);",
"INSERT INTO KOLEJKA_ROZGRYWEK (start_kolejki, koniec_kolejki, id_sezon_liga) VALUES ('01/09', '08/09', 2);",
"INSERT INTO KOLEJKA_ROZGRYWEK (start_kolejki, koniec_kolejki, id_sezon_liga) VALUES ('01/09', '08/09', 3);",
"INSERT INTO KOLEJKA_ROZGRYWEK (start_kolejki, koniec_kolejki, id_sezon_liga) VALUES ('01/09', '08/09', 4);",
"INSERT INTO KOLEJKA_ROZGRYWEK (start_kolejki, koniec_kolejki, id_sezon_liga) VALUES ('01/09', '08/09', 5);",
'INSERT INTO DRUZYNA (nazwa_druzyny) values ("Lech Poznan");',
'INSERT INTO DRUZYNA (nazwa_druzyny) values ("Juventus FC");',
'INSERT INTO DRUZYNA (nazwa_druzyny) values ("Arsenal FC");',
'INSERT INTO DRUZYNA (nazwa_druzyny) values ("Chalsea");',
'INSERT INTO DRUZYNA (nazwa_druzyny) values ("Salernitana");',
'INSERT INTO DRUZYNA (nazwa_druzyny) values ("Everton");',
"INSERT INTO GRACZ (imie, nazwisko, rok_urodzenia) VALUES ('Janusz', 'Kowlaski', 1973);",
"INSERT INTO GRACZ (imie, nazwisko, rok_urodzenia) VALUES ('Gianluigi', 'Buffon', 1980);",
"INSERT INTO GRACZ (imie, nazwisko, rok_urodzenia) VALUES ('Thiery', 'Henry', 1977);",
"INSERT INTO GRACZ (imie, nazwisko, rok_urodzenia) VALUES ('John', 'Terry', 1978);",
"INSERT INTO GRACZ (imie, nazwisko, rok_urodzenia) VALUES ('Edin', 'Degoe', 1977);",
"INSERT INTO GRACZ (imie, nazwisko, rok_urodzenia) VALUES ('Dane', 'Vise', 1979);",
"INSERT INTO DRUZYNA_SZCZEBEL (id_sezon_liga, id_druzyny) VALUES (1,1);",
"INSERT INTO DRUZYNA_SZCZEBEL (id_sezon_liga, id_druzyny) VALUES (4,2);",
"INSERT INTO DRUZYNA_SZCZEBEL (id_sezon_liga, id_druzyny) VALUES (2,3);",
"INSERT INTO DRUZYNA_SZCZEBEL (id_sezon_liga, id_druzyny) VALUES (2,4);",
"INSERT INTO DRUZYNA_SZCZEBEL (id_sezon_liga, id_druzyny) VALUES (5,5);",
"INSERT INTO GRACZ_DRUZYNA (id_gracza, id_druzyna_szczebel) VALUES (1,1);",
"INSERT INTO GRACZ_DRUZYNA (id_gracza, id_druzyna_szczebel) VALUES (2,2);",
"INSERT INTO GRACZ_DRUZYNA (id_gracza, id_druzyna_szczebel) VALUES (3,3);",
"INSERT INTO GRACZ_DRUZYNA (id_gracza, id_druzyna_szczebel) VALUES (4,4);",
'INSERT INTO MECZ (wynik, id_druzyna_szczebel_1, id_druzyna_szczebel_2) VALUES ("2:0", 3, 4);',
'INSERT INTO MECZ (wynik, id_druzyna_szczebel_1, id_druzyna_szczebel_2) VALUES ("3:0", 4, 3);']

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
id_druzyna_szczebel INTEGER NOT NULL,
FOREIGN KEY(id_gracza) REFERENCES GRACZ(id_gracza),
FOREIGN KEY(id_druzyna_szczebel) REFERENCES DRUZYNA_SZCZEBEL(id_druzyna_szczebel)
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
start_kolejki TEXT NOT NULL,
koniec_kolejki TEXT NOT NULL,
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
id_druzyna_szczebel_1 INTEGER NOT NULL,
id_druzyna_szczebel_2 INTEGER NOT NULL,
FOREIGN KEY(id_druzyna_szczebel_1) REFERENCES DRUZYNA_SZCZEBEL(id_druzyna_szczebel),
FOREIGN KEY(id_druzyna_szczebel_2) REFERENCES DRUZYNA_SZCZEBEL(id_druzyna_szczebel));
"""

CREATE_SUGESTIE = """
CREATE TABLE IF NOT EXISTS SUGESTIE
(id_sugestii INTEGER PRIMARY KEY,
sugestia TEXT NOT NULL);
"""
lista_tabel = [CREATE_GRACZ, CREATE_GRACZ_DRUZYNA, CREATE_TABLE_LIGA, CREATE_TABLE_szczebel, CREATE_TABLE_SEZON_LIGA, KOLEJKA_ROZGRYWEK, CREATE_DRUZYNA, CREATE_DRUZYNA_SZCZEBEL, CREATE_TABLE_SEZON, CREATE_SUGESTIE, CREATE_MECZ]

connection = sqlite3.connect("budowanie.db")

def create_tables(connection):
    with connection:
        for tabela in lista_tabel:
            connection.execute(tabela)

def add(connection):
    with connection:
        for komenda in lista:
            connection.execute(komenda)


create_tables(connection)
add(connection)


