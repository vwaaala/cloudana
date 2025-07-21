
use anchor_lang::prelude::*;

// State definitions for staking accounts.

// TODO: Define individual stake account per worker.
#[account]
pub struct StakeAccount {
    // Wallet that owns this stake.
    pub authority: Pubkey,

    // Amount of CLD staked.
    pub staked_amount: u64,

    // Timestamp of last stake — used for cooldown logic.
    pub last_stake_ts: i64,

    // Optional pending unstake request.
    pub pending_unstake: Option<UnstakeRequestData>,
}

// TODO: Optional structure to hold pending unstake metadata.
#[derive(AnchorSerialize, AnchorDeserialize, Clone)]
pub struct UnstakeRequestData {
    pub requested_at: i64,
    pub amount: u64,
}

// TODO: Global pool state (if needed for analytics, APY, etc.)
#[account]
pub struct GlobalStakePool {
    // Total amount of CLD staked across system.
    pub total_staked: u64,

    // Optional DAO-controlled parameters (e.g., cooldown time, min stake)
    // pub cooldown_period: i64,
    // pub min_stake: u64,
}
