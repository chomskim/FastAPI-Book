## Chapter 5

### Backend using Python FastAPI

```sh
pip install motor dnspython
pip install python-decouple
```

### Set .env [Using decouple to get .env]

```sh
[.env]
DB_URL = "mongodb+srv://<dbuser>:<password>@cluster0.#####.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "carsDB"
COLLECTION_NAME = "cars1"
```

### Run API Server

```sh
python importScript.py [import sample data to DB]

python main.py

http GET "http://localhost:8000/cars/"
HTTP/1.1 200 OK
content-length: 2869
content-type: application/json
date: Thu, 27 Oct 2022 03:07:33 GMT
server: uvicorn

[{"_id":"6359f3a8cb8d71e23efa8beb","brand":"Ford","make":"Fiesta","year":2004,"price":1950,"km":164572,"cm3":1399},
{"_id":"6359f3a8cb8d71e23efa8be9","brand":"Fiat","make":"500L","year":2014,"price":7499,"km":159193,"cm3":1248},
{"_id":"6359f3a8cb8d71e23efa8be8","brand":"Lada","make":"Niva","year":2000,"price":2200,"km":135000,"cm3":1689},
{"_id":"6359f3a8cb8d71e23efa8be7","brand":"Renault","make":"Megane","year":2008,"price":2950,"km":191707,"cm3":1461},
...
{"_id":"6359f3a7cb8d71e23efa8bcf","brand":"Seat","make":"Altea","year":2005,"price":2890,"km":162358,"cm3":1896}]

http POST "http://localhost:8000/cars/" brand="aaa" make="500" year=2015 cm3=1222 price=2000 km=100000
HTTP/1.1 201 Created
content-length: 109
content-type: application/json
date: Thu, 27 Oct 2022 03:10:21 GMT
server: uvicorn

{
    "_id": "6359f69d3d4a61cf2d6aa192",
    "brand": "aaa",
    "cm3": 1222,
    "km": 100000,
    "make": "500",
    "price": 2000,
    "year": 2015
}
```
