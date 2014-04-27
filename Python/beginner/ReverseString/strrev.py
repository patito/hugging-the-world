import unittest

def strrev(str):
    if not str:
        return None
    l = len(str) - 1
    x = ""
    for i in range(0, len(str)):
        x += str[l]
        l = l - 1
    return x


class TestSequenceFunctions(unittest.TestCase):

    def test_strrev(self):
        self.assertEqual(None, strrev(None))
        self.assertEqual("xunil", strrev("linux"))

if __name__ == '__main__':
    unittest.main()

