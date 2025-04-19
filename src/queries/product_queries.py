from models.product_model import Product
from database.db_sqlalchemy import db


class ProductQueries:

    def get_all(self):
        return Product.query.all()

    def get_by_id(self, product_id: int):
        return Product.query.get(product_id)

    def create_product(self, new_product: Product) -> Product:
        db.session.add(new_product)
        db.session.commit()
        return new_product

    def update_product(self, product_id: int, data: dict) -> None:
        Product.query.filter_by(id=product_id).update(data)
        db.session.commit()

    def delete_product(self, product: Product) -> Product:
        db.session.delete(product)
        db.session.commit()
        return product
