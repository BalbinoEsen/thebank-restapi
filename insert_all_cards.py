import requests
from tqdm import tqdm
from time import sleep

endpoint = "/insert"

env = {
    "prod": "http://credit-card-auth-api-cerberus.herokuapp.com",
    "dev": "http://localhost:12345"
}

url = f"{env['dev']}{endpoint}"

cardList = [
    {
        "name": "Erick Hernandez",
        "number": "7000123456780000",
        "date": "12/24",
        "code": "182",
        "balance": 0.00,
        "limit": 1000.00,
        "state": "Activa"
    },
    {
        "name": "test01",
        "number": "7000123456780001",
        "date": "12/24",
        "code": "181",
        "balance": 1000.00,
        "limit": 1000.00,
        "state": "Activa"
    },
    {
        "name": "test02",
        "number": "7000123456780002",
        "date": "12/24",
        "code": "182",
        "balance": 1000.00,
        "limit": 1000.00,
        "state": "Robada"
    },
    {
        "name": "test03",
        "number": "7000123456780003",
        "date": "12/24",
        "code": "183",
        "balance": 1000.00,
        "limit": 1000.00,
        "state": "Perdida"
    },
    {
        "name": "test04",
        "number": "7000123456780004",
        "date": "12/24",
        "code": "184",
        "balance": 1000.00,
        "limit": 1000.00,
        "state": "Inactiva"
    },
    {
        "name": "test05",
        "number": "7000123456780005",
        "date": "12/24",
        "code": "185",
        "balance": 0.00,
        "limit": 1000.00,
        "state": "Activa"
    },
    {
        "name": "test06",
        "number": "7000123456780006",
        "date": "12/24",
        "code": "186",
        "balance": 500.00,
        "limit": 1000.00,
        "state": "Activa"
    },
    {
        "name": "test06",
        "number": "7000123456780006",
        "date": "12/24",
        "code": "186",
        "balance": 500.00,
        "limit": 1000.00,
        "state": "Activa"
    },
    {
        "name": "test07",
        "number": "7000123456780007",
        "date": "12/24",
        "code": "187",
        "balance": 1500.00,
        "limit": 3000.00,
        "state": "Activa"
    },
]

for card in tqdm(cardList):
    sleep(0.25)
    response = requests.put(url, data=card)
    if response.status_code == 200:
        dataJson = response.json()
