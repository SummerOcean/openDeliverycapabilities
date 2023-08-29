
def funx():
    return '12'

def fun(x):
    print(f"打印引用的函数对象: {x()}")
    return "hello"

x=funx

print(fun(x))