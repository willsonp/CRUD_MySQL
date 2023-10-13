from werkzeug.security import generate_password_hash, check_password_hash
class User():
    def __init__(self, iduser, name, user_name, user_password):
        self.iduser = iduser
        self.name = name
        self.user_name = user_name
        self.user_password = user_password
    
    @classmethod
    def check_password(self,hased_password, user_password):
        return check_password_hash(self.user_password,hased_password)
    
    # has=(generate_password_hash('Devel0pment!'))
    # print(has)
