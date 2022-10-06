class TestPosts:
    def test_single_id_status(self, test_client):
        """ Проверяем, получается ли при запросе по 'id' нужный статус-код """
        response = test_client.get('/posts/5', follow_redirects=True)
        assert response.status_code == 200, "Статус код по 'id' неверный"

    def test_single_name_status(self, test_client):
        """ Проверяем, получается ли при запросе по 'user_name' нужный статус-код """
        response = test_client.get('/users/leo', follow_redirects=True)
        assert response.status_code == 200, "Статус код по 'user_name' неверный"

    def test_search_content(self, test_client):
        """ Проверяем, получается ли нужный контент страницы"""
        response = test_client.get('/posts/5', follow_redirects=True)
        assert "post" in response.data.decode("utf-8"), "Контент страницы неверный"
