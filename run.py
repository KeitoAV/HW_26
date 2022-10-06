
from flask import Flask

from app.api.views import blueprint as api_blueprint
from app.main.views import blueprint as main_blueprint
from app.posts.views import blueprint as post_blueprint


def create_app():
    app = Flask(__name__)

    app.config['JSON_AS_ASCII'] = False

    app.register_blueprint(api_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(post_blueprint)
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
