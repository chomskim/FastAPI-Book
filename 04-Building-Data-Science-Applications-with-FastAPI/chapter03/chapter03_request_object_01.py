from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def get_request_object(request: Request):
    return {
        "request.method": request.method,
        "request.url": request.url,
        "request.headers": request.headers,
        "request.query_params": request.query_params,
        "request.client": request.client
        }
