import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_post():
    data = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", data=data)
    assert response.status_code == 201
    assert response.json()["title"] == data["title"]

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json() == {}
