class ExecutionUnit:
    """
    Class representing the smallest executable unit for map and reduce.

    Encapsulate a function and its input.
    """

    def __init__(self, function, input):
        self.function = function
        self.input = input

    def __call__(self):
        return self.function(self.input() if type(self.input) == ExecutionUnit else self.input)
