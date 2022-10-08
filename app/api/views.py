import logging
from config import LOGS_PATH
from config import DATA_PATH
from datetime import datetime
from flask import Blueprint, jsonify

from db import db
from utils import PostManager

blueprint = Blueprint('api', __name__, url_prefix='/api')

# logging.basicConfig(filename=LOGS_PATH, level=logging.INFO, encoding='utf8')


@blueprint.route('/posts')
def get_all_posts():
    """Обрабатывает запрос GET /api/posts и возвращает полный список постов в виде JSON-списка"""

    logging.info(f"{datetime.now()} /api/posts")

    posts = PostManager(DATA_PATH)
    all_posts = posts.get_all()

    return jsonify(all_posts)


@blueprint.route('/posts/<int:post_id>')
def get_post_by_id(post_id):
    """Обрабатывает запрос GET /api/posts/<post_id> и возвращает один пост в виде JSON-словаря"""

    logging.info(f"{datetime.now()} /api/posts/{post_id}")

    posts = PostManager(DATA_PATH)
    post = posts.get_post_by_pk(post_id)
    if post:
        return jsonify(post)
    return 'Пост с данным id отсутствует в БД'


@blueprint.route('/test_db/')
def test_db():
    result = db.session.execute(
        'SELECT 1'
    ).scalar()

    return jsonify(
        {
            'result': result,
        }
    )