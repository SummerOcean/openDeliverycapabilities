'''
连接数据库
'''
import pymysql
import pytest

from CONFIG.configPath import db_info
#写在字典里

'''
db_info={
    "host":"qc-rds.can-dao.com",
    "user":"sys_idms_fds_qc",
    "password":"3xapSx!ksxGVdD7x",
    "database":"idms_fds_qc",
    "port" :3306,
}
'''

class ConnectDb():
    def __init__(self,db_info):
        # 初始化，连上数据库
        self.db = pymysql.connect(
            **db_info,
            cursorclass=pymysql.cursors.DictCursor,
        )
        #初始化创建游标
        self.cur=self.db.cursor()

    #查询

    def select_sql(self,sql):
        try:
            self.cur.execute(sql)
            result=self.cur.fetchall()
            return result
        except:
            print('数据库查询sql出现异常')
    #执行
    def excute_sql(self,sql):
        try:
            self.cur.execute(sql)
            self.db.commit()
        except:
            #出现异常，回滚机制
            self.db.rollback()
            print('数据库查询sql出现异常')

    def close(self):
        #关闭连接
        self.db.close()

