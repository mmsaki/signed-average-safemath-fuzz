from woke.testing import *
from woke.testing.fuzzing import *
from pytypes.contracts.Math import Math
from decimal import Decimal
from decimal import *
import math
getcontext().prec = 1000

class MathTest(FuzzTest):
    signed_math: Math
    expected: int
    actual: int
    a: int

    def pre_sequence(self) -> None:
        self.signed_math = Math.deploy()

    @flow()
    def flow_signed_math(self) -> None:
        self.a = random_int(0, 2**128-1)

        self.actual = self.signed_math.level4(self.a) 
        self.expected = power_of_2(self.a)

    @invariant(period=10)
    def invariant_count(self) -> None:
        assert self.actual == self.expected

@default_chain.connect()
def test_default():
    default_chain.set_default_accounts(default_chain.accounts[0])

    MathTest().run(sequences_count=30, flows_count=100)


def power_of_2(number: int):
  ans = 0
  for i in range(0, 129):
    if 2**i >= number:
      ans = 2**(i-1)
      return ans
    else:
      continue


  