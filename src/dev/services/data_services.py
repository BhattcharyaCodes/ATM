#write the implementation of mongodb , data query etc.


#We'll put our data access code and logic here.
from typing import List, Optional

import datetime

from src.dev.data.customer import Customer


def create_bank_account(fname: str, lname: str, account_type: str) -> Customer:
    customer = Customer()
    customer.name = name
    customer.cust_ids =
    customer.account_type =
    customer.account_no =
    customer.card_no =
    customer.balance =
    customer.pin =
    customer.cust_fname =
    customer.cust_lname =

    customer.save()

    return customer


#
# def find_account_by_email(email: str) -> Customer:
#     customer = Customer.objects(email=email).first()
#     return customer

