import unittest
import Lesson14

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Lesson14.add(1, 2), 3)


    def test_sub(self):
        self.assertEqual(Lesson14.sub(4, 2), 2)


    def test_mul(self):
        self.assertEqual(Lesson14.mul(5, 2), 10)


    def test_div(self):
        self.assertEqual(Lesson14.div(8, 4), 2)

if __name__== "__main__":
    unittest.main()
