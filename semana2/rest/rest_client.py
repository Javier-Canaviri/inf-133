import requests
url ="http://localhost:8000/"
# get consulta a la ruta /lista_estudiantes
ruta_get =url+"lista_estudiantes"
get_response= requests.request(method="GET", url=ruta_get)
print(get_response.text)

#POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post=url+"agrega_estudiante"
nuevo_estudiante={
    "nombre":"Juanito",
    "apellido":"Perez",
    "carrera":"Ingenieria Agronomica",
    
}
post_response=requests.request(method="POST",
                               url=ruta_post,
                               json=nuevo_estudiante)
print(post_response.text)


ruta_nomP=url+"buscar_nombre"
nombres_con_P=requests.request(method="GET",url=ruta_nomP)
print("NOMBRES CON P:")
print (nombres_con_P.text)
