from models.entities import User

class ModelUser():
    
    @classmethod
    def login(self,db,user):
        try:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM users WHERE username = %s', (User.username))
            row = cursor.fetchone()
            cursor.close()
            if row:
                user = User(row[0],row[1],row[2],User.check_password(row[3],User.password))
                print(user)
                return user
            else:
                return False
        except Exception as e:
            print(e)
            raise Exception(e)
