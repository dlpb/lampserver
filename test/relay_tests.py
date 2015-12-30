import unittest


class RelayBoard:
    def blah(self):
        return False


# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        relay = RelayBoard()
        self.assertFalse(relay.blah())


def main():
    unittest.main()

if __name__ == '__main__':
    main()