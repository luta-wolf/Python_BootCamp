def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    purse2: dict[str, int] = purse.copy()
    if "gold_ingots" in purse2:
        purse2["gold_ingots"] += 1
    else:
        purse2["gold_ingots"] = 1
    return purse2


def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    purse2: dict[str, int] = purse.copy()
    if "gold_ingots" in purse2 and purse2["gold_ingots"] > 0:
        purse2["gold_ingots"] -= 1
    return purse2


def empty(purse: dict[str, int]) -> dict[str, int]:
    purse2: dict[str, int] = purse.copy()
    purse2.clear()
    return purse2


if __name__ == "__main__":
    d: dict[str, int] = {'gold_ingots': 10, 'silver_ingots': 13, 'copper_ingots': 10}
    # d: dict[str, int] = {'silver_ingots': 13, 'copper_ingots': 10}

    print(add_ingot(d))
    print(get_ingot(d))
    print(empty(d))

    print(add_ingot(get_ingot(add_ingot(empty(d)))))
