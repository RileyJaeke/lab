from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('John')
        self.p2 = Account('Jane')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == 'John'
        assert self.p2.get_name() == 'Jane'

    def test_deposit(self):
        self.p1.deposit(100)
        assert self.p1.get_balance() == 100
        self.p2.deposit(-100)
        assert self.p2.get_balance() == 0

    def test_withdrawal(self):
        self.p1.deposit(100)
        self.p1.withdrawal(90)
        assert self.p1.get_balance() == 10
        self.p2.withdrawal(-100)
        assert self.p2.get_balance() == 0
        self.p2.deposit(10)
        self.p2.withdrawal(20)
        assert self.p2.get_balance() == 10
