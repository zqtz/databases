import redis
import sys
sys.path.append('E:\\code\\code_spider\\spider_three_month\\需要技能\数据库\\redis\\userful_command\\setting.py')
from setting import HOST,PORT
import re

class RedisClient(object):
    def __init__(self):
        self._db = redis.Redis(host=HOST,port=PORT)

    def get(self,count=1):
        # 移除并返回最左侧代理
        # proxy = self._db.lrange('proxies',count-1,0)
        # self._db.ltrim('proxy',count,-1)
        # or
        proxy = self._db.lpop('proxies')
        return proxy

    def put(self,proxy):
        self._db.rpush('proxy',proxy)

    def pop(self):
        try:
            proxy = self._db.rpop('proxies')
            return proxy
        except:
            print('PoolEmptyError')

    def get_len(self):
        len = self._db.llen('proxies')
        return len

    def flush(self):
        self._db.flushdb()

if __name__ == '__main__':
    client = RedisClient()
    print(client.get())

db = redis.Redis(host='localhost',port=6379)
# result = db.lrange('proxies',0,0)[0]
# print(result)
db.rpush('456','106.54.128.253:999')

