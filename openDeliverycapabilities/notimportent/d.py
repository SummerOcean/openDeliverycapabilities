'''
步骤不一样的不适合参数化
'''
import pytest


@pytest.mark.parametrize()
def test():
    print()

#多个参数 list 、dict容器存多个变量
@pytest.mark.parametrize("test_input,except",[[{"user":"test","pwd":"123"},"success"],])
