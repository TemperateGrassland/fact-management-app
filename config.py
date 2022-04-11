import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Secret key is used by extensions (i.e flask-wtf) to protect webforms against Cross-site request forgery.
    # This will need to be updated for security reasons before deploying to prod
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
