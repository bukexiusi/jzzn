class a():
    def __init__(self):
        self.level = 1
        print('a born,id:%s' % str(hex(id(self))))


class b():
    def __init__(self, aObject):
        self.level = 2
        print('b born,id:%s' % str(hex(id(self))))


class c():
    def __init__(self, bObject):
        self.level = 3
        print('c born,id:%s' % str(hex(id(self))))


class d():
    def __init__(self, cObject):
        self.level = 4
        print('c born,id:%s' % str(hex(id(self))))


if __name__ == "__main__":
    ao = a()
    bo = b(ao)
    co = c(bo)
