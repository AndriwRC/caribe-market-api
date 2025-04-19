from models.store_model import Store
from database.db_sqlalchemy import db


class StoreQueries:

    def get_all(self):
        return Store.query.all()

    def get_by_id(self, store_id: int):
        return Store.query.get(store_id)

    def create_store(self, new_store: Store) -> Store:
        db.session.add(new_store)
        db.session.commit()
        return new_store

    def update_store(self, store_id: int, data: dict) -> None:
        Store.query.filter_by(id=store_id).update(data)
        db.session.commit()

    def delete_store(self, store: Store) -> Store:
        db.session.delete(store)
        db.session.commit()
        return store
