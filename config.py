import MySQLdb


class Config():
    SECRET_KEY='tMUHQ$1rvpUg5Lh'
    WTF_CSRF_SECRET_KEY='tMUHQ$1rvpUg5Lh'
    PORT=5000

class DevConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='Devel0pment!'
    MYSQL_DB='puntoventa_python'
    MYSQL_PORT=3306   


class Get_Connection(Config):
    def get_connection():
        try:
            return MySQLdb.connect(host=DevConfig.MYSQL_HOST,user=DevConfig.MYSQL_USER,password=DevConfig.MYSQL_PASSWORD,db=DevConfig.MYSQL_DB,port=DevConfig.MYSQL_PORT)       
        except Exception as e:
            print(e)
        return None
    
config = {
    'development': DevConfig,
    'conexion': Get_Connection
} 