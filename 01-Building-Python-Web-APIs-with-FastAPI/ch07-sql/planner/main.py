import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

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

# register origins

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


# @app.on_event("startup")
# async def init_db():
#     await settings.initialize_database()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
