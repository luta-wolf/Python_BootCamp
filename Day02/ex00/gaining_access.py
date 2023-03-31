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
