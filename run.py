import os

from flask import Flask, jsonify

from app.api.views import blueprint as api_blueprint
from app.main.views import blueprint as main_blueprint
from app.posts.views import blueprint as post_blueprint
from db import db

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}'
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(api_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(post_blueprint)

    db.init_app(app)

    return app


app = create_app()


@app.errorhandler(404)
def page_not_found(e):
    return 'Страница не найдена :('


@app.errorhandler(500)
def server_error(e):
    return 'Ведутся технические работы...'


if __name__ == "__main__":
    app.run(port=25000)
