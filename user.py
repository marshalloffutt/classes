# 9-3

class User():
    
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    def describe_user(self):
        print("\n" + self.first_name.title() + " " + self.last_name.title() + " is a " +
        str(self.age) + " year old " + self.profession + ".")

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + ".")

larry = User("Larry", "Whizbang", 54, "construction worker")
gary = User("Gary", "Granderson", 68, "accountant")
barry = User("Barry", "Berringer", 45, "baseball player")
jerry = User("Jerry", "Johnson", 34, "programmer")

larry.describe_user()
larry.greet_user()

gary.describe_user()
gary.greet_user()

barry.describe_user()
barry.greet_user()

jerry.describe_user()
jerry.greet_user()