import redis
import json
from logging import info, error
import logging
import argparse

logging.basicConfig(level=logging.INFO, format="%(message)s")

bad_guys = []


def listener(red: redis.Redis):
    info("Subscribe to topic")
    try:
        subscriber = red.pubsub()
        subscriber.subscribe("ex01_topic")
    except Exception as e:
        error(e)
        return False
    info("Subscribed")

    info("Listening")
    for msg in subscriber.listen():
        if msg is not None:
            if msg.get('type') == 'message':
                fixer(msg.get('data'))

    return True


def fixer(message: str):
    global bad_guys

    load: dict = json.loads(message)

    sender = load.get('metadata').get('from')
    receiver = load.get('metadata').get('to')
    amount = load.get('amount')

    if amount > 0 and receiver in bad_guys:
        load['metadata']['from'] = receiver
        load['metadata']['to'] = sender

    info(str(load))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", help="list of bad guys' account numbers, length = 10")
    args = parser.parse_args()
    if args.e:
        baddies = args.e
        baddies = baddies.split(',')
        for i in baddies:
            if i.isdigit():
                bad_guys.append(int(i))
            else:
                error("Account should be all numeric \nE.g: 2222222222,444444444")
                exit(1)
    else:
        info("Using default bad guys 2222222222,444444444")
        bad_guys = [2222222222, 4444444444]

    info("Connection to redis started")
    try:
        red = redis.StrictRedis('localhost', 6379, decode_responses=True)
        info("Redis connected")
    except:
        error("Redis connection error")
        exit(1)

    while listener(red):
        pass