from common import ExecutionUnit

class Reduce:
    def __init__(self, units, function, initial=None):
        self.units = units
        self.function = function
        self.initial = initial

        self.units_iter = iter(units)

    def __iter__(self):
        return self
    
    def __next__(self):
        x = self.initial if (not self.initial is None) else next(self.units_iter) 

        y = next(self.units_iter)
        x = ExecutionUnit(self.function, x, y)

        return x

    def __call__(self):
        return self.eval()
        
    def eval(self):
        try:
            x = next(self)

            while True:
                y = next(self)
                x = ExecutionUnit(self.function, x, y)
        except StopIteration:
            return x()


if __name__ == '__main__':
    r = Reduce([1,2,3,4], lambda x, y: x + y)
    print(r.eval())


    from map import Map

    m = Map([1,2,3,4], lambda x: x**2)
    r2 = Reduce(m, lambda x, y: x + y)

    print(r2.eval())