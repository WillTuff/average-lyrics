import unittest

class testProgram(unittest.TestCase):

    def setUp(self):
        self.artistIds = ["A1", "A2", "A3"]

    def test_checkInput(self):
        self.assertEqual(self.artistIds[0], "A1")

if __name__ == '__main__':
    unittest.main()