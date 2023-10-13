class Config():
    SECRET_KEY='2*D!e3v7el0pm*ent!'

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