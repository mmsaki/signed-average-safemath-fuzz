/*
Sometimes, a contract from dependencies is not needed in the project contracts,
but may become useful when testing the contracts. In this case, it is recommended
to import the needed contracts so that pytypes are generated for them.
*/

import "@openzeppelin/contracts/utils/math/SignedMath.sol";