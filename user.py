# 9-3, 9-5
class User():
    
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name.title() + " " + self.last_name.title() + " is a " +
        str(self.age) + " year old " + self.profession + ".")

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + ".")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("You have now tried to login " + str(self.login_attempts) + " times.")

    def reset_login_attempts(self):
        self.login_attempts = 0


# 9-7
class Admin(User):
    def __init__(self, first_name, last_name, age, profession):
        super().__init__(first_name, last_name, age,  profession)
        self.privileges = Privilege()
        

# 9-8
class Privilege():

    def __init__(self):
        self.privileges = [
            'can edit post', 
            'can delete post', 
            'can ban user',]

    def show_privileges(self):
        print("\nAs an admin, you can do the following:")
        for privilege in self.privileges:
            print("\t" + privilege)


# Instantiations
larry = User("Larry", "Whizbang", 54, "construction worker")
gary = User("Gary", "Granderson", 68, "accountant")
barry = User("Barry", "Berringer", 45, "baseball player")
jerry = User("Jerry", "Johnson", 34, "programmer")

harry = Admin("Harry", "Henderson", 35, "system administrator")
harry.privileges.show_privileges()

larry.describe_user()
larry.greet_user()

gary.describe_user()
gary.greet_user()

barry.describe_user()
barry.greet_user()

jerry.describe_user()
jerry.greet_user()
jerry.increment_login_attempts()
jerry.increment_login_attempts()
jerry.reset_login_attempts()

print ("Login attempts: " + str(jerry.login_attempts))