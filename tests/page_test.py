def test_main_menu_links(client):
    response =client.get('/')
    assert response.status_code == 200
