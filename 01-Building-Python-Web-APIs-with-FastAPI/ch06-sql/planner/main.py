import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
# from fastapi.staticfiles import StaticFiles

from database.connection import conn

from routes.users import user_router
from routes.events import event_router


from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    print("startup")
    conn()
    yield
    # shutdown
    print("shutdown")

app = FastAPI(lifespan=lifespan)

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# app.mount("/images", StaticFiles(directory="images"), name="images")

# @app.on_event("startup")
# def on_startup():
#     conn()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
