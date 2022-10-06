import logging
from flask import Blueprint, render_template
from utils import PostManager
from config import DATA_PATH, COMMENTS_PATH

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def page_index():
    """Главная страница"""

    logging.info('Главная страница запрошена')

    posts = PostManager(DATA_PATH)
    all_posts = posts.get_all()

    comments = PostManager(COMMENTS_PATH)
    all_comments = {post['pk']: len(comments.get_comments_by_post_id(post['pk'])) for post in all_posts}

    return render_template('index.html', all_posts=all_posts, all_comments=all_comments)
