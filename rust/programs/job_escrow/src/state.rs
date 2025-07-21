
use anchor_lang::prelude::*;

// This account holds job-level metadata and state.
#[account]
pub struct JobAccount {
    // Pubkey of client who funded the job.
    pub client_pubkey: Pubkey,

    // Assigned worker's wallet.
    pub worker_pubkey: Pubkey,

    // Unique job ID or hash (e.g., SHA256 of task input).
    pub job_hash: [u8; 32],

    // Escrowed payment amount.
    pub funded_amount: u64,

    // Job lifecycle state.
    // TODO: Define as an enum for clarity.
    pub status: u8, // 0 = Pending, 1 = InProgress, 2 = Completed, 3 = Cancelled, 4 = Slashed

    // Submitted proof hash (to match against off-chain verifier).
    pub submitted_proof_hash: Option<[u8; 32]>,

    // TODO: Add created_ts, expiry_ts if SLA logic is time-bound.
    // pub created_ts: i64,
    // pub expiry_ts: i64,
}

// Escrow vault PDA to hold CLD tokens per job
#[account]
pub struct EscrowVault {
    // TODO: Store associated SPL token account for job funds.
    pub token_account: Pubkey,
    pub bump: u8,
}
