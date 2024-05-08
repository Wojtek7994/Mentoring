from DataBase import DataBase


class Bank:
    print("Witamy w banku")
    print("Podaj imie i nazwisko")
    imie = input("Imię ")
    nazwisko = input("Nazwisko ")
    print("Witaj " + imie + " " + nazwisko)
    NumerUsera = input("Podaj swoje Id")
    print("Twój numer ID  to " + NumerUsera)
def get_user1():
    return get_user1()


user1 =DataBase(1,"Jan","Kowalski",3000)
user2 =DataBase(2,"Barbara","Nowak",5000)
user3 =DataBase(3,"Dawid","Podsiadło",2000)

print(user1.saldo,user2.saldo,user3.saldo)
user1.dodaj_saldo(3000)
user2.dodaj_saldo(123)
print(user1.saldo,user2.saldo,user3.saldo)































