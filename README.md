# OpenZeppelin fuzz

In this repo I will be fuzzing OpenZeppelin SafeMath library with woke.

## Getting Started

> **NOTE** You can set up your you woke environment with my [Template here](https://github.com/mmsaki/woke-template) or clone this repo

1. Setup your environment

   ```sh
   python -m venv venv
   source ./venv/bin/activate
   pip install woke
   ```

1. Install openzepelin contracts you want to fuzz

   ```sh
   pnpm install @openzeppelin/contracts
   # or
   npm install @openzeppelin/contracts
   ```

   > If you are cloning this project just run `npm install` or `pnpm install`

1. Import contracts and libraries in `./contracts/Imports.sol`
1. Write your contracts in `./contracts/Math.sol`
1. Generate pytypes

   ```sh
   woke init pytypes -w
   ```

## Fuzzing

1. Run woke fuzzer

   ```sh
   woke fuzz tests/test_signed_math.py -n 8
   ```

## Average function

```js
function average(int256 a, int256 b) internal pure returns (int256) {
		// Formula from the book "Hacker's Delight"
		int256 x = (a & b) + ((a ^ b) >> 1);
		return x + (int256(uint256(x) >> 255) & (a ^ b));
}
```
