from fastapi import FastAPI
from app.database import engine, Base
from app.routers import products, categories, users, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory Management API",
    description="REST API za upravljanje zalihama proizvoda",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(products.router)


@app.get("/")
def root():
    return {"message": "Inventory Management API is running!"}