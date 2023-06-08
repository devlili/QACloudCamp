from http import HTTPStatus

import requests

base_url = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    """Получение списка постов."""
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == HTTPStatus.OK, "Посты не получены"
    assert len(response.json()) > 0, "Посты не получены"


def test_get_posts_with_parameters():
    """Получение списка постов определенного пользователя."""
    params = {"userId": 1}
    response = requests.get(f"{base_url}/posts", params=params)
    assert response.status_code == HTTPStatus.OK, "Посты не получены"
    assert len(response.json()) > 0, "Посты не получены"
    for post in response.json():
        assert post["userId"] == 1, f"Пост '{post}' другого пользователя"


def test_get_single_post():
    """Получение одного поста."""
    post_id = 1
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == HTTPStatus.OK, "Пост не получен"
    assert response.json()["id"] == post_id, "Пост не получен"


def test_create_new_post():
    """Добавление нового поста."""
    data = {
        "title": "New Post",
        "body": "This is a new post",
        "userId": 1,
    }
    response = requests.post(f"{base_url}/posts", json=data)
    assert response.status_code == HTTPStatus.CREATED, "Пост не добавлен"
    assert response.json()["title"] == "New Post", "Пост не добавлен"


def test_create_new_post_with_empty_title():
    """Негативный тест на добавление поста с пустым параметрм title."""
    data = {"title": "", "body": "This is a new post", "userId": 1}
    response = requests.post(f"{base_url}/posts", json=data)
    assert (
        response.status_code != HTTPStatus.CREATED
    ), "Пост добавлен с пустым параметром title"
    assert (
        response.json()["title"] != ""
    ), "Пост добавлен с пустым параметром title"


def test_delete_post():
    """Удаление поста."""
    data = {
        "title": "Post to Delete",
        "body": "This is a new post",
        "userId": 1,
    }
    create_response = requests.post(f"{base_url}/posts", json=data)
    created_post_id = create_response.json()["id"]

    delete_response = requests.delete(f"{base_url}/posts/{created_post_id}")
    assert delete_response.status_code == HTTPStatus.OK, "Пост не удален"
    assert delete_response.json() == {}, "Пост не удален"

    get_response = requests.get(f"{base_url}/posts/{created_post_id}")
    assert get_response.status_code == HTTPStatus.NOT_FOUND, "Пост не удален"
