
// Main entry point for the governance_dao program.

use anchor_lang::prelude::*;

pub mod instructions;
pub mod state;

use instructions::*;

// TODO: Replace this with the actual program ID.
declare_id!("GovernanceDao11111111111111111111111111111111");

#[program]
pub mod governance_dao {
    use super::*;

    // TODO: Create a new governance proposal.
    pub fn create_proposal(ctx: Context<CreateProposal>, title: String, description_uri: String, options: Vec<String>) -> Result<()> {
        create_proposal::handler(ctx, title, description_uri, options)
    }

    // TODO: Cast a vote on an existing proposal.
    pub fn vote(ctx: Context<Vote>, option: u8) -> Result<()> {
        vote::handler(ctx, option)
    }

    // TODO: Finalize voting and set result.
    pub fn finalize_proposal(ctx: Context<FinalizeProposal>) -> Result<()> {
        finalize_proposal::handler(ctx)
    }
}
