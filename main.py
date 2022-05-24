import sqlite3

output = []


def wybor_funkcji():
    ilosc = int(input('ilosc '))

    for egz in range(ilosc):
        egz = input('essa ')
        wejscie_tupla = eval(egz)
        funkcja = wejscie_tupla[0]
        # print(wejscie_tupla[0])
        if funkcja == "dodaj":
            # print('wybrano funkcje dodaj')
            dodaj(wejscie_tupla[1:])
        if funkcja == "wypozycz":
            # print('wybrano funkcje wypozycz')
            wypozycz(wejscie_tupla[1:])
        if funkcja == "oddaj":
            # print('wybrano funkcje oddaj')
            oddaj(wejscie_tupla[1:])


class Ksiazka():
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

    ilosc = 0


class czytelnik():
    def __init__(self, name):
        self.name = name
        # self.lista_ksiazek = lista_ksiazek

    def czyMozeWypozyczyc(self):
        pass


# liczba_ksiazek = int(input())

def dodaj(podany_input):
    # podany_input = podany_input
    egzemplarz = podany_input
    # tupla = eval(egzemplarz)
    # lista_ksiazek.append(Ksiazka(tupla[0],tupla[1]))
    # a,b,c = tupla[1:] #sprawdzic to czy dziala
    tytul_do_sql, autor_do_sql, rok_do_sql = egzemplarz
    # tytul_do_sql = tupla[0]
    # autor_do_sql = tupla[1]
    # rok_do_sql = tupla[2]
    query = f"INSERT INTO ksiazki(tytul,autor,rok) VALUES('{tytul_do_sql}','{autor_do_sql}',{rok_do_sql})"
    cursor.execute(query)
    output.append('True')
    # print('True')


# zbior_czytelnikow=set()
def wypozycz(podany_input):
    egzemplarz = podany_input
    czytelnik, tytul_do_sql = egzemplarz
    query_czy_ksiazka_dostepna1 = f"select count(tytul) from ksiazki where tytul='{tytul_do_sql}'"
    cursor.execute(query_czy_ksiazka_dostepna1)
    czy_ksiazka_dostepna1 = cursor.fetchone()[0]
    #12print(f"czy ksiazka dostepna {tytul_do_sql}: {czy_ksiazka_dostepna1}")
    if czy_ksiazka_dostepna1 > 0:

        # czy_jest_w_bazie = 0
        query_czy_jest_w_bazie = f"select count(*) from czytelnicy where imie_nazwisko='{czytelnik}'"
        cursor.execute(query_czy_jest_w_bazie)
        czy_jest_w_bazie = cursor.fetchone()
        # print(czy_jest_w_bazie)
        if czy_jest_w_bazie[0] == 0:
            # print('uzytkownik nie znajduje sie w bazie')
            query_dodawanie_czytelnika = f"INSERT INTO czytelnicy(imie_nazwisko,ksiazka) VALUES('{czytelnik}','{tytul_do_sql}')"
            cursor.execute(query_dodawanie_czytelnika)
            query_wyswietl_calosc_czytelnicy = f"select * from czytelnicy"
            cursor.execute(query_wyswietl_calosc_czytelnicy)
            calosc_czytelnicy = cursor.fetchall()
            # print(f"calosc czytelnicy: {calosc_czytelnicy}")
            query_zwiekszanie_liczby_ksiazek = f"UPDATE czytelnicy SET liczba_ksiazek = liczba_ksiazek +1 WHERE imie_nazwisko = '{czytelnik}'"
            cursor.execute(query_zwiekszanie_liczby_ksiazek)
            #usunac z listy ksiazek
            query = f"DELETE FROM ksiazki WHERE tytul IN (select tytul from ksiazki where tytul='{tytul_do_sql}'  LIMIT 1)"
            # query=f"DELETE FROM ksiazki WHERE tytul='{tytul_do_sql}'"
            cursor.execute(query)
            output.append('True')
            # print('True')
        else:
            # trzeba teraz sprawdzic ile ten czytelnik ma ksiazek wypozyczonych ogolnie i ile tej konkretnej
            # query_sprawdzenie_liczby_ksiazek =
            query_liczba_ksiazek_ogolem = f"select count(liczba_ksiazek) from czytelnicy where imie_nazwisko='{czytelnik}'"
            cursor.execute(query_liczba_ksiazek_ogolem)
            liczba_ksiazek = cursor.fetchone()[0]
            # print(f"liczba_ksiazek = {liczba_ksiazek}")

            query_liczba_konkretnej_ksiazki_ogolem = f"select count(ksiazka) from czytelnicy where imie_nazwisko='{czytelnik}'and ksiazka='{tytul_do_sql}'"
            cursor.execute(query_liczba_konkretnej_ksiazki_ogolem)
            liczba_konkretnej_ksiazki = cursor.fetchone()[0]
            # print(f"liczba_konkretnej_ksiazki = {liczba_konkretnej_ksiazki}")

            query_czy_ksiazka_dostepna = f"select count(tytul) from ksiazki where tytul='{tytul_do_sql}'"
            cursor.execute(query_czy_ksiazka_dostepna)
            czy_ksiazka_dostepna = cursor.fetchone()[0]
            # print(f"czy ksiazka dostepna {tytul_do_sql}: {czy_ksiazka_dostepna}")

            # wyswietl_czytelnikow()
            # print('wypozycz tytul do sql: '+tytul_do_sql)
            limit_ksiazek = 3
            if liczba_ksiazek > limit_ksiazek:
                output.append('False')
                # print('False')

            elif liczba_konkretnej_ksiazki > 0:
                output.append('False')
                # print("False")

            else:
                query = f"DELETE FROM ksiazki WHERE tytul IN (select tytul from ksiazki where tytul='{tytul_do_sql}'  LIMIT 1)"
                # query=f"DELETE FROM ksiazki WHERE tytul='{tytul_do_sql}'"
                cursor.execute(query)
                query2 = f"INSERT INTO czytelnicy(imie_nazwisko,ksiazka) VALUES('{czytelnik}','{tytul_do_sql}')"
                cursor.execute(query2)
                output.append('True')
                # print('True')
    else:
        output.append('False')
        # print("False")


