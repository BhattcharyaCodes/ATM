class Customer:
    def __init__(self, cust_name, pin=None):
        # print("enter account")
        self.cust_ids = []
        for i in range(1000, 9999):
            self.cust_ids.append(i+1)
            if cust_name is None:
                self.cust_name = "John Doe{}".format(i+1)
            else:
                self.cust_name = cust_name
        self.account_type = ["savings", "salaried"]
        self.account_no = 6003450348983409
        self.card_no = 123412341234
        self.balance = 2000
        self.pin = "0000"
        # if pin is None:
        #     self.pin = "0000"
        # else:
        #     self.pin = pin

    def print_customer_info(self):
        print("Customer Name: {} \nCustomer Id: {} \nCustomer A/c no.: {} \nAccount Balance: {}"
              " \n".format(self.cust_name, self.cust_ids[0], self.account_no, self.balance))


if __name__ == '__main__':

    msg = "Initiating Customer Creation"
    bor = '*'
    border = bor * len(msg)

    print("{}\n{}\n{}".format(border, msg, border))

    name = str(input("Enter you first and last name separated by a space:"))

    cust = Customer(name)
    print("Customer created is:")
    cust.print_customer_info()