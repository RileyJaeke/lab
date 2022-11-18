class Account:
    """
    A class representing details for an Account object.
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of a person object.
        :param name: Person's first name.
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount) -> bool:
        """
        Method to deposit money into the person's account.
        :param amount: Amount of money going into the person's account.
        :return: Boolean determining if the transaction was successful.
        """
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdrawal(self, amount) -> bool:
        """
        Method to withdrawal money from the person's account.
        :param amount: Amount of money withdrawn from the person's account
        :return: Boolean determining if the transaction was successful.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Method to return person's balance
        :return: Account Balance
        """
        return self.account_balance

    def get_name(self) -> str:
        """
        Method to get the name of the person.
        :return: First Name.
        """
        return self.account_name
