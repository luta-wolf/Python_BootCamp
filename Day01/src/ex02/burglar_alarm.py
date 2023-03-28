def decorator_function(func: any) -> any:
    def wrapper(purse: dict):
        print('SQUEAK')
        return func(purse)

    return wrapper


@decorator_function
def add_ingot(purse: dict) -> dict:
    purse2: dict = purse.copy()
    if "gold_ingots" in purse2:
        purse2["gold_ingots"] += 1
    else:
        purse2["gold_ingots"] = 1
    return purse2


@decorator_function
def get_ingot(purse: dict) -> dict:
    return purse.copy()


@decorator_function
def empty(purse: dict) -> dict:
    purse2: dict = purse.copy()
    purse2.clear()
    return purse2


if __name__ == "__main__":
    d: dict[str, int] = {'gold_ingots': 10, 'silver_ingots': 13, 'copper_ingots': 10}

    print(add_ingot(d))
    print(get_ingot(d))
    print(empty(d))
