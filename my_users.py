from user import User
from admin import Admin

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