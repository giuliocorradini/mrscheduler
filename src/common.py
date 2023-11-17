class ExecutionUnit:
    """
    Class representing the smallest executable unit for map and reduce.

    Encapsulate a function and its input.
    """

    def __init__(self, function, *input):
        self.function = function
        self.input = input

    @staticmethod
    def __eval_if_function_(el):
        return el() if type(el) == ExecutionUnit else el

    def __call__(self):
        inputs = [self.__eval_if_function_(el) for el in self.input]
        return self.function(*inputs)
