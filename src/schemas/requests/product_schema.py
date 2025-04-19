from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.product_model import Product, db


class ProductSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Product
        load_instance = True
        sqla_session = db.session
        include_fk = True
