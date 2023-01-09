from fs_api import app # Flask instance of the API
import json

def test_index_route():
    response = app.test_client().get('/directory')

    assert response.status_code == 200
    res = json.loads(response.data.decode('utf-8'))
    print(response.data.decode('utf-8'), res)
    assert 'directory' in res

def test_post_directory():
    response = app.test_client().post('/directory', json={
        "name": "test",
        "maxElNumber": 4
    })
    print('responce', response.data)
    assert response.data != None