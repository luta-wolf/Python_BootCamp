import json
import logging
import sys
import redis  # база данных в памяти

red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # уровень печати
handler = logging.StreamHandler(sys.stdout)  # писать на экран
logger.addHandler(handler)


def reciever():
    b = [int(s) for s in sys.argv[2].split(',')]
    sub = red.pubsub()
    sub.subscribe('msg')
    for message in sub.listen():
        str_a = message["data"]
        if type(str_a) is str:
            dic_a = json.loads(str_a)
            dic_to = dic_a["metadata"]["to"]
            dic_amount = dic_a["amount"]
            for bad_gays in b:
                if bad_gays == dic_to and dic_amount > 0:
                    temp = dic_a["metadata"]["from"]
                    dic_a["metadata"]["from"] = dic_to
                    dic_a["metadata"]["to"] = temp
                    print("Opa!", bad_gays, dic_to)
            logger.info(dic_a)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "-e":
        reciever()
    else:
        print("need more args or flag error")
