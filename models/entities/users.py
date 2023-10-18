from werkzeug.security import check_password_hash,generate_password_hash
class Users():
    def __init__(self, iduser, username, password, name=None):
        self.iduser = iduser
        self.username = username
        self.password = password
        self.name = name
    
    @classmethod
    def check_password(self,hased_password, password):
        return check_password_hash(hased_password,password)
    
    # has=(generate_password_hash('Devel0pment!'))
    # print(has)
