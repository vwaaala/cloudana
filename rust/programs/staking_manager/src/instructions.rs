 
// Centralized instruction module for staking_manager program.

// TODO: Break out logic into separate submodules for maintainability.
pub mod stake;
pub mod unstake_request;
pub mod finalize_unstake;
pub mod slash_worker;
pub mod get_stake_weight;

// TODO: Re-export all handlers for use in lib.rs.
pub use stake::*;
pub use unstake_request::*;
pub use finalize_unstake::*;
pub use slash_worker::*;
pub use get_stake_weight::*;
