import time

import pytest
from jsonpath import jsonpath
from API.createStore import cerate_deliveryStore
from COMMON.read_yaml import read_file
from pathlib import Path



file_path = Path(__file__).parent.parent.joinpath('data', 'test_data.yml')
print(file_path)
test_data = read_file(file_path)
print(test_data)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

@pytest.mark.parametrize("input,expected",test_data['test_add_store'])
def test_addStore(input,expected):
    '''创建门店成功'''
    c_as=cerate_deliveryStore(**input)
    print("创建门店成功"+c_as.text)
    assert c_as.json()['msg']==expected['msg']
    assert c_as.json()['status'] == expected['status']
    #assert c_as.json()['status'] ==
    