# from customer import *
#   import pdb

def session_auth(pin):
    # pin = str(input("\nEnter your 4 digit PIN\t"))
    atm_pin = "0000"
    if pin == atm_pin:
        return True
    else:
        return False


# class AtmImpl():
#     def __init__(self):
#         #self.balance = 2000

# 2nd implementation

def withdrawal(self):
    withdraw = float(input("How much do you want to withdraw = "))
    if self.balance > withdraw > 0:
        self.balance = self.balance - withdraw
        print("Balance withdrawn:{} current balance now is {}".format(withdraw, self.balance))
    elif withdraw < 0:
        print("Invalid Amount Entered.")
    else:
        print("Withdrawal not allowed. Not enough balance")


def check_balance(self):
    # use arr to store the customer_id
    print("balance = {}".format(self.balance))
    return


def transfer_funds(self):
    print("You are here to transfer funds")


def deposit(self):
    print("initial balance: {}".format(self.balance))
    deposit_amt = float(input("Enter the cash amount to be deposited\t"))
    if deposit_amt > 0:
        self.balance += deposit_amt
        print("Your new account balance is:{}".format(self.balance))
    else:
        print("Invalid amount")


def choice(self):
    choice = str(input("Choose/Type an input string from the following menu: \n 1. Check Balance \n "
                       "2. Withdrawals \n 3. Transfer Funds \n 4. Deposit\n"))
    print(choice)
    if choice == "Check Balance":
        self.checkbalance()
        self.next_transaction()

    elif choice == "Withdrawals":
        self.withdrawal()
        self.next_transaction()

    elif choice == "Transfer Funds":
        self.transfer_funds()
        self.next_transaction()

    elif choice == "Deposit":
        self.deposit()
        self.next_transaction()
    else:
        print("Invalid Choice is entered,\t that's not the end of road though!"
              " Retry using correct spell and casing\n")


def next_transaction(self):
    ans = str(input("Do you want to continue? Y/N"))
    if ans is 'Y':
        self.choice()
    else:
        print("Bye,bye baby!")

# if __name__ == "__main__":
#     impl = AtmImpl()
#     impl.balance = 2000
#     transaction = ["Check Balance", "Withdrawals", "Transfer", "Deposit"]
#     print("Pretend to swipe your card up here")
#     result = impl.session_auth()
#     # pdb.set_trace()
#     if result is True:
#         impl.choice()
#         impl.next_transaction()
#     else:
#         print("Bad PIN, end of the road for you")
