import mongoengine


class Bank(mongoengine.Document):


     account_type


     customer = list()