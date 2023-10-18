from .entities.users import Users
class ModelUser():
    
    @classmethod
    def login(self,db,user):
        try:
          # Open connection to MySQL DB
            cursor = db.cursor()
            cursor.execute('SELECT id,username,password,name FROM users WHERE username = %s', (user.username,))
            row = cursor.fetchone()
            cursor.close()
            if row != None:
                user = Users(row[0],row[1],Users.check_password(row[2],user.password),row[3])
                # print(user)
                return user
            else:
                return None
        except Exception as e:
            print(e)
            raise Exception(e)

    @classmethod
    def get_id(self,db,id):
        try:
        # Open connection to MySQL DB
            cursor = db.cursor()
            cursor.execute('SELECT id,username,password,name FROM users WHERE id = %s', (id,))
            row = cursor.fetchone()
            cursor.close()
            if row != None:
                user = Users(row[0],row[1],row[2],row[3])
                # print(user)
                return user
            else:
                return None
        except Exception as e:
            print(e)
            raise Exception(e)
