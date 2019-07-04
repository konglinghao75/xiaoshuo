# -*- coding: utf-8 -*-
"""
使用文档：

本文件是Redis连接的全局单例模式，

>>> XzxRedis().r
>>> Redis<ConnectionPool<Connection<host=140.143.206.157,port=6379,db=15>>>

XzxRedis().r返回一个 redis 数据库的链接池对象

@author: zpj

"""

import redis

########Redis 数据库  全局设置#########

REDIS_HOST = '140.143.206.157'
REDIS_PROT = '6379'
REDIS_PSWD = '1'
REDIS_DBNUM = '15'

######################################

class XzxRedis:

    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        if not XzxRedis.init_flag:
            
            print("初始化XzxRedis数据库")
            
            pool = redis.ConnectionPool(
                    
                    host = REDIS_HOST, 
                    port= REDIS_PROT, 
                    password = REDIS_PSWD, 
                    db = REDIS_DBNUM, 
                    decode_responses = True,
                                        )
            
            self.r = redis.StrictRedis(connection_pool=pool)
            
            XzxRedis.init_flag = True



if __name__ == '__main__':
    
    pass
    
#    x = XzxRedis()
#    y = XzxRedis()
    
















