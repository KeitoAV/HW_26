class TestMain:
    def test_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код"""
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"

    def test_root_content(self, test_client):
        """ Проверяем, получается ли нужный контент страницы"""
        response = test_client.get('/', follow_redirects=True)
        assert "SKYPROGRAM" in response.data.decode("utf-8"), "Контент страницы неверный"

    def test_search_content(self, test_client):
        """ Проверяем, получается ли нужный контент страницы"""
        response = test_client.get('/search', follow_redirects=True)
        assert "search" in response.data.decode("utf-8"), "Контент страницы неверный"
