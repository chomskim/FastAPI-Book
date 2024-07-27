## Building Python Web APIs with FastAPI Book

### Install Python

### Install venv

```sh
pip install fastapi uvicorn
```

### Chapter 2

```sh
cd ch02/todos
uvicorn api:app --port 8000 --reload

url http://127.0.0.1:8000/
{"message":"Hello World"}(env0)

curl -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"id": 1,
"item": "First Todo is to finish this book!"
}'
--------
{"message":"Todo added successfully."}

curl -X 'GET' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json'
--------
{"todos":[{"id":1,"item":"First Todo is to finish this book!"}]}

curl -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"id": 1,
"item": "First Todo is to finish this book!"
}'
--------
{
"message": "Todo added successfully."
}

curl -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{}'
--------
{
  "detail": [
    { "loc": ["body", "id"], "msg": "field required", "type": "value_error.missing" },
    { "loc": ["body", "item"], "msg": "field required", "type": "value_error.missing" }
  ]
}

curl -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"id": 2,
"item": "Validation models help with input types"
}'
--------
{"message":"Todo added successfully."}

curl -X 'GET' 'http://127.0.0.1:8000/todo/1' -H 'accept: application/json'
--------
{
  "todo": {
    "id": 1,
    "item": "First Todo is to finish this book!"
  }
}

curl -X 'PUT' \
'http://127.0.0.1:8000/todo/1' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"item": "Read the next chapter of the book."
}'
--------
{"message":"Todo updated successfully."}

```

### Chapter 3

```sh
uvicorn api:app --host=0.0.0.0 --port 8000 --reload

curl -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"id": 1,
"item": "This todo will be retrieved without exposing my ID!"
}'
--------
{"message":"Todo added successfully."}

curl -X 'GET' 'http://127.0.0.1:8000/todo' -H 'accept: application/json'
--------
{
  "todos": [
    {
      "item": "This todo will be retrieved without exposing my ID!"
    }
  ]
}

[GET]http://172.30.1.40:8000/todo/12
--------
{
    "detail": "Todo with supplied ID doesn't exist"
}
```

### Chapter 4

```sh
pip install jinja2
pip install python-multipart

uvicorn api:app --host=0.0.0.0 --port 8000 --reload

[Chrome]http://172.30.1.40:8000/todo/

```

### Chapter 5

```sh
pip install "pydantic[email]"

python main.py

curl -X 'POST' \
'http://0.0.0.0:8000/user/signup' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "fastapi@packt.com",
"password": "Stro0ng!",
"username": "FastPackt",
"events": []
}'
--------
{"message":"User successfully registered!"}


curl -X 'POST' \
'http://0.0.0.0:8000/user/signin' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "fastapi@example.com",
"password": "Stro0ng!"
}'
--------
{"message":"User signed in successfully"}

curl -X 'POST' \
'http://0.0.0.0:8000/user/signin' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "fastapi@example.com",
"password": "password!"
}'
--------
{"detail":"Wrong credential passed"}

curl -X 'GET' \
'http://0.0.0.0:8000/event/' \
-H 'accept: application/json'
--------
[]

curl -X 'POST' \
'http://0.0.0.0:8000/event/new' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"id": 1,
"title": "FastAPI Book Launch",
"image": "https://linktomyimage.com/image.png",
"description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
"tags": [
  "python",
  "fastapi",
  "book",
  "launch"
],
"location": "Google Meet"
}'
--------
{"message":"Event created successfully"}

curl -X 'GET' 'http://0.0.0.0:8000/event/1' -H 'accept: application/json'
--------
{
  "id": 1,
  "title": "FastAPI Book Launch",
  "image": "https://linktomyimage.com/image.png",
  "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
  "tags": [
    "python",
    "fastapi",
    "book",
    "launch"
  ],
  "location": "Google Meet"
}

curl -X 'DELETE' 'http://0.0.0.0:8000/event/1' -H 'accept: application/json'
--------
{"message":"Event deleted successfully"}

curl -X 'GET' 'http://0.0.0.0:8000/event/1' -H 'accept: application/json'
--------
{"detail":"Event with supplied ID does not exist"}
```

### Chapter 6 -- ch06-sql

### SQL Build

```sh
pip install sqlmodel
pip install pydantic_settings

[Git checkout from planner-sql branch]

mkdir images
python main.py
NFO:     Will watch for changes in these directories: ['/home/cskim/blockchain-repo/BPWA-with-FastAPI/ch06-sql/planner']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [10913] using StatReload
INFO:     Started server process [10933]
INFO:     Waiting for application startup.

[After http://127.0.0.1:8000]

2022-10-18 16:01:46,987 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-10-18 16:01:46,997 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("event")
2022-10-18 16:01:46,997 INFO sqlalchemy.engine.Engine [raw sql] ()
2022-10-18 16:01:46,999 INFO sqlalchemy.engine.Engine COMMIT
INFO:     Application startup complete.
INFO:     127.0.0.1:42778 - "GET / HTTP/1.1" 307 Temporary Redirect
2022-10-18 16:06:58,089 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-10-18 16:06:58,097 INFO sqlalchemy.engine.Engine SELECT event.tags, event.id, event.title, event.image, event.description, event.location
FROM event
2022-10-18 16:06:58,154 INFO sqlalchemy.engine.Engine [generated in 0.05782s] ()
INFO:     127.0.0.1:42778 - "GET /event/ HTTP/1.1" 200 OK
2022-10-18 16:06:58,274 INFO sqlalchemy.engine.Engine ROLLBACK

[From Another terminal]
curl -X 'POST' \
'http://0.0.0.0:8000/event/new' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"title": "FastAPI Book Launch",
"image": "fastapi-book.jpeg",
"description": "We will be discussing the contents of the FastAPI book in this event!",
"tags": [
  "python",
  "fastapi",
  "book",
  "launch"
  ],
"location": "Google Meet"
}'
--------
{"message":"Event created successfully"}

curl -X 'GET' 'http://0.0.0.0:8000/event/' -H 'accept: application/json'
--------
[
  {
    "id": 2,
    "title": "FastAPI BookLaunch",
    "image": "https://linktomyimage.com/image.png",
    "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
    "tags": [
      "python",
      "fastapi",
      "book",
      "launch"
    ],
    "location": "Google Meet"
  },
  {
    "id": 3,
    "title": "FastAPI Book Launch",
    "image": "fastapi-book.jpeg",
    "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
    "tags": [
      "python",
      "fastapi",
      "book",
      "launch"
    ],
    "location": "Google Meet"
  }
]
```

