
// Main entry point for the job_escrow program.

use anchor_lang::prelude::*;
use instructions::*;

pub mod instructions;
pub mod state;

// TODO: Replace this with your deployed program ID.
declare_id!("JobEscrow111111111111111111111111111111111111");

#[program]
pub mod job_escrow {
    use super::*;

    // TODO: Create a new job escrow, locking funds into a vault.
    pub fn create_job(ctx: Context<CreateJob>, job_hash: [u8; 32], amount: u64) -> Result<()> {
        create_job::handler(ctx, job_hash, amount)
    }

    // TODO: Submit a zk proof and update job state.
    pub fn submit_proof(ctx: Context<SubmitProof>, proof_hash: [u8; 32]) -> Result<()> {
        submit_proof::handler(ctx, proof_hash)
    }

    // TODO: Verify the proof off-chain, then release funds to worker.
    pub fn release_funds(ctx: Context<ReleaseFunds>) -> Result<()> {
        release_funds::handler(ctx)
    }

    // TODO: Cancel job and refund client if timeout occurs.
    pub fn cancel_job(ctx: Context<CancelJob>) -> Result<()> {
        cancel_job::handler(ctx)
    }

    // TODO: Slash worker and refund job if proof invalid (CPI from slashing_engine).
    pub fn slash_and_revert(ctx: Context<SlashAndRevert>) -> Result<()> {
        slash_and_revert::handler(ctx)
    }
}
