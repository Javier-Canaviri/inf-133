import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

ruta_actualizar = url + "estudiantes/1"
estudiante_actualizado = {
    "nombre": "Juan",
    "apellido": "Fernandez",
    "carrera": "Ingeniería civil",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=estudiante_actualizado
)
print(put_response.text)

print("----------------------------------")

# GET filtrando por nombre con query params
ruta_get = url + "estudiantes?nombre=Juan"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)