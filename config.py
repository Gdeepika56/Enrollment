import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "'\xd4z\xc6P\xceUC\xae\xdd\xb2\x8f!N,\x83\x11'"

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment',
                        'host' : 'mongodb://localhost:27017/UTA_Enrollment'
    }


