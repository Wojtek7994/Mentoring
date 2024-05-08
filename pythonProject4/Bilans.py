class Bilasns():

    def __init__(self,bilans):
        self.bilans = bilans
    print("podaj co chcesz zrobić na koncie")
    def get_user1(self, saldo, zwiekszyc:int=10, zmnniejszyc:int=32):
        saldo = saldo + zwiekszyc
        saldo  = saldo - zmnniejszyc
        saldo = input("Czy chcesz zwiększyć czy zmniejszyć saldo ?")
        return None

    get_user1(103)