from flask import Flask
import redis

app = Flask(__name__)

#Initialises redis key-value store
client = redis.Redis(host='localhost', port='6379')

@app.route('/')
def hello_world():
    return 'Mustafa Flask-Redis Containers challenge!'

@app.route('/count')
def count_visits():
    #Increments visitor count by one (initialises key 'visitor_count' with value 0 as it didn't exist prior)
    client.incr('visitor_count')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)