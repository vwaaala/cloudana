 
// Instruction routing for slashing logic.

pub mod report_violation;
pub mod execute_slash;

// TODO: Re-export handlers for main lib.rs
pub use report_violation::*;
pub use execute_slash::*;
