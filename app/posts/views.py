import logging
from config import DATA_PATH, COMMENTS_PATH
from flask import Blueprint, render_template, request
from utils import PostManager

blueprint = Blueprint('post', __name__)


@blueprint.route('/posts/<int:post_id>')
def page_post(post_id):
    """Страница одного поста, теги"""
    logging.info('Страница одного поста запрошена')

    posts = PostManager(DATA_PATH)
    post = posts.get_post_by_pk(post_id)

    new_content = ''
    for word in post['content'].split():
        if '#' in word:
            word = f'<a href="/searching_posts?my_tag={word[1:]}" class="item__tag">{word}</a>'
        new_content += word + ' '
    post['content'] = new_content

    comments = PostManager(COMMENTS_PATH)
    all_comments = comments.get_comments_by_post_id(post_id)

    return render_template('post.html', post=post, all_comments=all_comments)


@blueprint.route('/search')
def search():
    """Страница поиска"""
    logging.info('Страница поиска запрошена')

    return render_template('search.html')


@blueprint.route('/searching_posts')
def searching():
    """Список постов по ключевому слову, теги"""

    logging.info('Страница постов по "query" запрошена')

    posts = PostManager(DATA_PATH)

    if 'my_tag' in request.args:
        query = request.args['my_tag']
        tag = '#' + query
        posts = posts.search_for_posts(tag)

        comments = PostManager(COMMENTS_PATH)
        all_comments = {post['pk']: len(comments.get_comments_by_post_id(post['pk'])) for post in posts}

        return render_template('tag.html', posts=posts, tag=tag, all_comments=all_comments)
    else:
        query = request.args['my_form']
        posts = posts.search_for_posts(query)

        comments = PostManager(COMMENTS_PATH)
        all_comments = {post['pk']: len(comments.get_comments_by_post_id(post['pk'])) for post in posts}

    return render_template('search.html', posts=posts, all_comments=all_comments)


@blueprint.route('/users/<user_name>')
def page_username(user_name):
    """Вывод постов конкретного пользователя"""

    logging.info('Страница постов одного пользователя запрошена')

    posts = PostManager(DATA_PATH)
    page_user = posts.get_posts_by_user(user_name)

    comments = PostManager(COMMENTS_PATH)
    all_comments = {post['pk']: len(comments.get_comments_by_post_id(post['pk'])) for post in page_user}

    return render_template('user-feed.html', user=page_user, all_comments=all_comments)
