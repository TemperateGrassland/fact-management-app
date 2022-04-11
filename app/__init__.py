from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#the __name__ variable is a python predefined variable. It is set to the name
#of the module in which it is used.
app = Flask(__name__)

# Read the app's config file
app.config.from_object(Config)

# Import db
db = SQLAlchemy(app)
# import database migration engine in case changes are made to the data structure storing facts
migrate = Migrate(app, db)

#Putting the import statement at the bottom avoids circular imports between
# app and routes
from app import routes, models
