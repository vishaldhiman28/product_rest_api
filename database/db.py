from flask_mongoengine import MongoEngine

db = MongoEngine()  # mongoengine initialize


def initialize_db(app):
    """
    function to connect flask app to the database
    """
    db.init_app(app)
