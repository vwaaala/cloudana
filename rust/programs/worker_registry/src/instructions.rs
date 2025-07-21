 
// Central module to organize all instruction handlers for worker_registry.

// TODO: Break out each instruction into its own module (for clarity).
// Use mod.rs style layout for better structure.

pub mod register_worker;
pub mod update_worker;
pub mod deactivate_worker;
pub mod heartbeat;

// TODO: Re-export all handlers so they can be used in lib.rs.
pub use register_worker::*;
pub use update_worker::*;
pub use deactivate_worker::*;
pub use heartbeat::*;
