# worker_service.py
# TODO: Business logic for worker registration, metadata updates, and heartbeat

# TODO: register_worker(pubkey, metadata_uri, zk_pubkey_hash)
# - Check if worker already exists
# - Insert into DB
# - Validate zk_pubkey_hash format
# - Return confirmation or error

# TODO: update_metadata(pubkey, metadata_uri)
# - Update metadata URI
# - Raise error if not registered

# TODO: heartbeat(pubkey)
# - Update last_seen timestamp
# - Used by SLA checker and reward scheduler
