from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.store_model import Store, db


class StoreSchema(SQLAlchemyAutoSchema):
    website = fields.Url()

    class Meta:
        model = Store
        load_instance = True
        sqla_session = db.session
