import unittest
import key
import game


class TestCase(unittest.TestCase):
    def test_00(self):
        key_ = key.Key()
        self.assertEqual(len(key_), 1337)
        self.assertEqual(key_[404], 3)
        self.assertTrue(key_ > 9000)
        self.assertEqual(key_.passphrase, "zax2rulez")
        self.assertEqual(str(key_), "GeneralTsoKeycard")

    def test_01(self):
        game_ = game.Game()
        cheater = game.Cheater
        cooperator = game.Cooperator
        self.assertEqual(cheater.move(self), False)
        self.assertEqual(cooperator.move(self), True)


if __name__ == '__main__':
    unittest.main()
