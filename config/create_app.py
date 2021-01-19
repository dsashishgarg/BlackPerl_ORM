from flask import Flask, jsonify
from flask_restplus import Api


def create_app(env=None):
    from app.product.routes import register_routes

    app = Flask(__name__)
    app.config['PROPAGATE_EXCEPTIONS'] = True

    api = Api(app, title="BlackPerl")

    register_routes(api, app)

    return app
