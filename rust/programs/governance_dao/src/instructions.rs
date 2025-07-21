 
// Centralized instruction dispatcher for governance DAO.

pub mod create_proposal;
pub mod vote;
pub mod finalize_proposal;

// TODO: Re-export handlers for program use
pub use create_proposal::*;
pub use vote::*;
pub use finalize_proposal::*;
