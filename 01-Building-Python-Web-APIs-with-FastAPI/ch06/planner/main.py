import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from database.connection import Settings
from routes.events import event_router
from routes.users import user_router

from contextlib import asynccontextmanager
settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    print("startup")
    await settings.initialize_database()
    yield
    # shutdown
    print("shutdown")
    
app = FastAPI(lifespan=lifespan)


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
