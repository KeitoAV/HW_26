import json


class TestApi:
    def test_api_posts(self, test_client):
        """ Проверяем возвращается ли список и есть ли у элементов нужные ключи """

        response = test_client.get('/api/posts')
        response = json.loads(response.get_data(as_text=True))
        assert isinstance(response, list)
        assert list(response[0].keys()) == [
            "content", "likes_count", "pic", "pk",
            "poster_avatar", "poster_name", "views_count"
        ]

    def test_api_post_by_id(self, test_client):
        """ Проверяем возвращается ли словарь запрошенного id и есть ли у элементов нужные ключи """
        response = test_client.get('api/posts/1')
        response = json.loads(response.get_data(as_text=True))
        assert isinstance(response, dict)
        assert list(response) == [
            "content", "likes_count", "pic", "pk",
            "poster_avatar", "poster_name", "views_count"
        ]
