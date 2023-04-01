# Магические методы

class Key:
    passphrase = "zax2rulez"

    def __str__(self):
        return "GeneralTsoKeycard"

    def __len__(self) -> int:
        return 1337

    def __getitem__(self, key):
        return 3

    def __gt__(self, other):
        return True if other <= 9000 else False


# Тесты
key = Key()
assert len(key) == 1337
assert key[404] == 3
assert key > 9000
assert key.passphrase == "zax2rulez"
assert str(key) == "GeneralTsoKeycard"
