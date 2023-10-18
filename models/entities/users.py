# from  flask_bcrypt import generate_password_hash, check_password_hash
class Users():
    def __init__(self, iduser, username, password, name=None):
        self.iduser = iduser
        self.username = username
        self.password = password
        self.name = name
    
    # @classmethod
    # def check_password(cls,hased_password, password):
    #     return check_password_hash(hased_password,password)
    
    # @classmethod
    # def generate_pwd(cls,password):        
    #     return generate_password_hash(password).decode('utf-8')
    
    # haspwd=check_password_hash('$2b$12$trejbleRXa1JxilFVEWGvulmaKdAe9Ksnj5YpqtOWNPiNgxH9Gb96','Devel0pment!')
    # print(haspwd)
    # print(generate_password_hash('Devel0pment!'))
