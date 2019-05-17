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