
class Privileges:
    def __init__(self, add_post, del_post, ban_user, suspend_user):

        self.add_post = add_post
        self.del_post = del_post
        self.ban_user = ban_user
        self.suspend_user = suspend_user


    def admin_abilities(self):
        admin_privileges = print(f"administers have the following capablities: {self.add_post} {self.del_post} {self.ban_user} {self.suspend_user}")
        return admin_privileges

current_admin = Privileges("'adding posts'", "'deleting posts'", "'banning users'", "'suspending users'")
current_admin.admin_abilities()
        
