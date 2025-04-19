from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.phone_model import Phone, db


class PhoneSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Phone
        load_instance = True
        sqla_session = db.session
        include_fk = True
