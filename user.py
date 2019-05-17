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