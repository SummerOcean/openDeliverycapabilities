# -*- coding : utf-8 -*-
"""
@projectname : FDS
@author : Eden
@Time : 2023/8/21
@File : read_yaml.py
@describe 读取yaml文件中的测试数据

"""

import  yaml
from pathlib import Path
def read_file(file_path: Path) :
    with open(file_path,'r',encoding="utf-8") as fp:
        res=yaml.safe_load(fp)
        print(res)
    return res


'''
if __name__=='__main__':
    file_path=Path(__file__).parent.parent.joinpath('data','test_data.yml')
    r=read_file(file_path)
'''