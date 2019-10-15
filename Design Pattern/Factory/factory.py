

class A(object):
    def __init__(self):
        pass

    def print(self):
        print("A")


class B(object):
    def __init__(self):
        pass

    def print(self):
        print("B")


def get(obj=''):
    objs = dict(a=A(), b=B())
    return objs[obj]


a = get('a')
a.print()
a.print()
b = get('b')
b.print()