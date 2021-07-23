# The Bank Api - Credit Card Verify
## Hecho Por
- Erick
- Carlos
- Balbino

## Estados de las tarjetas:
los estados manejados en las tarjetas pueden ser:
- Activa
- Robada
- Perdida
- Inactiva

## Codigos de respuesta:
- ` 00 -- #transaccion aprobada`
- ` 05 -- #Error de código`
- ` 07 -- #Error de fecha`
- ` 08 -- #Error de nombre`
- ` 14 -- #Error Numero tarjeta`
- ` 41 -- #Tarjeta esta perdida`
- ` 43 -- #Tarjeta es robada`
- ` 51 -- #Saldo insuficiente`
- ` 54 -- #Tarjeta esta inactiva`
- ` 61 -- #Excede el limite de la tarjeta`
- ` QY -- #Tipo de tarjeta es invalido`

## Endpoints y uso:

### Card Endpoint:
Este endpoint les ayudara a ver como esta esa tarjeta en el momento de la transaccion.  

```python
restapi     = "https://credit-card-auth-api-cerberus.herokuapp.com"
endpoint    = "/card/"
cardId      = "7000123456780000"

url = f"{restapi}{endpoint}{cardId}"

response = requests.get(url)
        print(response)
        dataJson = response.json()
        print(dataJson)
```
Respuesta:
```
<Response [200]>
{'id': 5, 'name': 'Erick Hernandez', 'number': '7000123456780000', 'date': '12/24', 'code': '$2b$14$Hzcnrg6n0fZPd9yRWQtZxufo6fMy7WHWbsxgVIcZZPOhIdkHrsbYO', 'salt': '$2b$14$Hzcnrg6n0fZPd9yRWQtZxu', 'balance': '40.50', 'limit': '1000.00', 'state': 'Activa'}
```

### Verify Endpoint:
Este endpoint les ayudara a verificar la transaccion con la tarjeta.  
Deben enviar los datos importantes de la tarjeta mas el balance que es el valor la transaccion.  

```python
restapi     = "https://credit-card-auth-api-cerberus.herokuapp.com"
endpoint    = "/verify"

url = f"{restapi}{endpoint}"

data = {
    "name": "Erick Hernandez",
    "number": "7000123456780000",
    "date": "12/24",
    "code": "182",
    "balance": 20.25 # el valor de la transaccion
}

response = requests.post(url, data=data)
print(response)
if response.status_code == 200:
    dataJson = response.json()
    if dataJson['response'] == '00':
        print(dataJson)
    else:
        print(dataJson)
```
Respuesta:
```
<Response [200]>
{'response': '00'}
```