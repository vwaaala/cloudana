
use anchor_lang::prelude::*;

// This file defines the state account(s) used by the worker_registry program.

#[account]
pub struct WorkerAccount {
    // TODO: Store the wallet address of the worker (who owns this account).
    pub authority: Pubkey,

    // TODO: URI pointing to metadata (IPFS or HTTPS) describing compute capacity.
    pub metadata_uri: String,

    // TODO: Hash of zk-SNARK public key — used to verify proof identity.
    pub zk_pubkey_hash: [u8; 32],

    // TODO: Reputation score calculated based on completed jobs, proof history, SLA.
    pub reputation_score: u64,

    // TODO: Activity flag — deactivated workers are ignored by scheduler.
    pub active: bool,

    // TODO: Timestamp of last heartbeat or proof submission.
    pub last_seen_ts: i64,

    // Optional: Add bump seed if using PDA (Program Derived Address)
    // pub bump: u8
}
