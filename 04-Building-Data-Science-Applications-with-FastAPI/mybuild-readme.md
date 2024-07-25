## Chapter 3

```sh
uvicorn --host 0.0.0.0 chapter3_project.app:app

pip install python-multipart

uvicorn --host 0.0.0.0 chapter03_form_data_01:app

curl --location 'http://172.30.1.72:8000/users' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'name=kim' \
--data-urlencode 'age=30'

HTTP
POST /users HTTP/1.1
Host: 172.30.1.72:8000
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

name=kim&age=30

```

```py
import requests

url = "http://172.30.1.72:8000/users"

payload = 'name=kim&age=30'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```
uvicorn --host 0.0.0.0 chapter03_file_uploads_02:app

curl --location 'http://172.30.1.72:8000/files' \
--form 'file=@"/C:/Users/cskim/Pictures/avatar-b001-400.png"'

{
    "file_name": "avatar-b001-400.png",
    "content_type": "image/png"
}

curl --location 'http://172.30.1.72:8000/files' \
--form 'file=@"/home/cskim/images/avatar/avatar-b001-400.png"'
{"file_name":"avatar-b001-400.png","content_type":"image/png"}

uvicorn --host 0.0.0.0 chapter03_file_uploads_03:app

curl --location 'http://172.30.1.72:8000/files' \
--form 'files=@"/C:/Users/cskim/Pictures/avatar-b001-400.png"' \
--form 'files=@"/C:/Users/cskim/Pictures/penn-love-sm.png"'

[
    {
        "file_name": "avatar-b001-400.png",
        "content_type": "image/png"
    },
    {
        "file_name": "penn-love-sm.png",
        "content_type": "image/png"
    }
]

uvicorn --host 0.0.0.0 chapter03_headers_cookies_01:app

curl --location 'http://172.30.1.72:8000/' \
--header 'Hello: World'
{
    
    "hello": "World"
}

uvicorn --host 0.0.0.0 chapter03_headers_cookies_02:app
curl --location 'http://172.30.1.72:8000/'
{"user_agent":"curl/7.81.0"}

uvicorn --host 0.0.0.0 chapter03_request_object_01:app
    return {
        "request.method": request.method,
        "request.url": request.url,
        "request.headers": request.headers,
        "request.query_params": request.query_params,
        "request.client": request.client
        }
curl --location 'http://172.30.1.72:8000/' -- actually use postman
{
    "request.method": "GET",
    "request.url": {
        "_url": "http://172.30.1.72:8000/"
    },
    "request.headers": {
        "user-agent": "PostmanRuntime/7.39.0",
        "accept": "*/*",
        "cache-control": "no-cache",
        "postman-token": "ae4988ec-a758-4a32-8e33-7e66e658bf4d",
        "host": "172.30.1.72:8000",
        "accept-encoding": "gzip, deflate, br",
        "connection": "keep-alive"
    },
    "request.query_params": {},
    "request.client": [
        "172.30.1.50",
        53191
    ]
}

uvicorn --host 0.0.0.0 chapter03_response_path_parameters_04:app
curl --location 'http://172.30.1.72:8000/posts/1'
{
    "title": "Hello"
}

uvicorn --host 0.0.0.0 chapter03_custom_response_03:app
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     172.30.1.50:53297 - "GET /redirect HTTP/1.1" 301 Moved Permanently
INFO:     172.30.1.50:53297 - "GET /new-url HTTP/1.1" 200 OK

```

## Chapter 5

```sh
uvicorn --host 0.0.0.0 02_function_dependency_01:app

http://localhost:8000/items?skip=5&limit=50
{"skip":5,"limit":50}


```

## Chapter 6

```sh


```

## Chapter 10

```sh
cd chapter10/project
docker build -t fastapi-app .

docker run -p 8000:80 -e ENVIRONMENT=production -e DATABASE_URL=sqlite+aiosqlite:///app.db fastapi-app

curl --location 'http://172.30.1.72:8000/posts' \
--header 'Content-Type: application/json' \
--data '{
"title": "hello",
"content": "world" 
}'

http://localhost:8000/posts
[{"title":"hello","content":"world","publication_date":"2024-07-24T23:07:22.145819","id":1}]

curl --location 'http://172.30.1.72:8000/posts'
[
    {
        "title": "hello",
        "content": "world",
        "publication_date": "2024-07-24T23:07:22.145819",
        "id": 1
    }
]

```


