from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()

@app.get("/headers")
async def read_headers(user_agent: Optional[str] = Header(None)):
    
    return {"User-Agent": user_agent}
