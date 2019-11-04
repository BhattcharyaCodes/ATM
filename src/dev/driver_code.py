from customer import Customer
from atm_impl import *

from src.dev.atm_impl import session_auth


def next_transaction():
    ans = str(input("Do you want to continue? Y/N "))
    if ans is 'Y':
        choices(cust)
    else:
        print("Bye,bye baby!")


"""
Bank is more of a part where the driver code to the whole atm resides.
The flow starts off with the:
1 Customer Creation
2 Atm transactions the customer wants to conduct
"""

if __name__ == '__main__':

    msg = "Initiating Customer Creation"
    bor = '*'
    border = bor * len(msg)
    print("{}\n{}\n{}".format(border, msg, border))

    name = str(input("Enter you first and last name separated by a space:"))
    # pin = str(input("Enter you PIN:"))
    cust = Customer(name)
    print("Customer created is:")
    cust.print_customer_info()
    print("Pretend to swipe your card up here, at the ATM to initiate ATM transaction")
    pin = str(input("\nEnter your 4 digit PIN\t"))
    print(pin)
    print(cust.pin)
    result = session_auth(pin)
    # pdb.set_trace()

    if result is True:
        choices(cust)
        next_transaction()
    else:
        print("Bad PIN, end of the road for you")
