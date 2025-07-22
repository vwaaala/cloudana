# worker.py
# TODO: Define routes for worker lifecycle: registration, update, heartbeat

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/worker", tags=["worker"])

# TODO: Define worker registration request model
# class RegisterWorkerRequest(BaseModel):
#     pubkey: str
#     metadata_uri: str
#     zk_pubkey_hash: str

# TODO: Register a new compute worker
# @router.post("/register")
# async def register_worker(req: RegisterWorkerRequest):
#     - Validate zk_pubkey_hash format
#     - Call worker_service.register()
#     - Return success or error

# TODO: Worker heartbeat
# @router.post("/heartbeat")
# async def worker_heartbeat(pubkey: str):
#     - Update last_seen timestamp
#     - Return OK or 404 if not registered
