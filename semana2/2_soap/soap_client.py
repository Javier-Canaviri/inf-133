from zeep import Client

client = Client('http://localhost:8000')

result = client.service.Saludar(nombre="Javier")
print(result)

suma = client.service.SumaDosNumeros(num1=6, num2=4)
print(suma)

cadena = client.service.CadenaPalindromo(cadena="Javier")
print(cadena)