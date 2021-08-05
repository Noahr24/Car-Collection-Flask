import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Sets Congiguration variables for our flask app
    """
    SECRET_KEY= "You will never guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
