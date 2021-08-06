import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    # Optional to add in for Thapelo  ", 'host': 'mongodb://localhost:27017/UTA_Enrollment'"
    MONGODB_SETTINGS = {'db': 'UTA_Enrollment'}
