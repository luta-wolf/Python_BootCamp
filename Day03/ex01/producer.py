import json
import redis
from logging import info, error
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def test(red: redis.Redis):
    messages: list = [
        {"metadata": {"from": 1111111111, "to": 2222222222}, "amount": 10000},
        {"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000},
        {"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000},
    ]

    messages = [json.dumps(i) for i in messages]

    for i in messages:
        try:
            red.publish('ex01_topic', i)
            info("Message sent.\n")
        except Exception as e:
            info("Message not sent...")
            error(e)


def main():
    info("Connection to redis started")

    try:
        red = redis.StrictRedis("localhost", 6379, charset='utf-8', decode_responses=True)
        info("Redis connected")
    except Exception as e:
        info("Redis connection error")
        error(e)
    test(red)


if __name__ == "__main__":
    main()
