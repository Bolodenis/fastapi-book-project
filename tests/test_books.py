# tests/test_books.py
from tests import client

API_PREFIX = "/api/v1"  # Adjust this to match your settings

def test_get_all_books():
    response = client.get(f"{API_PREFIX}/books/")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_single_book():
    response = client.get(f"{API_PREFIX}/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"

def test_create_book():
    new_book = {
        "id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": "Fantasy",
    }
    response = client.post(f"{API_PREFIX}/books/", json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 4
    assert data["title"] == "Harry Potter and the Sorcerer's Stone"

def test_update_book():
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put(f"{API_PREFIX}/books/1", json=updated_book)
    assert response.status_code == 200
    data = response.json()
    data = response.json()
    assert data["title"] == "The Hobbit: An Unexpected Journey"

def test_delete_book():
    response = client.delete(f"{API_PREFIX}/books/3")
    assert response.status_code == 204

    response = client.get(f"{API_PREFIX}/books/3")
    assert response.status_code == 404                                                                                                                                                      