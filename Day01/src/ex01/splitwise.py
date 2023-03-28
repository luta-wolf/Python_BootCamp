from typing import Any

from functional_purse import add_ingot


def split_booty(*wallets: object) -> tuple[Any, Any, Any]:
    lst: list = []
    s: int = 0
    for i in wallets:
        if i.get('gold_ingots'):
            s += i['gold_ingots']
    for i in range(3):
        res: int = int(s / (3 - i))
        s = s - res
        ingot: dict = {}
        for _ in range(res):
            ingot = add_ingot(ingot)
        lst.append(ingot)
    return lst[0], lst[1], lst[2]


if __name__ == '__main__':
    d: dict[str, int] = {'gold_ingots': 5}
    d2: dict[str, int] = {'gold_ingots': 12}
    d3: dict[str, int] = {'gold_ingots': 2}
    d4: dict[str, int] = {"apples": 10}
    d5: dict[str, int] = {'gold_ingots': 0}
    d6: dict[str, int] = {'gold_ingots': 3}

    print(split_booty(d, d2, d3, d4, d5, d6))
