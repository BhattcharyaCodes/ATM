# class Bank():
#
#     # def __init__(self):
#     #     print("Bank Constructor")
#
#     def new_customer_creation(self):
#         # print("call the customer object")
#         msg = "Initiating Customer Creation"
#         bor = '*'
#         border = bor * len(msg)
#         print("{}\n{}\n{}".format(border, msg, border))
#
#         name = str(input("Enter you first and last name separated by a space:"))
#         # pin = str(input("Enter you PIN:"))
#         cust = Customer(name)
#         print("Customer created is:")
#         cust.print_customer_info()

# from atm.dev.customer import Customer
from customer import Customer
from atm_impl import *

"""
Bank is more of a part where the driver code to the whole atm resides.
The flow starts off with the:
1 Customer Creation
2 Atm transactions the customer wants to conduct
"""
if __name__ == '__main__':
    # bank = Bank()
    # bank.new_customer_creation()

    msg = "Initiating Customer Creation"
    bor = '*'
    border = bor * len(msg)
    print("{}\n{}\n{}".format(border, msg, border))

    name = str(input("Enter you first and last name separated by a space:"))
    # pin = str(input("Enter you PIN:"))
    cust = Customer(name)
    print("Customer created is:")
    cust.print_customer_info()
    impl = AtmImpl()
    transaction = ["Check Balance", "Withdrawals", "Transfer", "Deposit"]
    print("Pretend to swipe your card up here, at the ATM to initiate ATM transaction")
    pin = str(input("\nEnter your 4 digit PIN\t"))

    result = session_auth(pin)
    # pdb.set_trace()
    if result is True:
        impl.choice()
        impl.next_transaction()
    else:
        print("Bad PIN, end of the road for you")