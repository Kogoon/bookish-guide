import os

#BASE_DIR = os.path.dirname(__file__)

DB_USER_NAME='admin'
DB_USER_PASSWD='1q2w3e4r!'
DB_HOST='testdb.cdfnd5ogvaqo.ap-northeast-2.rds.amazonaws.com'
DB_NAME='flaskapp'

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://testdb.cdfnd5ogvaqo.ap-northeast-2.rds.amazonaws.com'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}?charset=utf8'.format(DB_USER_NAME, DB_USER_PASSWD, DB_HOST, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
