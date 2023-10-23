// SPDX-License-Identifier: MIT

import "@openzeppelin/contracts/utils/math/SignedMath.sol";

pragma solidity ^0.8.20;

contract Math {
  function avg(int256 a, int256 b) public pure returns (int256) {
    return SignedMath.average(a,b);
  } 
}