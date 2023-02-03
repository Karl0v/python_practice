class Customer:

    def __init__(self, name: str, account: int):
        self.name = name
        self.account = account


    def __str__(self):
        return f'{self.name} in the account {self.account}'

    def buy(self):
        money = 0
