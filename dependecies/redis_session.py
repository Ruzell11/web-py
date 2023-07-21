import redis

# Redis configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379

def redis_session():
    try:
    # Create a Redis client
        redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    # Ping the Redis server
        response = redis_client.ping()
        if response:
            print("Redis is working and accessible.")
        else:
            print("Redis is not responding.")
    except:
        print("Redis is error")
