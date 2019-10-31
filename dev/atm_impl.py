from customer import Customer
from bank import next_transaction
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

def withdrawal(cust):
    withdraw = float(input("How much do you want to withdraw = "))
    if cust.balance > withdraw > 0:
        cust.balance = cust.balance - withdraw
        print("Balance withdrawn:{} current balance now is {}".format(withdraw, cust.balance))
    elif withdraw < 0:
        print("Invalid Amount Entered.")
    else:
        print("Withdrawal not allowed. Not enough balance")


def check_balance(cust):
    # use arr to store the customer_id
    print("balance = {}".format(cust.balance))
    return


def transfer_funds():
    print("You are here to transfer funds")


def deposit(cust):
    print("initial balance: {}".format(cust.balance))
    deposit_amt = float(input("Enter the cash amount to be deposited\t"))
    if deposit_amt > 0:
        cust.balance += deposit_amt
        print("Your new account balance is:{}".format(cust.balance))
    else:
        print("Invalid amount")


def choices(cust):
    transaction = ["Check Balance", "Withdrawals", "Transfer", "Deposit"]
    choice = str(input("Choose/Type an input string from the following menu: \n 1. Check Balance \n "
                       "2. Withdrawals \n 3. Transfer Funds \n 4. Deposit\n"))

    print(choice)
    if choice in transaction:
        if choice is "Check Balance":
            check_balance()
            next_transaction()

        elif choice == "Withdrawals":
            withdrawal()
            next_transaction()

        elif choice == "Transfer Funds":
            transfer_funds()
            next_transaction()

        elif choice == "Deposit":
            deposit(cust)
            next_transaction()
    else:
        print("Invalid Choice is entered,\t that's not the end of road though!"
              " Retry using correct spell and casing\n")

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
