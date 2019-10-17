import time, gc
from memory_profiler import profile


@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    time.sleep(10)
    del b
    del a
    print("+++++++++")


@profile
def my_func2():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    b.append(a)
    a.append(b)
    time.sleep(10)
    del b
    del a
    gc.collect()
    print("+++++++++")

@profile
def my_func3():
    a = []
    for i in range(10):
        a.append([1] * (10 ** 6))

    for element in a:
        print(element)

        gc.collect()
    print("+++++++++")

@profile
def my_func4():
    a = {
        "a": [1] * (10 ** 6),
        "b": [2] * (2 * 10 ** 7)
    }
    b = a.get("b")
    del b
    del a
    print("+++++++++")

def my_func5():
    my_func4()

class myClass():
    def __init__(self):
        self.a = 1

    @profile
    def getA(self):
        return self.a

if __name__ == '__main__':
    my_func5()
