from redis import StrictRedis
from dotenv import load_dotenv
from os import getenv

load_dotenv()

redisDB = StrictRedis.from_url(getenv("REDIS_URL"))

async def db_con_check():
    try:
        redisDB.ping()
        print("Connected to Redis database!")
    except:
        print("Connection to Redis database failed!")
