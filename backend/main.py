# main.py
# TODO: FastAPI application entrypoint for Cloudana backend

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings

# TODO: Import API routers
from api import worker, job, stake, governance

# TODO: Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

# TODO: Enable CORS (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Lock down in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO: Register routers
app.include_router(worker.router)
app.include_router(job.router)
app.include_router(stake.router)
app.include_router(governance.router)

# TODO: Define root endpoint
@app.get("/")
async def root():
    return {"message": "Cloudana backend is live!"}

# TODO (optional): Add startup/shutdown event handlers
# @app.on_event("startup")
# async def startup_db():
#     - Connect to DB
#     - Run pending migrations (if using Alembic)

# @app.on_event("shutdown")
# async def shutdown_db():
#     - Close DB connections cleanly

# Run using: `uvicorn main:app --reload`
