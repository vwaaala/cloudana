# 🌩️ Cloudana — Decentralized Verifiable Compute

Modular compute economy built on Solana. zkSNARK-verified, stake-secured.

## Structure

- `rust/`: Smart contracts & CLI
- `backend/`: FastAPI compute orchestration
- `circuits/`: zkSNARKs
- `sdk/`: Python/TS client libraries

> 🚀 Phase 1: Rust (Solana) Smart Contracts
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

> 🧪 Phase 2: zkSNARK Integration
> 2.1 Circuit & Prover Setup
cloudana/
├── circuits/
│   ├── examples/
│   │   ├── hash_check.circom        # Basic proof: sha256(input) == expected
│   │   ├── matrix_mult.circom       # Slightly complex: dot product/matrix
│   ├── artifacts/
│   │   ├── hash_check/
│   │   │   ├── hash_check.r1cs
│   │   │   ├── hash_check.wasm
│   │   │   ├── zkey
│   │   │   └── verification_key.json
│   ├── verifier_contracts/
│   │   ├── hash_check.sol
│   │   └── hash_check.rs            # Optional verifier for on-chain use

# 📦 zkSNARK Artifact Directory: hash_check

This directory contains the compiled and trusted setup artifacts for the `hash_check.circom` circuit.

---

## ✅ Artifacts

1. `hash_check.r1cs`
   - TODO: Generated via `circom hash_check.circom --r1cs`
   - Represents the compiled circuit in Rank-1 Constraint System format

2. `hash_check.wasm`
   - TODO: Also generated via `circom` command
   - WASM binary used to compute the witness from input.json

3. `zkey`
   - TODO: Generated via `snarkjs groth16 setup`
   - Contains proving and verifying keys post trusted setup

4. `verification_key.json`
   - TODO: Exported using `snarkjs zkey export verificationkey`
   - Used to verify the proof (by verifier contract or snarkjs CLI)

---

## 🛠️ Build Steps (To Generate These Files)

1. Compile the circuit:
   ```bash
   circom ../../examples/hash_check.circom --r1cs --wasm -o .

> 🌐 Phase 3: Python Backend API (FastAPI)

cloudana/backend/
├── api/                         # FastAPI routes (organized by domain)
│   ├── worker.py                # /register, /heartbeat
│   ├── job.py                   # /create_job, /submit_proof
│   ├── stake.py                 # /stake, /unstake, /slash
│   ├── governance.py            # /proposal, /vote
│   └── __init__.py
│
├── services/                    # Business logic layer
│   ├── worker_service.py
│   ├── job_service.py
│   ├── stake_service.py
│   ├── governance_service.py
│   └── __init__.py
│
├── zk/                          # zkSNARK integration
│   ├── verifier.py              # snarkjs-based proof validation
│   └── witness_generator.py     # (Optional) generate witness from input
│
├── solana_client/               # Interact with Anchor programs (via solana-py or Anchor IDL)
│   ├── provider.py
│   └── staking.py
│
├── db/                          # DB models (SQLAlchemy or Tortoise)
│   ├── base.py
│   ├── worker.py
│   ├── job.py
│   ├── stake.py
│   ├── governance.py
│   └── __init__.py
│
├── tasks/                       # Background jobs
│   ├── proof_queue.py           # Proof verification + fund release
│   ├── slashing_watchdog.py     # SLA monitor and slashing trigger
│   └── __init__.py
│
├── config/                      # Settings & environment
│   └── settings.py
│
├── main.py                      # FastAPI app entrypoint
└── requirements.txt             # Dependency list
