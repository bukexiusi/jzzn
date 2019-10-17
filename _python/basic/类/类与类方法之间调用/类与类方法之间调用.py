class A():

    def __init__(self):
        pass

    def methodA(self, zn):
        print(zn)


class B():

    def __init__(self, A):
        self.A = A

    def methodA(self):
        zn = 'zn'
        self.A.methodA(zn)

class C():

    def __init__(self):
        pass

    def methodC(self):
        execute = D(self)
        execute.methodD()

    def methodCC(self, zn):
        print(zn)

class D():

    def __init__(self, C):
        self.C = C

    def methodD(self):
        zn = 'zn'
        self.C.methodCC(zn)


if __name__ == "__main__":
    # b = B(A())
    # b.methodA()
    c = C()
    c.methodC()