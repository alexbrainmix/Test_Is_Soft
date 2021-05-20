import json
from crud import group

def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail":"Not Found"}


def test_create_group(client, monkeypatch):
    json_request={"name": "Python"}
    json__response={"id": 1, "name": "Python"}

    async def monkey_post(id):
        return 1

    monkeypatch.setattr(group, "create", monkey_post)
    response = client.post("/group/", json.dumps(json_request))

    assert response.status_code == 201
    assert response.json() == json__response


def test_read_group(client, monkeypatch):
    json__response={"id": 1, "name": "Python"}
    
    async def monkey_get(id):
        return json__response

    monkeypatch.setattr(group, "get_by_id", monkey_get)
    response = client.get("/group/1")

    assert response.status_code == 200
    assert response.json() == json__response


def test_update_group(client, monkeypatch):
    json__response={"id": 1, "name": "Python"}
    
    async def monkey_get(id):
        return json__response

    monkeypatch.setattr(group, "get_by_id", monkey_get)

    async def monkey_put(id, obj):
        return 1

    monkeypatch.setattr(group, "update", monkey_put)
    response = client.put("/group/1/", json.dumps(json__response))

    assert response.status_code == 200
    assert response.json() == json__response


def test_delete_group(client, monkeypatch):
    json__response={"id": 1, "name": "Python"}

    async def monkey_get(id):
        return json__response
    monkeypatch.setattr(group, "get_by_id", monkey_get)

    async def monkey_delete(id):
        return id
    monkeypatch.setattr(group, "delete", monkey_delete)
    response = client.delete("/group/1/")

    assert response.status_code == 200
    assert response.json() == json__response