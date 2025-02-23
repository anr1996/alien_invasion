class User:
    def __init__(self, first_name, last_name, **user_info):
        self.full_name = first_name + " " + last_name
        self.user_info = user_info
        self.login_attempts = 0
        
    def describe_user(self):
    
        print(f"Name: {self.full_name.title()}")
        
        if self.user_info:
            for user, info in self.user_info.items():
                print(f"{user}: {info}")
        else:
            print("No additional information available")
    
    def greet_user(self):
        print(f"Welcome to Python {self.full_name.title()}")
        
    def incr_login(self):
        self.login_attempts += 1
    
    def reset_login(self):
        self.login_attempts = 0
        
    def get_login(self):
        return self.login_attempts
        
        

    
    