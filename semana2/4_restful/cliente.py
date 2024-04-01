import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
print("-----------------------------------------------")
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)
print("-----------------------------------------------")

# DELETE elimina todos los estudiantes por la ruta /estudiantes
ruta_eliminar = url + "estudiantes"
eliminar_response = requests.request(method="DELETE", 
                                    url=ruta_eliminar)
print(eliminar_response.text)
print("-----------------------------------------------")

# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingenieria Agronomica"
}

post_response = requests.request(method="POST", 
                        url=ruta_post,
                        json=nuevo_estudiante)
print(post_response.text)
print("-----------------------------------------------")

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingenieria de sistemas",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)
print("-----------------------------------------------")

# GET busca a un estudiante por id /estudiantes/{id}
ruta_filtrar_nombre = url + "estudiantes/1"
filtrar_nombre_response = requests.request(method="GET", 
                                url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)
print("-----------------------------------------------")

# PUT actualiza un estudiante por la ruta /estudiantes
ruta_actualizar = url + "estudiantes"
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=estudiante_actualizado
)
print(put_response.text)
print("-----------------------------------------------")

#Agrega una ruta para mostrar todas las carreras
print("1 Agrega una ruta para mostrar todas las carreras")

ruta_carreras = url + "carreras"

carreras = requests.get(ruta_carreras)
print(carreras.text)
print("-----------------------------------------------")

print("2 Agrega una ruta que devuelva a todos los estudiantes de la carrera de Economia")

ruta_estEconomia = url + "economistas"
estEconomia = requests.get(ruta_estEconomia)
print(estEconomia.text)
print("-----------------------------------------------")

print("3 Agrega a dos estudiantes de economia")
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Javier",
    "apellido": "Canaviri",
    "carrera": "Economia"
}

post_response = requests.request(method="POST", 
                        url=ruta_post,
                        json=nuevo_estudiante)

ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Carlos",
    "apellido": "Huaranca",
    "carrera": "Economia"
}

post_response = requests.request(method="POST", 
                        url=ruta_post,
                        json=nuevo_estudiante)
print("todos los estudiantes \n",post_response.text)
print("-----------------------------------------------")
ruta_estEconomia = url + "economistas"
estEconomia = requests.get(ruta_estEconomia)
print("Los de economia:  \n",estEconomia.text)

