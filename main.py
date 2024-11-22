# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import Dict

# Initialize FastAPI app
app = FastAPI(
    title="Hello World API",
    description="A minimal production-ready API",
    version="1.0.0"
)

# Response model
class HelloResponse(BaseModel):
    message: str
    
@app.get("/", response_model=HelloResponse)
async def hello_world() -> Dict[str, str]:
    return {"message": "Hello, World!"}

@app.get("/hello/{name}", response_model=HelloResponse)
async def hello_name(name: str) -> Dict[str, str]:
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)