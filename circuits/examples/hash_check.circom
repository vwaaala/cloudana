 
// hash_check.circom
// TODO: Prove that SHA256(input) == expected
// This circuit will be used to verify that off-chain computation
// produces a hash result matching the expected output.

pragma circom 2.0.0;

// TODO: Import sha256 library from circomlib
// include "circomlib/sha256.circom";

template HashCheck() {
    // TODO: Define input signals (simulate a 512-bit input using two field elements)
    // signal input in[2];
    // signal input expected[2];

    // TODO: Instantiate SHA256(2) component for 512-bit input
    // component hasher = Sha256(2);

    // TODO: Connect input to hasher
    // for (var i = 0; i < 2; i++) {
    //     hasher.in[i] <== in[i];
    // }

    // TODO: Enforce equality between actual hash and expected hash
    // for (var i = 0; i < 2; i++) {
    //     hasher.out[i] === expected[i];
    // }
}

// TODO: Set template instantiation as main component
// component main = HashCheck();
