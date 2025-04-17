from models.user_model import User
from database.db_sqlalchemy import db


class UserQueries:

    def get_all(self):
        return User.query.all()

    def get_by_id(self, user_id: int):
        return User.query.get(user_id)

    def create_user(self, new_user: User) -> User:
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update_user(self, user_id: int, data: dict) -> User:
        user = User.query.filter_by(id=user_id).update(data)
        db.session.commit()
        return user

    def delete_user(self, user: User) -> User:
        db.session.delete(user)
        db.session.commit()
        return user
