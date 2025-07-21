
use anchor_lang::prelude::*;

// Record of a reported violation that may lead to slashing.
#[account]
pub struct ViolationReport {
    // ID of the job involved in the violation.
    pub job_id: u64,

    // Wallet of the accused worker.
    pub worker_pubkey: Pubkey,

    // Reporter (optional — could be validator, client, DAO bot).
    pub reported_by: Pubkey,

    // Type of violation.
    // TODO: Define enum mapping:
    // 0 = InvalidProof, 1 = SLAMissed, 2 = FraudulentOutput
    pub violation_type: u8,

    // Time of violation report.
    pub timestamp: i64,

    // Status of handling.
    // 0 = Pending, 1 = Executed, 2 = Rejected
    pub status: u8,
}
