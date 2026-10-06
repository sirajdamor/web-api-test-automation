import pytest

pytestmark = pytest.mark.api

TIMEOUT = 15


@pytest.mark.smoke
def test_get_single_post(session, base_url):
    r = session.get(f"{base_url}/posts/1", timeout=TIMEOUT)
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert set(body.keys()) == {"userId", "id", "title", "body"}


@pytest.mark.regression
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_returns_requested_id(session, base_url, post_id):
    r = session.get(f"{base_url}/posts/{post_id}", timeout=TIMEOUT)
    assert r.status_code == 200
    assert r.json()["id"] == post_id


@pytest.mark.regression
def test_list_all_posts(session, base_url):
    r = session.get(f"{base_url}/posts", timeout=TIMEOUT)
    assert r.status_code == 200
    assert len(r.json()) == 100


@pytest.mark.regression
def test_filter_posts_by_user(session, base_url):
    r = session.get(f"{base_url}/posts", params={"userId": 1}, timeout=TIMEOUT)
    assert r.status_code == 200
    posts = r.json()
    assert len(posts) == 10
    assert all(p["userId"] == 1 for p in posts)


@pytest.mark.regression
def test_response_is_json(session, base_url):
    r = session.get(f"{base_url}/posts/1", timeout=TIMEOUT)
    assert "application/json" in r.headers["Content-Type"]


@pytest.mark.smoke
def test_create_post(session, base_url):
    payload = {"title": "My test post", "body": "Created by automation", "userId": 1}
    r = session.post(f"{base_url}/posts", json=payload, timeout=TIMEOUT)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == payload["title"]
    assert "id" in body


@pytest.mark.regression
def test_update_post_with_put(session, base_url):
    payload = {"id": 1, "title": "Updated title", "body": "Updated body", "userId": 1}
    r = session.put(f"{base_url}/posts/1", json=payload, timeout=TIMEOUT)
    assert r.status_code == 200
    assert r.json()["title"] == "Updated title"


@pytest.mark.regression
def test_update_post_with_patch(session, base_url):
    r = session.patch(f"{base_url}/posts/1", json={"title": "Patched"}, timeout=TIMEOUT)
    assert r.status_code == 200
    assert r.json()["title"] == "Patched"


@pytest.mark.regression
def test_delete_post(session, base_url):
    r = session.delete(f"{base_url}/posts/1", timeout=TIMEOUT)
    assert r.status_code == 200


@pytest.mark.regression
def test_post_not_found(session, base_url):
    r = session.get(f"{base_url}/posts/99999", timeout=TIMEOUT)
    assert r.status_code == 404


@pytest.mark.regression
def test_comments_of_a_post(session, base_url):
    r = session.get(f"{base_url}/posts/1/comments", timeout=TIMEOUT)
    assert r.status_code == 200
    comments = r.json()
    assert len(comments) > 0
    assert all("@" in c["email"] for c in comments)


@pytest.mark.regression
def test_get_user(session, base_url):
    r = session.get(f"{base_url}/users/1", timeout=TIMEOUT)
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert "email" in body
