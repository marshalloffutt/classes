from user import User
from privilege import Privilege

class Admin(User):
    def __init__(self, first_name, last_name, age, profession):
        super().__init__(first_name, last_name, age,  profession)
        self.privileges = Privilege()