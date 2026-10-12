import sm

class PureFunction(sm.SM):
    startState = None

    def __init__(self, f):
        self.f = f

    def getNextValues(self, state, inp):
        return (state, self.f(inp))


if __name__ == "__main__":
    pf = PureFunction(lambda x: 2 * x)
    print(pf.transduce([2, 3, 4, 5]))


