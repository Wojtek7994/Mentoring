import unittest


class User:
    def __init__(self, user_id, first_name, last_name, balance):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def __str__(self):
        return f"ID: {self.user_id}, Imię: {self.first_name}, Nazwisko: {self.last_name}, Saldo: {self.balance} "

    def add_balance(self, amount):
        self.balance += amount
        print(
            f"Dodano {amount}  do salda użytkownika {self.first_name} {self.last_name}. Nowe saldo: {self.balance} ")

    def subtract_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(
                f"Odjęto {amount} z salda użytkownika {self.first_name} {self.last_name}. Nowe saldo: {self.balance} ")
        else:
            print(
                f"Brak wystarczających środków na koncie użytkownika {self.first_name} {self.last_name}. Aktualne saldo: {self.balance} ")


def main():
    users = [
        User(1, "Jan", "Kowalski", 1000.0),
        User(2, "Anna", "Nowak", 1500.0),
        User(3, "Piotr", "Wiśniewski", 1200.0),
        User(4, "Maria", "Wójcik", 800.0),
        User(5, "Krzysztof", "Kowalczyk", 500.0)
    ]

    while True:
        print("Lista użytkowników:")
        for user in users:
            print(user)

        print("Co chcesz zrobić?")
        print("1. Dodaj środki do salda")
        print("2. Odejmij środki z salda")
        print("3. Zakończ")

        choice = input("Wybierz opcję (1/2/3): ")

        if choice == '3':
            break

        user_id = int(input("Podaj ID użytkownika: "))
        amount = float(input("Podaj kwotę: "))

        user = next((u for u in users if u.user_id == user_id), None)

        if user:
            if choice == '1':
                user.add_balance(amount)
            elif choice == '2':
                user.subtract_balance(amount)
            else:
                print("Nieprawidłowa opcja.")
        else:
            print("Nie znaleziono użytkownika o podanym ID.")

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Jan", "Kowalski", 1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.user.balance, 1000.0)

    def test_add_balance(self):
        self.user.add_balance(2500.0)
        self.assertEqual(self.user.balance, 3500.0)

    def test_subtract_balance(self):
        self.user.subtract_balance(200.0)
        self.assertEqual(self.user.balance, 800.0)

    def test_subtract_balance_insufficient_funds(self):
        self.user.subtract_balance(38893.0)
        self.assertEqual(self.user.balance, 1000.0)

    def test_str_method(self):
        expected_str = "ID: 1, Imię: Jan, Nazwisko: Kowalski, Saldo: 1000.0 "
        self.assertEqual(str(self.user), expected_str)

if __name__ == '__main__':
    unittest.main()


