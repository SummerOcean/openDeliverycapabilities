"""
# @author: 李淑华
# @software: pycharm
# @file_name: Config.py
# @create_time: 2022/3/1 18:29
# @此模块提供：公共路径配置
"""
from os import path
import os
#当前文件路径

CUR_PATH = os.path.realpath(__file__)
print(CUR_PATH)

# 项目根目录
ROOT_PATH = os.path.dirname(os.path.dirname(CUR_PATH))
# 日志报告路径
# LOG_PATH=os.path.join(ROOT_PATH,r'logRecord\\')
# print(LOG_PATH)
#配置读取数据库
db_info={
    "host":"rm-uf6h36245w88g2p16vo.mysql.rds.aliyuncs.com",
    "user":"sys_idms_fds_qc",
    "password":"3xapSx!ksxGVdD7x",
    "database":"idms_fds_qc",
    "port" :3306,
}