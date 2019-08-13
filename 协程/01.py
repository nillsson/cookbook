from collections import Iterable
from collections import Iterator

print(isinstance('abc', Iterator))
print(isinstance(iter('abc'), Iterator))
print(isinstance(iter(iter('abc')), Iterable))


def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 2

g = odd()
print(type(g))

one = next(g)
print(one)
two = next(g)
print(two)
print("下一个就会出异常")
three = next(g)
print(three)



