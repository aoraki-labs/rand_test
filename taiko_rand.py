from web3 import Web3
from web3.middleware.geth_poa import geth_poa_middleware
from eth_abi import encode

# test rpc from endpoint
w3 = Web3(Web3.HTTPProvider(""))

# Suppose weight is all 48,000,000:
weights = [48000000] * 32
weights = [48000000 / 2 ** exp for exp in range(32)]
total_weight = sum(weights)


def read_history() -> list:
    tup = []
    with open("taiko_rand.csv") as f:
        counter = 0
        for line in f:
            if counter > 100000:
                break
            line = line.strip().split(",")
            tup.append((line[0], int(line[1])))
            counter += 1
    
    return tup


def get_slot_index(blockhash: str, proposed_id: int) -> int:

    blockhash_bytes = w3.to_bytes(hexstr=blockhash)
    encoded = encode(['bytes32', 'int256'], [blockhash_bytes, proposed_id]) 
    rand = w3.to_int(w3.solidity_keccak(['bytes32'], [encoded]))

    r = rand % total_weight
    accumulated_weight = 0
    for i in range(32):
        accumulated_weight += weights[i]
        if r < accumulated_weight:
            return i


if __name__ == "__main__":
    tup = read_history()
    
    index_count = [0] * 32
    for (blockhash, proposed_id) in tup:
        index = get_slot_index(blockhash, proposed_id)
        index_count[index] += 1
    
    print(index_count)
