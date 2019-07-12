from random import randint

class Accounts:

    def __init__(self):
        #Dictionary to store all accounts information
        #structure => data[acc_number] = [name,balance]
        self.data = {}

    #Function to create a new account
    def create(self,name,initial_deposit):
        self.acc_number = randint(10000,99999)
        while True:
            if self.acc_number in self.data.values():
                self.acc_number = randint(10000,99999)
            else:
                break
        self.data[self.acc_number]=[name,initial_deposit]
        print("\nAccount Created. Your Account Number is {}" .format(self.acc_number))

    #To aunthenticate if the account exists
    def verify(self,name,acc_number):
        if acc_number in self.data.keys():
            if name in self.data[acc_number]:
                print("Account Authenticated.")
                return True
            else:
                print("\nAccount Authentication Failed.")
                return False
        else:
            print("\nAccount Authentication Failed.")
            return False

    #To deposit and update balance
    def deposit(self,amount):
        self.data[self.acc_number][1] = self.data[self.acc_number][1] + amount
        self.display()

    #To withdraw and update balance
    def withdraw(self,amount):
        if amount > self.data[self.acc_number][1]:
            print("Insufficient Funds")
        else:
            self.data[self.acc_number][1] = self.data[self.acc_number][1] - amount
        self.display()

    #To display Balance    
    def display(self):
        print("\nAccount Balance: {}" .format(self.data[self.acc_number][1]))

acc = Accounts()


while True:
    print("\n")
    print("1. Create New Savings Account.")
    print("2. Access Existing Account.")
    print("3. Exit.")
    option = int(input("Select option: "))

    if option is 1:
        name = input("Enter your name: ")
        initial_deposit = int(input("Enter your initial deposit: "))
        acc.create(name,initial_deposit)

    elif option is 2:
        name = input("Enter your name: ")
        acc_number = int(input("Enter your 5 digit Account number: "))
        print("\n")
        if acc.verify(name,acc_number) is True:
            while True:
                print("\n")
                print("1. Make a Deposit.")
                print("2. Make a Withdrawal .")
                print("3. Display Balance")
                print("4. Go back to previous menu.")
                op = int(input("Select option: "))
                if op is 1:
                    amount = int(input("Enter amount: "))
                    acc.deposit(amount)
                elif op is 2:
                    amount = int(input("Enter amount: "))
                    acc.withdraw(amount)
                elif op is 3:
                    acc.display()

                elif op is 4:
                    break

                else:
                    print("Select Correct Option.")

    elif option is 3:
        quit()

    else:
        print("Select correct option.")
