from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import all_routers
from repo.database import create_tables

app = FastAPI(
    title="Intel Excalibur API",
    description="Intelligence management API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()

for router in all_routers:
    app.include_router(router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Intel Excalibur API", "docs": "/docs"}
