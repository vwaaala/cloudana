
// Main entry point for the worker_registry program.

use anchor_lang::prelude::*;

// TODO: Import instruction and state modules.
pub mod instructions;
pub mod state;

use instructions::*;

// TODO: Replace this with a real program ID once deployed.
declare_id!("WorkerRegistry1111111111111111111111111111111");

#[program]
pub mod worker_registry {
    use super::*;

    // TODO: Implement worker registration.
    // Should create WorkerAccount with zkPubkeyHash, metadata, default score.
    pub fn register_worker(ctx: Context<RegisterWorker>, metadata_uri: String, zk_pubkey_hash: [u8; 32]) -> Result<()> {
        register_worker::handler(ctx, metadata_uri, zk_pubkey_hash)
    }

    // TODO: Allow metadata update for existing registered worker.
    pub fn update_worker(ctx: Context<UpdateWorker>, metadata_uri: String) -> Result<()> {
        update_worker::handler(ctx, metadata_uri)
    }

    // TODO: Soft deactivate a worker (e.g., voluntary exit or slashed).
    pub fn deactivate_worker(ctx: Context<DeactivateWorker>) -> Result<()> {
        deactivate_worker::handler(ctx)
    }

    // TODO: Heartbeat function to mark recent activity timestamp.
    pub fn heartbeat(ctx: Context<Heartbeat>) -> Result<()> {
        heartbeat::handler(ctx)
    }
}
