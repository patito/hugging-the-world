import unittest

def isDivisible(number, divisible):

	if (number <= 0) or (divisible <= 0):
		return False

	while (number > 0):
		number -= divisible
		if (number == 0):
			return True
	return False

def doIt():
	for i in range(1, 101):
		div3 = isDivisible(i, 3)
		div5 = isDivisible(i, 5)
		if (div3 == True) and (div5 == True):
			print str(i) + " Kitkat"
		elif (div3 == True):
			print str(i) + " Kit"
		elif (div5 == True):
			print str(i) + " kat"

class TestDivisible(unittest.TestCase):

    def test_divisible(self):
        self.assertEqual(False, isDivisible(2, -1))
        self.assertEqual(False, isDivisible(2, 0))
        self.assertEqual(False, isDivisible(0, 0))
        self.assertEqual(False, isDivisible(-2, -1))
        self.assertEqual(False, isDivisible(-2, -1))
        self.assertEqual(False, isDivisible(-2, 4))
        self.assertEqual(False, isDivisible(-2, 8))
        self.assertEqual(False, isDivisible(2, 8))
        self.assertEqual(True, isDivisible(5, 5))
        self.assertEqual(True, isDivisible(100, 5))
        self.assertEqual(True, isDivisible(33, 3))


if __name__ == '__main__':
	doIt()
	unittest.main()

