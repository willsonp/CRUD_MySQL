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

config = {
    'development': DevConfig
} 