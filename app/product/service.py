from flask.json import jsonify
from app.product.schema import ProductSchema
from marshmallow.fields import String

from typing import List
from .models import ProductModel


class ProductService:

    @staticmethod
    def create(new_product: ProductSchema) -> ProductModel:
        ProductModel.insert(new_product)
        return new_product

    @staticmethod
    def get_all() -> List[ProductModel]:
        return jsonify(ProductModel.getall())

    @staticmethod
    def get_by_id(product_id: int) -> ProductModel:
        return jsonify(ProductModel.find_by_id(product_id))

    @staticmethod
    def delete_by_id(product_id: int) -> List[int]:
        return (ProductModel.delete(product_id))
