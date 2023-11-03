// SPDX-License-Identifier: MIT

import "@openzeppelin/contracts/utils/math/SignedMath.sol";

pragma solidity ^0.8.20;

contract Math {
    function avgFloor(int256 a, int256 b) public pure returns (int256) {
        return SignedMath.average(a, b);
    }

    function avgCeil(int256 a, int256 b) public pure returns (int256) {
        // Formula from the book "Hacker's Delight"
        return (a | b) - ((a ^ b) >> 1);
    }

    function level5(int256 a, int256 b) external view returns (int256) {
        // TODO: Write your solution here

        return this.avgCeil(a, b);
    }

    function level4(uint256 number) external pure returns (uint256) {
        uint256 y = 0x80000000000000000000000000000000;
        while (y > number) {
            y = y >> 0x01;
        }
        return y;
    }
}
