import requests
url = "http://localhost:8000"

response = requests.get(f"{url}/posts")

print(response.text)

print("------------------11111111111111111------------------------")
response2 = requests.get(f"{url}/post/2")
print(response2.text)

print("--------------------222222222222222----------------------")
ruta_post = url + "/posts"
nuevo_post = {
        "title": "Mi experiencia como dev",
        "content": "tatatata experiencia como dev.",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_post)
print(post_response.text)

print("-------------------3333333333333333-----------------------")
ruta_ac = url + "/post/3"

actualizar_post = {
        "content": "En progreso.",
}
post_response = requests.put(url=ruta_ac, json=actualizar_post)
print(post_response.text)

print("------------------44444444444444444------------------------")


response = requests.get(f"{url}/posts")

print(response.text)