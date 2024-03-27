import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

# GET /tacos
response = requests.get(url)
print(response.json())


print("----------------------------POST-------------------------------")
# POST /taco 
mi_taco = {
    "base": "tortilla",
    "guiso": "de carne",
    "toppings": ["cebolla", "Queso"],
    "salsa": "completo",

}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

print("----------------------------GET-------------------------------")
# GET /tacos
response = requests.get(url)
print(response.json())

print("------------------------------PUT-----------------------------")
# PUT /tacos/1
edit_pizza = {
    "base": "tortilla",
    "guiso": "vegano",
    "toppings": ["palta", "Queso"],
    "salsa": "mayonesa",
}
response = requests.put(url+ "/1", json=edit_pizza, headers=headers)
print(response.json())

print("----------------------------GET-------------------------------")
# GET /tacos
response = requests.get(url)
print(response.json())

print("---------------------------DELETE--------------------------------")
# DELETE /tacos/1

response = requests.delete(url + "/1")
print(response.json())

print("------------------------------GET-----------------------------")
# GET /tacos
response = requests.get(url)
print(response.json())
print("-----------------------------------------------------------")
