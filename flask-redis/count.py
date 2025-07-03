import os
from flask import Flask
import redis

app = Flask(__name__)

#Initialises redis key-value store
redis_host = os.getenv('REDIS_HOST')
redis_port=os.getenv('REDIS_PORT')
client = redis.Redis(host=redis_host , port=redis_port)

@app.route('/')
def hello_world():
    return 'Mustafa Flask-Redis Containers challenge!'

@app.route('/count')
def count_visits():
    #Increments visitor count by one (initialises key 'visitor_count' with value 0 as it didn't exist prior)
    count = client.incr('visitor_count')
    return f'The website visit count is: {count}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)