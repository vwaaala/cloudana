# governance.py
# TODO: DAO proposal lifecycle: create, vote, finalize

from fastapi import APIRouter

router = APIRouter(prefix="/governance", tags=["governance"])

# TODO: Create a governance proposal
# @router.post("/proposal")
# async def create_proposal(...):
#     - Accept title, description_uri, options[]
#     - Store in DB
#     - Start proposal window (start_ts → end_ts)

# TODO: Vote on a proposal
# @router.post("/vote")
# async def vote(...):
#     - Accept proposal_id, voter_pubkey, option_index
#     - Call governance_service.vote()
#     - Apply stake weight
#     - Prevent double voting

# TODO: Finalize vote
# @router.post("/finalize")
# async def finalize(...):
#     - Accept proposal_id
#     - Tally votes, update status
#     - Emit result (e.g., emit DAO event)
