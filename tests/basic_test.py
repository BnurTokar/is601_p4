def test_request_main_menu_links(client):
    response =client.get('/')
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data