from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.user_model import User, db


class UserSchema(SQLAlchemyAutoSchema):
    email = fields.Email(required=True)

    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
