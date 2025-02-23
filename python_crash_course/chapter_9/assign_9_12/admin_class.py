from user_classes import User


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can flag content"]
        

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
     
       

class Admin(User):
    def __init__(self, first_name, last_name, **user__info):
        super().__init__(first_name, last_name, **user__info)

    privileges = Privileges()
    
    
