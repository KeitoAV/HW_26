import json
import logging

from json import JSONDecodeError


class PostManager:
    def __init__(self, path):
        try:
            with open(path, 'r', encoding='utf8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            logging.info("Ошибка доступа к файлу")
        except JSONDecodeError:
            logging.info("Файл не удается преобразовать")

    def get_all(self):
        """Загрузка данных из файлов json"""
        return self.data

    def get_posts_by_user(self, user_name):
        """Возвращает посты определенного пользователя"""

        if type(user_name) != str:
            raise TypeError("'user_name' не является 'str'")

        posts_by_user = []
        poster_names = self.data
        for name in poster_names:
            if user_name.lower() in name["poster_name"].lower():
                posts_by_user.append(name)
        return posts_by_user

    def search_for_posts(self, query):
        """Возвращает список постов по ключевому слову"""

        if type(query) != str:
            raise TypeError("'query' не является 'str'")

        search_by_query = []
        all_posts = self.data
        for post in all_posts:
            if query.lower() in post["content"].lower():
                search_by_query.append(post)
        return search_by_query

    def get_post_by_pk(self, post_pk):
        """Возвращает один пост по его идентификатору"""

        if type(post_pk) != int:
            raise TypeError("'post_pk' не является 'int'")

        all_posts = self.data
        for post in all_posts:
            if post["pk"] == post_pk:
                return post

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста"""

        all_comments = self.data
        comments = []
        for comment in all_comments:
            if comment["post_id"] == post_id:
                comments.append(comment)
        return comments
