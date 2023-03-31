from gaining_access import Key


def main():
    key = Key()
    print(key.passphrase)
    print(key.__str__())
    print(key.__len__())
    print(key > 9000)
    print(key[404])
    return key


def test_attrib(key):
    if key.passphrase == "zax2rulez":
        print('Test attrib Ok')
    else:
        print('Test attrib Fail')


def test_str(key):
    if key.__str__() == 'GeneralTsoKeycard':
        print('Test str Ok')
    else:
        print('Test str Fail')


def test_len(key):
    if key.__len__() == 1337:
        print('Test len Ok')
    else:
        print('Test len Fail')


def test_gt(key):
    if key > 9000:
        print('Test gt Ok')
    else:
        print('Test gt Fail')


def test_getitem(key):
    if key[0] == 3:
        print('Test getitem Ok')
    else:
        print('Test getitem Fail')


if __name__ == "__main__":
    key = main()
    test_attrib(key)
    test_str(key)
    test_len(key)
    test_gt(key)
    test_getitem(key)
