from database.db_sqlalchemy import db


class Store(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.Text)
    address = db.Column(db.String(50))
    website = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
