from flask_session import Session


def make_config(Database):

    backend = Database.get('backend')
    driver = Database.get('driver')
    host = Database.get('host')
    port = Database.get('port')
    name = Database.get('name')
    user = Database.get('user')
    password = Database.get('password')

    return '{}+{}://{}:{}@{}:{}/{}'.format(backend, driver, user, password, host, port, name)

class Config():
    Develop = False
    Testing = False
    Product = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False




class Develop(Config):
    Develop = True

    Database = {
        'backend': 'mysql',
        'driver': 'pymysql',
        'host': 'localhost',
        'port': 3306,
        'name': 'flask66',
        'user': 'root',
        'password': 'love',

    }

    SQLALCHEMY_DATABASE_URI = make_config(Database)

envs = {
    'develop': Develop
}