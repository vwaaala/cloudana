# job.py
# TODO: Define routes for job creation, proof submission, and escrow payout

from fastapi import APIRouter

router = APIRouter(prefix="/job", tags=["job"])

# TODO: Submit new job request
# @router.post("/create")
# async def create_job(...):
#     - Accept client_pubkey, worker_pubkey, job_hash, amount
#     - Call job_service.create_job()
#     - Trigger fund escrow (via solana_client.provider)
#     - Return job_id

# TODO: Submit zk proof for a job
# @router.post("/submit_proof")
# async def submit_proof(...):
#     - Accept job_id, proof.json, public.json
#     - Call zk verifier
#     - If valid: call job_service.release_funds()
#     - Return success/failure
