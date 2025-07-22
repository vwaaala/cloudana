# job_service.py
# TODO: Job lifecycle: create, proof verification, fund release

# TODO: create_job(client_pubkey, worker_pubkey, job_hash, amount)
# - Create DB entry
# - Escrow funds via solana_client.provider
# - Return job ID

# TODO: submit_proof(job_id, proof_path, public_path)
# - Call zk.verifier.verify_proof()
# - If valid, update job record
# - Trigger fund release via solana_client.provider

# TODO: release_funds(job_id)
# - Confirm job has valid proof
# - Call on-chain escrow release

# TODO: cancel_job(job_id)
# - Only if expired or failed
# - Refund client via escrow