#### Update Class EventUpdate -- for pydantic v2.0

```py
class EventUpdate(SQLModel):
    title: Optional[str] = Field(default=None)
    image: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    tags: Optional[List[str]] = Field(default=None)
    location: Optional[str] = Field(default=None)
```

```sh
curl --location --request PUT 'http://172.30.1.72:8000/event/edit/1' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Very SlowAPI Book Launch"
}'

{
    "image": "fastapi-book.jpeg",
    "id": 1,
    "tags": [
        "python",
        "fastapi",
        "book",
        "launch"
    ],
    "title": "Very SlowAPI Book Launch",
    "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
    "location": "Google Meet"
}

```

### MongoDB Build

```sh
pip install beanie motor

```


### Chapter 7

```sh
pip install passlib[bcrypt]
pip install python-jose[cryptography]

python main.py
...
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
...
2024-07-26 20:04:14,472 INFO sqlalchemy.engine.Engine 
CREATE TABLE event (
        id INTEGER NOT NULL, 
        title VARCHAR NOT NULL, 
        image VARCHAR NOT NULL, 
        description VARCHAR NOT NULL, 
        tags JSON, 
        location VARCHAR NOT NULL, 
        PRIMARY KEY (id)
)
...
CREATE TABLE user (
        email VARCHAR NOT NULL, 
        username VARCHAR NOT NULL, 
        password VARCHAR NOT NULL, 
        events JSON, 
        PRIMARY KEY (email)
)
...

curl --location 'http://172.30.1.72:8000/event/new' \
--header 'Content-Type: application/json' \
--data '{
    "title": "FastAPI Book Launch",
    "image": "fastapi-book.jpeg",
    "description": "We will be discussing the contents of the FastAPI book in this event!",
    "tags": [
        "python",
        "fastapi",
        "book",
        "launch"
    ],
    "location": "Google Meet"
}'
----------------------
{
    "message": "Event created successfully"
}
----------------------
curl --location 'http://172.30.1.72:8000/event/'

[
    {
        "image": "fastapi-book.jpeg",
        "id": 1,
        "tags": [
            "python",
            "fastapi",
            "book",
            "launch"
        ],
        "description": "We will be discussing the contents of the FastAPI book in this event!",
        "title": "FastAPI Book Launch",
        "location": "Google Meet"
    },
    {
        "image": "fastapi-book.jpeg",
        "id": 2,
        "tags": [
            "python",
            "fastapi",
            "book",
            "launch"
        ],
        "description": "We will be discussing the contents of the FastAPI book in this event!",
        "title": "SlowAPI Book Launch",
        "location": "Google Meet"
    },
    {
        "image": "fastapi-book.jpeg",
        "id": 3,
        "tags": [
            "python",
            "fastapi",
            "book",
            "launch"
        ],
        "description": "We will be discussing the contents of the FastAPI book in this event!",
        "title": "Very FastAPI Book Launch",
        "location": "Google Meet"
    }
]

curl --location 'http://172.30.1.72:8000/user/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "fastapi@example.com",
    "events": [],
    "password": "Str0ng!!",
    "username": "fastapiexample001"
}'

{
    "message": "User created successfully"
}

curl --location 'http://172.30.1.72:8000/user/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "slowapi@example.com",
    "events": [1,2],
    "password": "Str0ng!!",
    "username": "slowapi001"
}'

{
    "message": "User created successfully"
}

# async def sign_user_in(user: UserSignIn, session=Depends(get_session)) -> dict:
curl --location 'http://172.30.1.72:8000/user/signin' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "slowapi@example.com",
    "password": "Str0ng!!"
}'

{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2xvd2FwaUBleGFtcGxlLmNvbSIsImV4cGlyZXMiOjE3MjIwNDQ1NjcuMjk3OTk2OH0.o2Emrh50BhtJ2MasMkdSUsrNXpExS4PwuCxK1G_Djtc",
    "token_type": "Bearer"
}

curl --location 'http://172.30.1.72:8000/event/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2xvd2FwaUBleGFtcGxlLmNvbSIsImV4cGlyZXMiOjE3MjIwNDQ1NjcuMjk3OTk2OH0.o2Emrh50BhtJ2MasMkdSUsrNXpExS4PwuCxK1G_Djtc' \
--data '{
    "title": "Very SlowAPI Book Launch",
    "image": "fastapi-book.jpeg",
    "description": "We will be discussing the contents of the FastAPI book in this event!",
    "tags": [
        "python",
        "fastapi",
        "book",
        "launch"
    ],
    "location": "Google Meet"
}'

{
    "message": "Event created successfully"
}

# async def sign_user_in(user: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)) -> dict:

```

### Chapter 8

```sh
pip install pytest
pip install httpx pytest-asyncio
```
