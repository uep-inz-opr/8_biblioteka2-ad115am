import sqlite3

if __name__ == "__main__":

    sqlite_con = sqlite3.connect(":memory:")
    cursor = sqlite_con.cursor()
    cursor.execute('''CREATE TABLE ksiazki (tytul data_type STRING, 
                          autor data_type STRING,  
                          rok data_type INTEGER
                          );''')
def wybor_funkcji():
    ilosc = int(input())
    for row in range(ilosc):
        egz = input('bez tego nie zadziala xd: ')
        wejscie_tupla = eval(egz)
        funkcja = wejscie_tupla[0]
        print(wejscie_tupla[0])
        if funkcja==" dodaj ":
            print('wybrano funkcje dodaj')
            dodaj(wejscie_tupla[1:])
        if funkcja==" wypozycz ":
            print('wybrano funkcje wypozycz')
            wypozycz(wejscie_tupla[1:])



class Ksiazka():
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

    ilosc = 0

#liczba_ksiazek = int(input())

def dodaj(podany_input):
        #podany_input = podany_input
        egzemplarz = podany_input
        #tupla = eval(egzemplarz)
        #lista_ksiazek.append(Ksiazka(tupla[0],tupla[1]))
        #a,b,c = tupla[1:] #sprawdzic to czy dziala
        tytul_do_sql,autor_do_sql,rok_do_sql = egzemplarz
        # tytul_do_sql = tupla[0]
        # autor_do_sql = tupla[1]
        # rok_do_sql = tupla[2]
        query = f"INSERT INTO ksiazki(tytul,autor,rok) VALUES('{tytul_do_sql}','{autor_do_sql}',{rok_do_sql})"
        cursor.execute(query)

def wypozycz(podany_input):
    egzemplarz = podany_input
    czytelnik, tytul_do_sql= egzemplarz
    print('wypozycz tytul do sql: '+tytul_do_sql)
    #query = f"DELETE FROM ksiazki WHERE tytul IN (select tytul from ksiazki where tytul='{tytul_do_sql}'  LIMIT 1)"
    query=f"DELETE FROM ksiazki WHERE tytul='{tytul_do_sql}'"
    cursor.execute(query)

wybor_funkcji()

query_count = f"select tytul, autor, count(tytul) from ksiazki group by tytul order by tytul"
cursor.execute(query_count)
result_count = cursor.fetchall()

for row in result_count:
    print(row)
print('koniec funkcji dodaj -----------------------------------------')

wybor_funkcji()

query_count2= f"select tytul, autor, count(tytul) from ksiazki group by tytul order by tytul"
cursor.execute(query_count2)
result_count2 = cursor.fetchall()
for row in result_count2:
    print(row)





