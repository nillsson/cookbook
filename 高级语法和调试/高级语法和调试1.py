#zip
l1 = [1,3,141,131,12]
l2 = [31,1341,5451,1123,1]
z = zip(l1,l2)
print(type(z))
print(z)
for i in z:
    print(i)

l1 = ['yiyi',"mimi","dodo"]
l2 = [12,432,213]
z = zip(l1,l2)
l4 = [i for i in z]
print(l4)

em = enumerate(l1)
l3 = [i for i in em]

em2 = enumerate(l1,start=100)
l4 = [i for i in em2]
print(l4)

#collections
import collections
Point = collections.namedtuple("point",["x","y"])
p = Point(11,12)
print(p)
print(p[0])

Circle = collections.namedtuple("Circle",["x","y","r"])
c = Circle(10,2,3)
print(c)

from collections import deque
q = deque(["a","c","d"])

q.append("x")
print(q)

q.appendleft("y")
print(q)



#defaultdict
d1 = {"one":1,"two":2}
print(d1["one"])

from collections import defaultdict
func = lambda: "yiyi"
d2 = defaultdict(func)
d2["one"], d2["two"]= 1, 2
print(d2["four"])

from collections import Counter
#为什么下面结果不把dad...作为键值，而是以其中每一个字母作为键值
#需要括号里内容为可迭代
c = Counter("dadfdsrewqrqewbvaadsafavc afafdadfas")
print(c)

s = ["mimi","dodo","yiyi"]
t = Counter(s)
print(t)




