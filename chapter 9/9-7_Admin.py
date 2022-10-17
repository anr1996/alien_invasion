class User:
    # defining init function and adding multiple attributes
    def __init__(self, first_name, last_name, email, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.password = password
        self.login_attempts = 10

    # defining function f_name for first name
    def f_name(self):
        print(f"enter your first name.\n {self.first_name}. ")

    # defining function l_name for last name
    def l_name(self):
        print(f"enter your last name. \n {self.last_name}.")
    
    # defining function profile_email for email
    def profile_email(self):
        print(f"enter your email. \n{self.email}.")
    
    # defining function profile_user for username
    def profile_user(self):
        print(f"please create a username.\n {self.user_name}.")

    # defining function profile_pass for password
    def profile_pass(self):
        print(f"please create a password.\n {self.password}.")

    # defining function attempted_logins for number of login attempts
    def attempted_logins(self):
        print(f"attempts to login in: {self.login_attempts}")
    
    # defining function attempted_login_increase for increase in the number of login attempts
    def attempted_login_increase(self, login_increase):
        self.login_attempts += login_increase

    # defining function login_attempts_reset for reseting the number of login attempts to 0
    def login_attempts_reset(self):
        self.login_attempts = 0

# assigning class User to variable my_profile.
my_profile = User('Adrian', 'Rich', 'anrich250@gmail.com', 'thok250zzz', 'forgot1996')


class Admin_user(User):

    

    def __init__(self, first_name, last_name, email, user_name, password):
        super().__init__(first_name, last_name, email, user_name, password)
        self.admin_privileges = ['Can add post', 'can delete post', 'can ban user', 'can suspend user']
    
    def admin_power(self):
        admin_options = print(f"The admin has the current options: {self.admin_privileges}")
        return admin_options


current_admin = Admin_user('adrian', 'rich', 'anrich250@gmail.com', 'thok250zzz', 'nintendo260')
current_admin.admin_power()
    
