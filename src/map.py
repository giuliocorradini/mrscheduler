from common import ExecutionUnit
from functools import partial

class Map:
    def __init__(self, units, function):
        self.call_units = True if type(units) == Map else False
        self.units = units
        self.function = function
        self.units_iterator = iter(units)

    def __iter__(self):
        return self
    
    def __next__(self):
        u = next(self.units_iterator)

        map_unit = ExecutionUnit(self.function, u)

        return map_unit
    
    def __call__(self):
        return self.eval()

    def eval(self):
        return [u() for u in self]
    
if __name__ == '__main__':
    m = Map([1,2,3,4], str)
    print(m.eval())

    m1 = Map([1,2,3,4], lambda x: x+1)
    m2 = Map(m1, lambda x: x*2)

    print(m2.eval())
