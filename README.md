# 🌩️ Cloudana — Decentralized Verifiable Compute

Modular compute economy built on Solana. zkSNARK-verified, stake-secured.

## Structure

- `rust/`: Smart contracts & CLI
- `backend/`: FastAPI compute orchestration
- `circuits/`: zkSNARKs
- `sdk/`: Python/TS client libraries

> Start from Phase 1: Smart Contract Design
cloudana/rust/programs/
├── Cargo.toml                    # Workspace manifest
├── worker_registry/             # Anchor program
│   ├── Cargo.toml
│   └── src/
│       ├── lib.rs
│       ├── instructions.rs      # Handle all instructions
│       └── state.rs             # WorkerAccount struct, etc.
├── staking_manager/
│   ├── Cargo.toml
│   └── src/
│       ├── lib.rs
│       ├── instructions.rs
│       └── state.rs
├── job_escrow/
│   ├── Cargo.toml
│   └── src/
│       ├── lib.rs
│       ├── instructions.rs
│       └── state.rs
├── governance_dao/
│   ├── Cargo.toml
│   └── src/
│       ├── lib.rs
│       ├── instructions.rs
│       └── state.rs
├── slashing_engine/
│   ├── Cargo.toml
│   └── src/
│       ├── lib.rs
│       ├── instructions.rs
│       └── state.rs