class Lowbalance(Exception):
    pass

class Amount(object):
    def __init__(self, initialvalue=0):
        self.balance = initialvalue

    def spend_cash(self, amount):
        if self.balance < amount:
            raise Lowbalance(f'{amount}')
        self.balance -= amount

    def add_cah(self,amount):
        self.balance += amount


def add(x,y):
    return (x+y)
