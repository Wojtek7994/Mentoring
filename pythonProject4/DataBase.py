class DataBase:

    def __init__(self,id, imie, nazwisko, saldo ):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = saldo

    def dodaj_saldo(self, saldo_poczatkowe):
        self.saldo = self.saldo+saldo_poczatkowe
        return self.saldo


user1 =DataBase(1,"Jan","Kowalski",3000)
user2 =DataBase(2,"Barbara","Nowak",5000)
user3 =DataBase(3,"Dawid","Podsiadło",2000)

print(user1.saldo,user2.saldo,user3.saldo)
user1.dodaj_saldo(3000)
user2.dodaj_saldo(123)
print(user1.saldo,user2.saldo,user3.saldo)
