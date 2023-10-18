# from  flask_bcrypt import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
class Users(UserMixin):
    def __init__(self, id, username, password, name=None):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
    
    @classmethod
    def check_password(cls,hased_password, password):
        return check_password_hash(hased_password,password)
    
    @classmethod
    def generate_pwd(cls,password):        
        return generate_password_hash(password).decode('utf-8')
    
    # Esto genera un string de 102 carácteres
    # haspwd=generate_password_hash('Devel0pment!').encode('utf-8')
    # print(haspwd)
    # print(len(haspwd))
    # print(generate_password_hash('Devel0pment!'))
