from .db import db


class Product(db.Document):
    """
    class to define product schema
    """
    name = db.StringField(required=True)
    brand_name = db.StringField(required=True)
    regular_price_value = db.DecimalField(required=True)
    offer_price_value = db.DecimalField()
    currency = db.StringField(required=True)
    classification_l1 = db.StringField()
    classification_l2 = db.StringField()
    classification_l3 = db.StringField()
    classification_l4 = db.StringField()
    image_url = db.StringField(required=True)

