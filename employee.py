import requests

class Employee:
    """A simple employee class"""

    raise_amt = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@gmail.com".format(str(self.first_name).lower(), str(self.last_name).lower())

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last_name}/{month}')
        if response.ok:
            return response.text
        else:
            return "Bad Response"