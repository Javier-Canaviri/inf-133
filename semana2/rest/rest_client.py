import requests
url ="http://localhost:8000/"
# get consulta a la ruta /lista_estudiantes
ruta_get =url+"lista_estudiantes"
get_response= requests.request(method="GET", url=ruta_get)
print(get_response.text)
print("--------------------------")

#POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post=url+"agrega_estudiante"
nuevo_estudiante={
    "nombre":"Pablo",
    "apellido":"Cordero",
    "carrera":"Ingenieria Agronomica",
    
}
post_response=requests.request(method="POST",
                               url=ruta_post,
                               json=nuevo_estudiante)
print(post_response.text)

ruta_estudiantes_con_p = url + "estudiantes_con_p"
estudiantes_con_p=requests.request(method="GET",url=ruta_estudiantes_con_p)
print("NOMBRES CON P:")
print (estudiantes_con_p.text)

ruta_conteo_carrera=url+"conteo_carreras"
conteo_carreras=requests.request(method="GET",url=ruta_conteo_carrera)
print("CONTEO DE CARRERAS:")
print(conteo_carreras.text)

ruta_total_estudiantes=url+"total_estudiantes"
total_estudiantes=requests.request(method="GET", url=ruta_total_estudiantes)
print("EL NUMERO DE ESTUDIANTES REGISTRADOS: ")
print(total_estudiantes.text)