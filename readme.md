### Test Taiko A4's Rand Function

This code is used to test if Taiko A4's rand function is real random. The data used here is the same as in the solidity code: the Sepolia block hash of previous block, the current L2 block id. I drew all historical records of ~580000 rows.

The logic is the same as solidity, rewritten in Python.

First, let's check the case when all the weights are the same. Assume the weights are all 48000000, we get the distribution is:

`[18150, 18333, 18179, 18136, 18093, 18367, 18497, 18221, 18406, 18419, 18389, 18293, 18079, 18444, 18274, 18247, 18203, 18556, 18488, 18296, 18350, 18091, 18385, 18485, 18140, 18402, 18489, 18387, 18199, 18347, 18325, 18060]`

Looks the distribution is even.

Then, let's check the case when the weights are not evenly distributed. Assume the weights are function of 48000000 * (1/2)^i. That is the previous weight is two times the current one. We get the distribution:

`[293083, 146901, 73011, 36340, 18230, 9019, 4614, 2248, 1126, 563, 289, 155, 72, 38, 23, 7, 7, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]`

Looks the distribution is the same as the weight.
