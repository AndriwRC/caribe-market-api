from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.user_model import User, db


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
