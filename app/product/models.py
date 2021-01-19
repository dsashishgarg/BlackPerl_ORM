from app.product.schema import ProductSchema
import sqlite3


class ProductModel:
    TABLE_NAME = 'products'

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def json(self):
        return {'product_name': self.product_name, 'product_price': self.product_price}

    @classmethod
    def find_by_id(cls, product_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE product_id=?".format(
            table=cls.TABLE_NAME)
        result = cursor.execute(query, (product_id,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'product': {'product_id': row[0], 'product_name': row[1], 'product_price': row[2]}}
        return {'message': "product not found"}

    def get(self, product_id):
        product = self.find_by_id(product_id)
        if product:
            return product
        return {'message': 'product not found'}, 404

    @classmethod
    def delete(cls, product_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE product_id=?".format(
            table=cls.TABLE_NAME)
        cursor.execute(query, (product_id,))

        connection.commit()
        connection.close()

        return {'message': 'Product deleted'}

    @classmethod
    def getall(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=cls.TABLE_NAME)
        result = cursor.execute(query)
        products = []
        for row in result:
            products.append(
                {'product_id': row[0], 'product_name': row[1], 'product_price': row[2]})
        connection.close()
        return {'products': products}
