from fastapi import FastAPI
from app.api.users.routes import router as users_router
from app.db.database import Base, engine

# Create all tables
Base.metadata.create_all(engine)

app = FastAPI(title="User Management API", version="0.1", tags=["main_tag"])

app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}
