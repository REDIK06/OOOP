class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def _merge_balances(self, other_balance):
        self._balance += other_balance


my_account = Bank("User1", 100)
your_account = Bank("User2", 100)

my_account._merge_balances(your_account._balance)
print(f"Мой счет: {my_account._balance}, Ваш счет: {your_account._balance}")