import unittest

def longeststr(str):
    if not str:
        return None
    l = str.split(" ")
    major = l[0]
    for i in range(1, len(l)):
        if (len(l[i]) > len(major)):
            major = l[i]
    return major

class TestLongestWord(unittest.TestCase):

    def test_longeststr(self):
        self.assertEqual(None, longeststr(None))
        self.assertEqual("linux", longeststr("linux"))
        self.assertEqual("GNU/Linux", longeststr("Debian GNU/Linux"))
        self.assertEqual("", longeststr("                "))
        self.assertEqual("vizinha", longeststr("   Toda vez que chego em casa a barata da vizinha ta na minha cama"))

if __name__ == '__main__':
    unittest.main()
