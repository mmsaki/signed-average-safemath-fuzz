# OpenZeppelin SignedMath bug `SignedMath.average()`

Bug introduced: v4.5.0-rc.0
commit: https://github.com/OpenZeppelin/openzeppelin-contracts/commit/3458c1e8541ce0a0cd935828c9db8f9cbca988a0

# SignedMath.sol

```js
function average(int256 a, int256 b) internal pure returns (int256) {
		// Formula from the book "Hacker's Delight"
		int256 x = (a & b) + ((a ^ b) >> 1);
		return x + (int256(uint256(x) >> 255) & (a ^ b));
}
```

Issue: Weak test cases, and bad implementation

Fix:

```js
function average(int256 a, int256 b) internal pure returns (int256) {
		// Formula from the book "Hacker's Delight"
		return (a & b) + ((a ^ b) >> 1);
}
```
