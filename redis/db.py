import redis
# from proxypool.error import PoolEmptyError
HOST = 'localhost'
PORT = 6379
# PASSWORD = ''

# 面试经常问的问题
'https://github.com/JiangRRRen/Redis-study/blob/master/%E9%9D%A2%E8%AF%95%E7%9B%B8%E5%85%B3/Redis%E9%9D%A2%E8%AF%95%E5%B8%B8%E8%A7%81%E5%9F%BA%E6%9C%AC%E9%97%AE%E9%A2%98.md'

class RedisClient(object):
    def __init__(self, host=HOST, port=PORT):
        self._db = redis.Redis(host=host, port=port)

    def get(self, count=1):
        """
        get proxies from redis
        """
        proxies = self._db.lrange("proxies", 0, count - 1)
        self._db.ltrim("proxies", count, -1)
        return proxies

    def pop(self):
        """
        get proxy from right.
        """
        return self._db.rpop("proxies").decode('utf-8')

if __name__ == '__main__':
    conn = RedisClient()
    print(conn.pop())
