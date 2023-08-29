
def fun_x():

    x = []

    def func(a):
        x.append(a)

    return func()


    func(a=1)
    func(a=2)
    func(a=3)
    print(x)

x = [333]
print(x)
