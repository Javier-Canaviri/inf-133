def test_get_libro(test_client, auth_headers2):
    response = test_client.get("/api/libros", headers=auth_headers2)
    assert response.status_code == 200
    assert response.json == []


def test_create_libro(test_client, auth_headers2):
    data = {"titulo": "Lion", "autor": "Panthera leo","edicion":2, "disponibilidad": True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers2)
    assert response.status_code == 403


def test_get_libro(test_client, auth_headers2, auth_headers):
    # Primero crea un libro
    data = {"titulo": "Lion", "autor": "Panthera leo","edicion":2, "disponibilidad": True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    # Ahora obtén el libro
    response = test_client.get(f"/api/libros/{libro_id}", headers=auth_headers2)
    assert response.status_code == 200
    assert response.json["titulo"] == "Tiger"


def test_update_libro(test_client, auth_headers2, auth_headers):
    # Primero crea un libro
    data = {"titulo": "Lion", "autor": "Panthera leo","edicion":2, "disponibilidad": True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    # Ahora actualiza el libro
    update_data = {"titulo": "Tiger", "autor": "Panthera ","edicion":3, "disponibilidad": True}
    response = test_client.put(
        f"/api/libros/{libro_id}", json=update_data, headers=auth_headers2
    )
    assert response.status_code == 403


def test_delete_libro(test_client, auth_headers2,auth_headers):
    # Primero crea un libro
    data = {"titulo": "Lion", "autor": "Panthera leo","edicion":2, "disponibilidad": True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    # Ahora elimina el libro
    response = test_client.delete(f"/api/libros/{libro_id}", headers=auth_headers2)
    assert response.status_code == 403

    # Verifica que el libro ha sido eliminado
    response = test_client.get(f"/api/libros/{libro_id}", headers=auth_headers2)
    assert response.status_code == 200