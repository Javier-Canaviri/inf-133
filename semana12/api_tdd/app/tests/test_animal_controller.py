def test_get_animals(test_client, auth_headers2):
    response = test_client.get("/api/animals", headers=auth_headers2)
    assert response.status_code == 200
    assert response.json == []


def test_create_animal(test_client, auth_headers2):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    response = test_client.post("/api/animals", json=data, headers=auth_headers2)
    assert response.status_code == 403


def test_get_animal(test_client, auth_headers2, auth_headers):
    # Primero crea un animal
    data = {"name": "Tiger", "species": "Panthera tigris", "age": 3}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora obtén el animal
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers2)
    assert response.status_code == 200
    assert response.json["name"] == "Tiger"


def test_update_animal(test_client, auth_headers2, auth_headers):
    # Primero crea un animal
    data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora actualiza el animal
    update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
    response = test_client.put(
        f"/api/animals/{animal_id}", json=update_data, headers=auth_headers2
    )
    assert response.status_code == 403


def test_delete_animal(test_client, auth_headers2,auth_headers):
    # Primero crea un animal
    data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora elimina el animal
    response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers2)
    assert response.status_code == 403

    # Verifica que el animal ha sido eliminado
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers2)
    assert response.status_code == 200