# stake.py
# TODO: Stake, unstake, finalize unstake, and slash endpoints

from fastapi import APIRouter

router = APIRouter(prefix="/stake", tags=["stake"])

# TODO: Stake CLD tokens
# @router.post("/stake")
# async def stake_tokens(...):
#     - Accept pubkey and amount
#     - Call stake_service.stake()
#     - Broadcast to Solana (via solana_client.staking)
#     - Return tx hash

# TODO: Request unstake
# @router.post("/unstake")
# async def unstake_request(...):
#     - Apply cooldown
#     - Return unlock time

# TODO: Finalize unstake
# @router.post("/finalize")
# async def finalize_unstake(...):
#     - Transfer CLD back to user
#     - Mark stake as withdrawn

# TODO: Slash a worker
# @router.post("/slash")
# async def slash_worker(...):
#     - Only callable by slashing service / DAO
#     - Reduce staked amount and log
