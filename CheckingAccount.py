class checkingaccount(object):
    def __init__(self, name, account_number, address, initial_amount):
        self._name = name
        self._no = account_number
        self._add = address
        self._balance = initial_amount

    def deposit(self, amount):
        amount=float(input("Enter amount to be Deposited: "))
        self._balance += amount
        print("\n You deposited:", amount)

    def withdraw(self, amount):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self._balance>=amount:
            self._balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient account balance  ")

    def get_balance(self):
        return self._balance

    def report(self):
        print("\n CardHolder Name=",self._name)
        print("\n CardHolder Account No=",self._no)
        print("\n CardHolder Address=",self._add)
        print("\n Net Available Balance=",self._balance)
        

##Driver Code##
  
a1 = checkingaccount('Sandeep Dwivedi', '787878787', '201 STL drive', 20000)

a1.deposit(1000)
a1.withdraw(20)
a1.report()
