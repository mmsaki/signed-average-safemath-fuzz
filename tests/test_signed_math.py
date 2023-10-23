from woke.testing import *
from woke.testing.fuzzing import *
from pytypes.contracts.Math import Math
from decimal import Decimal
from decimal import *
getcontext().prec = 1000

class MathTest(FuzzTest):
    signed_math: Math
    avg: int
    actual: int
    a: int
    b: int

    def pre_sequence(self) -> None:
        self.signed_math = Math.deploy()

    @flow()
    def flow_increment(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        self.avg = self.signed_math.avg(a, b)
        # rounding towards zero
        self.actual = int(Decimal(a + b) / 2)

    @invariant(period=10)
    def invariant_count(self) -> None:
        assert self.avg == self.actual


@default_chain.connect()
def test_default():
    default_chain.set_default_accounts(default_chain.accounts[0])

    MathTest().run(sequences_count=30, flows_count=100)