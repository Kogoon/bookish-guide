import os

#BASE_DIR = os.path.dirname(__file__)

#DB_USER_NAME='brokurly'
DB_USER_NAME='admin'
#DB_USER_PASSWD='Kosa0401!'
DB_USER_PASSWD='1q2w3e4r!'
#DB_HOST='brokurlydatabase.cdfnd5ogvaqo.ap-northeast-2.rds.amazonaws.com'
DB_HOST='database-1.cdfnd5ogvaqo.ap-northeast-2.rds.amazonaws.com'
#DB_NAME='brokurlyapp'
DB_NAME='flaskapp'

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://testdb.cdfnd5ogvaqo.ap-northeast-2.rds.amazonaws.com'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}?charset=utf8'.format(DB_USER_NAME, DB_USER_PASSWD, DB_HOST, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# app config
class Config:
    ROOT_DIR = ROOT_DIR
    STATIC_DIR = '{0}/static'.format(ROOT_DIR)
    TEMPLATES_DIR = '{0}/templates'.format(ROOT_DIR)
    ERROR_CODE = {
        40000: 'Bad Request',
        41000: 'Gone',
        40300: 'Forbidden',
        40400: 'Not Found',
        50000: 'Internal Server Error',
    }