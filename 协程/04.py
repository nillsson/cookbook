# yield from案例
def gen():
    for c in "AB":
        yield c

# list直接用生成器作为参数
print(list(gen()))

def gen_new():
    yield from "GUGUDAY"

print(list(gen_new()))

