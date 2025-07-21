# 🌩️ Cloudana — Decentralized Verifiable Compute

Modular compute economy built on Solana. zkSNARK-verified, stake-secured.

## Structure

- `rust/`: Smart contracts & CLI
- `backend/`: FastAPI compute orchestration
- `circuits/`: zkSNARKs
- `sdk/`: Python/TS client libraries

> Phase 1: 🚀 Phase 1: Rust (Solana) Smart Contracts
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

> Phase 2: 🧪 Phase 2: zkSNARK Integration
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
