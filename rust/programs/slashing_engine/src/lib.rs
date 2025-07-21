
// Main entry point for the slashing_engine program.

use anchor_lang::prelude::*;

pub mod instructions;
pub mod state;

use instructions::*;

// TODO: Replace with actual deployed program ID.
declare_id!("SlashingEngine1111111111111111111111111111111");

#[program]
pub mod slashing_engine {
    use super::*;

    // TODO: Called by backend/API to report a violation after off-chain detection.
    pub fn report_violation(ctx: Context<ReportViolation>, job_id: u64, violation_type: u8) -> Result<()> {
        report_violation::handler(ctx, job_id, violation_type)
    }

    // TODO: Slash the worker's stake and trigger escrow refund. CPI to `staking_manager` and `job_escrow`.
    pub fn execute_slash(ctx: Context<ExecuteSlash>) -> Result<()> {
        execute_slash::handler(ctx)
    }
}
