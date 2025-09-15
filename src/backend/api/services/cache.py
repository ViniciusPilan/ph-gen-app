# ref: https://redis.io/learn/howtos/quick-start/cheat-sheet
# Used to read/write the current phrase into cache

import os
import redis


REDIS_HOST = os.environ.get("REDIS_HOST", "ph-gen-app-cache")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")


def get_current_phrase() -> str: 
    r = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT
    )
    try:
        current_phrase = r.get('current_phrase').decode("utf-8")
    except:
        current_phrase = None

    r.close()
    return current_phrase


def set_current_phrase(new_phrase: str):
    r = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT
    )
    r.set('current_phrase', new_phrase)
    r.close()


if __name__ == "__main__":
    print(get_current_phrase())
