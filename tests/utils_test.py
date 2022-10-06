from config import DATA_PATH, COMMENTS_PATH
from utils import PostManager
import pytest


keys_should_be = {
    "content", "likes_count", "pic", "pk",
    "poster_avatar", "poster_name", "views_count"
}

keys_should_be_comment = {
    "post_id", "commenter_name", "comment", "pk",
}


class TestPosts:
    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostManager(DATA_PATH)
        return post_dao_instance

    @pytest.fixture
    def comment_dao(self):
        comment_dao_instance = PostManager(COMMENTS_PATH)
        return comment_dao_instance

    def test_posts_all(self, post_dao):
        """Проверяем все посты"""
        posts = post_dao.get_all()
        assert type(posts) == list, "Возвращается не list"
        assert type(posts[0]) == dict, "Возвращается не dict"
        assert set(posts[0]) == keys_should_be, "Неверный список ключей"

    def test_post_by_pk(self, post_dao):
        """Проверяем возвращаются ли посты по 'pk'"""
        search_post = post_dao.get_post_by_pk(1)
        assert type(search_post) == dict, "Возвращается не dict"
        assert set(search_post) == keys_should_be, "Неверный список ключей"
        assert search_post['poster_name'] == 'leo', 'Не совпадает имя'
        assert search_post['pk'] == 1, "Неверный 'pk'"
        posts = post_dao.get_post_by_pk(777)
        assert posts is None, "Возвращает None, если нет поста"
        with pytest.raises(TypeError):
            search_post = search_post('1'), "'post_pk' не является 'int'"

    def test_search_for_posts(self, post_dao):
        """Проверяем возвращаются ли посты по ключевому слову"""
        search_posts = post_dao.search_for_posts('тарелка')
        assert type(search_posts) == list, "Возвращается не list"
        assert type(search_posts[0]) == dict, "Возвращается не dict"
        assert set(search_posts[0]) == keys_should_be, "Неверный список ключей"
        assert 'тарелка' in search_posts[0]['content'].lower(), "Некорректный результат поиска для 'тарелка'"
        posts = post_dao.search_for_posts("111111")
        assert posts == [], "Возвращается пустой список, если нет 'query' в контенте"
        with pytest.raises(TypeError):
            search_posts = search_posts(1), "'query' не является 'str'"

    def test_posts_by_user(self, post_dao):
        """Проверяем возвращаются ли посты определенного пользователя"""
        leo_posts = post_dao.get_posts_by_user('leo')
        assert type(leo_posts) == list, "Возвращается не list"
        assert type(leo_posts[0]) == dict, "Возвращается не dict"
        assert leo_posts[0]['poster_name'] == 'leo', 'Не совпадает имя'
        hank2_posts = post_dao.get_posts_by_user('hank2')
        assert len(hank2_posts) == 0, " Такого пользователя нет"
        with pytest.raises(TypeError):
            leo_posts = leo_posts(1), "'user_name' не является 'str'"

    def test_comments_by_post(self, comment_dao):
        """Проверяем возвращаются ли комментарии к посту """
        comments = comment_dao.get_comments_by_post_id(1)
        assert type(comments) == list, "Возвращается не list"
        assert type(comments[0]) == dict, "Возвращается не dict"
        assert comments[0]['commenter_name'].lower() == 'hanna', "Пользователь c таким именем не оставлял комментариев"
        assert comments[0]['comment'].lower() == 'очень здорово!', "Нет такого комментария"
        assert set(comments[0]) == keys_should_be_comment, "Неверный список ключей"
