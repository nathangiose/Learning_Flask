import os


class Config(object):
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or b'\xd3\xc6\xdc\xa7\xf9\xec\xb9\x81\xf2\x17\x8d\xc9\xf9V\xe5\xb6'

#    py -c "import os; print(os.urandom(16))"
#    the above mentioned is created to generate a random password

    # Optional to add in for Thapelo  ", 'host': 'mongodb://localhost:27017/UTA_Enrollment'"
    MONGODB_SETTINGS = {'db': 'UTA_Enrollment'}
