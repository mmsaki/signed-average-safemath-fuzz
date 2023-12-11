from woke.testing import *
from woke.testing.fuzzing import *
from pytypes.contracts.Math import Math
from decimal import Decimal
from decimal import *
import math
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
    def flow_signed_math(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

        # FLOOR : rounding towards zero
        self.avg = self.signed_math.avgFloor(a, b) # floor
        self.actual = int(Decimal(a + b) / 2) # floor

        # # CEIL
        # self.avg = self.signed_math.avgCeil(a, b) # ceil
        # self.actual = math.ceil(Decimal(a + b) / 2) # ceil


    @flow()
    def flow_level_5(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
       

        self.test1 = self.signed_math.level5(2**255-1,100);
        self.test1a = math.ceil(Decimal(2**255-1 + 100)/ 2);

        self.test2 = self.signed_math.level5(-2**255,-101);
        self.test2a = math.ceil(Decimal(-2**255 + -101)/2);

        assert self.test1 == self.test1a
        assert self.test2 == self.test2a        
 
        # LEVEL5
        self.avg = self.signed_math.level5(a, b) 
        self.actual = math.ceil(Decimal(a + b) / 2) 


    @invariant(period=10)
    def invariant_count(self) -> None:
        assert self.avg == self.actual

@default_chain.connect()
def test_default():
    default_chain.set_default_accounts(default_chain.accounts[0])

    MathTest().run(sequences_count=30, flows_count=100)