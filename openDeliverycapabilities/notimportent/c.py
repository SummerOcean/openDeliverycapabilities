import time
#写公共函数，计算运行时间
def run_time(fun):

        def inner():
            t1 = time.time()
            print(f"运行之前的时间:  {t1}")
            res = fun()  #写一个计算的函数
            t2 = time.time()
            print(f"运行之后的时间:   {t2}")
            print(t2 - t1)
            return res
        return inner()



@run_time
def fun_d():
    time.sleep(2)







