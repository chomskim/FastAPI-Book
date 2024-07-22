## Chapter 7

### Backend

```sh
pip install email-validator
pip install pyjwt passlib['bcrypt']
```

```sh
http POST 127.0.0.1:8000/users/register username="bill" password="bill" role="ADMIN" email="koko@gmail.com"
HTTP/1.1 201 Created
content-length: 166
content-type: application/json
date: Sat, 29 Oct 2022 11:04:13 GMT
server: uvicorn

{
    "_id": "635d08ad3c5c5e1106e48263",
    "email": "koko@gmail.com",
    "password": "$2b$12$0wzkQA3s9z4rlQoqaZKO4./e/.jbExJ1KPduzANWReP5ykyYhYxfG",
    "role": "ADMIN",
    "username": "bill"
}


http POST http://127.0.0.1:8000/users/login email="tanja@gmail.com" password="tanja"
HTTP/1.1 401 Unauthorized
content-length: 42
content-type: application/json
date: Sat, 29 Oct 2022 11:07:38 GMT
server: uvicorn

{
    "detail": "Invalid email and/or password"
}

http POST 127.0.0.1:8000/users/register username="tanja" password="tanja" role="SALESMAN" email="tanja@gmail.com"
HTTP/1.1 201 Created
...
http POST http://127.0.0.1:8000/users/login email="tanja@gmail.com" password="tanja"
HTTP/1.1 200 OK
content-length: 184
content-type: application/json
date: Sat, 29 Oct 2022 11:30:46 GMT
server: uvicorn

{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjcwNDUxNDcsImlhdCI6MTY2NzA0MzA0Nywic3ViIjoiNjM1ZDBlYmEzYzVjNWUxMTA2ZTQ4MjY0In0.DlR-xmIw_tNRh4B1iL1ZtZW_BtK8ALn0PLOT3SeoEDY"
}

http POST 127.0.0.1:8000/users/login password="bill" email="koko@gmail.com"
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjcwNDUyNzcsImlhdCI6MTY2NzA0MzE3Nywic3ViIjoiNjM1ZDA4YWQzYzVjNWUxMTA2ZTQ4MjYzIn0.dapZsxn9JuDOu_KLXab_bn5BrREZtBSp1ZVhOL7kRt4"
}

http GET 127.0.0.1:8000/users/me "Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjcwNDUyNzcsImlhdCI6MTY2NzA0MzE3Nywic3ViIjoiNjM1ZDA4YWQzYzVjNWUxMTA2ZTQ4MjYzIn0.dapZsxn9JuDOu_KLXab_bn5BrREZtBSp1ZVhOL7kRt4"
HTTP/1.1 200 OK
content-length: 91
content-type: application/json
date: Sat, 29 Oct 2022 11:35:19 GMT
server: uvicorn

{
    "email": "koko@gmail.com",
    "id": "635d08ad3c5c5e1106e48263",
    "role": "ADMIN",
    "username": "bill"
}

http POST 127.0.0.1:8000/users/register username="kim1" password="kimbill" role="ADMIN" email="kim1@gmail.com"
http POST 127.0.0.1:8000/users/register username="kim2" password="kimbill" role="ADMIN" email="kim2@gmail.com"
http POST 127.0.0.1:8000/users/register username="hwang1" password="hwangbill" role="ADMIN" email="hwang1@gmail.com"
http POST 127.0.0.1:8000/users/register username="hwang2" password="hwangbill" role="ADMIN" email="hwang2@gmail.com"
http POST 127.0.0.1:8000/users/register username="kandh" password="kandh" role="ADMIN" email="kandh@gmail.com"

[.env]
DB_URL = "mongodb+srv://<user>:<password>@cluster0.#######.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "carsDB"
COLLECTION_NAME = "cars2"

[./backend]
python importScript.py [CarBase2-->CarDB]

python main.py


```

### Frontend

- Set .env File

```sh
[.env]
REACT_APP_BASE_URL=http://127.0.0.1:8000/
```

- Use axios

```sh
yarn add axios

```

```sh
yarn
yarn start

```
