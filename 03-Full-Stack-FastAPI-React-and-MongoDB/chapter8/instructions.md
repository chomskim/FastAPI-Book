## Chapter 8

### Backend

```sh
pip install cloudinary
pip install Pillow
```

- Add new User

```sh
http POST "http://localhost:8000/users/register" email="marko@gmail.com" password="marko" username="marko" role="ADMIN"
HTTP/1.1 201 Created
content-length: 168
content-type: application/json
date: Sun, 30 Oct 2022 07:52:44 GMT
server: uvicorn

{
    "_id": "635e2d4dcfb47ebe11de5d73",
    "email": "marko@gmail.com",
    "password": "$2b$12$smcRT2TY8qzbk3q.9f4eVOYi6/bJz8DLEKzsar8yLgy5AyPScpHiS",
    "role": "ADMIN",
    "username": "marko"
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

http POST 127.0.0.1:8000/users/register username="kim1" password="kimbill" role="ADMIN" email="kim1@gmail.com"
http POST 127.0.0.1:8000/users/register username="kandh" password="kandh" role="ADMIN" email="kandh@gmail.com"

[.env]
DB_URL = "mongodb+srv://<user>:<password>@cluster0.#######.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "carsDB"
COLLECTION_NAME = "cars1"

CLOUD_NAME=dd0######
API_KEY=93############
API_SECRET=<serect key>
[./backend]
#python importScript.py [CarBase2-->CarDB]

python main.py


```

### Frontend

```sh
npx create-next-app .

yarn -D add tailwindcss postcss autoprefixer
yarn -D add @tailwindcss/forms
npx tailwindcss init -p

yarn add cloudinary-build-url
yarn add axios
yarn add cookie cookies-next
yarn add jsonwebtoken jwt-decode
yarn add swr
```

- Set .env File

```sh
[.env]
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000

NEXT_PUBLIC_CLOUD_NAME=dd0######
```

- Use axios

```sh
yarn add axios

```

```sh
yarn
yarn start

```
