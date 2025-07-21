
use anchor_lang::prelude::*;

// DAO Proposal account (one per active vote)
#[account]
pub struct Proposal {
    // ID for indexing or reference.
    pub proposal_id: u64,

    // Who created this proposal.
    pub creator_pubkey: Pubkey,

    // Off-chain URI (IPFS or HTTPS) for proposal body.
    pub description_uri: String,

    // Title string (short summary).
    pub title: String,

    // Options presented in this vote (e.g., ["yes", "no"]).
    pub options: Vec<String>,

    // Tally of votes per option.
    pub vote_counts: Vec<u64>,

    // Proposal state enum.
    // TODO: Define as u8 enum with values: 0 = Active, 1 = Passed, 2 = Rejected
    pub status: u8,

    // Time boundaries.
    pub start_ts: i64,
    pub end_ts: i64,
}

// Per-user vote tracking (one per proposal per user)
#[account]
pub struct Voter {
    pub voter_pubkey: Pubkey,
    pub proposal_id: u64,

    // CLD stake at vote time (used for weighting)
    pub weight: u64,

    // Option index (0 = first choice, etc.)
    pub voted_option: u8,

    // Prevent double-voting
    pub has_voted: bool,
}
