from database.db_sqlalchemy import db


class Phone(db.Model):
    __tablename__ = "phones"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(15), unique=True, nullable=False)
    country_code = db.Column(db.String(5))
    has_whatsapp = db.Column(db.Boolean, default=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
