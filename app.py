import urllib.parse

from flask import Flask
from flask_restful import Api

from database.db import initialize_db
from resources.errors import errors
from resources.routes import initialize_routes

app = Flask(__name__)  # flask app
api = Api(app, errors=errors)  # rest api
username = urllib.parse.quote_plus('dbVishal')  # database server username
password = urllib.parse.quote_plus('yFlBhLiPVsnn0sDM')  # database server password

mongo_url = 'mongodb+srv://{0}:{1}@cluster0.b4a7f.mongodb.net/db_products?retryWrites=true&w=majority'.format(username,
                                                                                                              password)  # database server url

# configuration for db
app.config['MONGODB_SETTINGS'] = {
    'host': mongo_url
}

initialize_db(app)    # initializing database
initialize_routes(api)  # initializing api routes
app.run(host="0.0.0.0", port=5001)
