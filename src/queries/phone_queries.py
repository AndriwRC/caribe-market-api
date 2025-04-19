from models.phone_model import Phone
from database.db_sqlalchemy import db


class PhoneQueries:

    def get_all(self):
        return Phone.query.all()

    def get_by_id(self, phone_id: int):
        return Phone.query.get(phone_id)

    def create_phone(self, new_phone: Phone) -> Phone:
        db.session.add(new_phone)
        db.session.commit()
        return new_phone

    def update_phone(self, phone_id: int, data: dict) -> None:
        Phone.query.filter_by(id=phone_id).update(data)
        db.session.commit()

    def delete_phone(self, phone: Phone) -> Phone:
        db.session.delete(phone)
        db.session.commit()
        return phone