def oddaj(podany_input):
    egzemplarz = podany_input
    czytelnik, tytul_do_sql = egzemplarz
    query_czytelnik_posiada_taka_ksiazke = f"select count(ksiazka) from czytelnicy where imie_nazwisko='{czytelnik}' and ksiazka='{tytul_do_sql}'"
    cursor.execute(query_czytelnik_posiada_taka_ksiazke)
    czy_czytelnik_posiada_taka_ksiazke = cursor.fetchone()[0]
    query_czy_ksiazka_dostepna1 = f"select count(tytul) from ksiazki where tytul='{tytul_do_sql}'"
    cursor.execute(query_czy_ksiazka_dostepna1)
    czy_ksiazka_dostepna1 = cursor.fetchone()[0]
    #print(f"stan ksiazki  {tytul_do_sql}: {czy_ksiazka_dostepna1}")
    # print(f"czy czytelnik posiada taka ksiazke{czytelnik}: {tytul_do_sql}: {czy_czytelnik_posiada_taka_ksiazke}")
    if czy_czytelnik_posiada_taka_ksiazke > 0:
        query3 = f"INSERT INTO ksiazki(tytul) VALUES('{tytul_do_sql}')"
        cursor.execute(query3)
        query4 = f"DELETE FROM czytelnicy WHERE imie_nazwisko='{czytelnik}' and ksiazka='{tytul_do_sql}'"
        cursor.execute(query4)
        output.append('True')
        # print('True')
    else:
        output.append('False')
        # print('False')


if __name__ == "__main__":
    sqlite_con = sqlite3.connect(":memory:")
    cursor = sqlite_con.cursor()
    cursor.execute('''CREATE TABLE ksiazki (tytul data_type STRING, 
                          autor data_type STRING,  
                          rok data_type INTEGER
                          );''')
    cursor.execute('''CREATE TABLE czytelnicy (imie_nazwisko data_type STRING, 
                          ksiazka data_type STRING,
                          liczba_ksiazek INT UNSIGNED DEFAULT 0)
                          ;''')

    wybor_funkcji()

    query_count = f"select tytul, autor, count(tytul) from ksiazki group by tytul order by tytul"
    cursor.execute(query_count)
    result_count = cursor.fetchall()

    # for row in result_count:
    #     print(row)
    # #print('koniec funkcji dodaj -----------------------------------------')
    #
    # #wybor_funkcji()
    #
    # query_count2= f"select tytul, autor, count(tytul) from ksiazki group by tytul order by tytul"
    # cursor.execute(query_count2)
    # result_count2 = cursor.fetchall()
    # for row in result_count2:
    #     print(row)
    # def wyswietl_czytelnikow():
    #     query_wyswietl_czytelnikow = f"select * from czytelnicy"
    #     cursor.execute(query_wyswietl_czytelnikow)
    #     print("CZTELNICY: ")
    #     print(cursor.fetchall())
    #
    # wyswietl_czytelnikow()
    for x in output:
        print(x)





