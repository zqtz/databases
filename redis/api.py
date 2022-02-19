from flask import Flask, g

from db import RedisClient

# __all__ = ['app']#如何理解

app = Flask(__name__)


def get_conn():
    """
    Opens a new redis connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'redis_client'):
        g.redis_client = RedisClient()
    return g.redis_client


@app.route('/')
def index():
    return 'Welcome to Proxy Pool System'


@app.route('/get')
def get_proxy():
    """
    Get a proxy
    """
    conn = get_conn()
    return conn.pop()

if __name__ == '__main__':
    app.run()

