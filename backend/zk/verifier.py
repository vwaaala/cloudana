# verifier.py
# TODO: This file will verify zk-SNARK proofs using snarkjs as a subprocess.
# Used in the /submit_proof route to validate proofs before calling on-chain release_funds()

import subprocess
import json
import os

# TODO: Define the file paths relative to the circuits directory
ZKEY_PATH = "cloudana/circuits/artifacts/hash_check/hash_check.zkey"
VK_PATH = "cloudana/circuits/artifacts/hash_check/verification_key.json"

def verify_proof(proof_path: str, public_path: str) -> bool:
    """
    TODO: Use snarkjs to verify Groth16 proof from JSON files.

    :param proof_path: path to proof.json
    :param public_path: path to public.json
    :return: True if valid, False otherwise
    """
    try:
        # TODO: Call `snarkjs groth16 verify` via subprocess
        result = subprocess.run(
            ["snarkjs", "groth16", "verify", VK_PATH, public_path, proof_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        # TODO: Parse stdout or return code
        return "OK" in result.stdout.decode()

    except Exception as e:
        # TODO: Log error properly in production
        print(f"[zkVerifier] Error verifying proof: {e}")
        return False
