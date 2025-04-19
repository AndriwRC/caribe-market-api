from database.db_sqlalchemy import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2))
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
