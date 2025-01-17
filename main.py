from fastapi import FastAPI
from routers import pokemon

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(pokemon.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Pokemon API!"}