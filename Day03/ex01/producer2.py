import json
import logging
import sys
import redis
import random

mess = {
    "metadata": {
        "from": 1023461740,
        "to": 5738456434
    },
    "amount": 10000
}
seq = [1000, -3000, 5000, -1000, -1500, 6000]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # уровень печати
handler = logging.StreamHandler(sys.stdout)  # вывод в терминал
logger.addHandler(handler)

red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)


def stream():
    mess["metadata"]["from"] += 1
    mess["metadata"]["to"] -= 1
    mess["amount"] = random.choice(seq)
    jm = json.dumps(mess)
    logger.info(jm)
    red.publish('msg', jm)


if __name__ == "__main__":
    # while True:
    for x in range(10):
        stream()
