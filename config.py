class Config():
    SECRET_KEY='Devel0pment!'

class DevConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='Devel0pment!'
    MYSQL_DB='products'
    MYSQL_PORT=3306    

config = {
    'development': DevConfig
} 