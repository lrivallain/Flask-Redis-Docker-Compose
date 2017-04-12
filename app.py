from flask import Flask
from redis import Redis
import os, socket
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    host = socket.gethostname()
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.\n\nHostname is : %s' % (redis.get('hits'), host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
