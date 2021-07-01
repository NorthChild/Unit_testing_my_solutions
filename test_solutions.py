import unittest
import solutions


# ARE THEY ANAGRAMS TEST
class testSolutions(unittest.TestCase):

    def test_anagramCheck(self):
        self.assertTrue(solutions.anagramCheck('funeral', 'real fun'))
        self.assertFalse(solutions.anagramCheck('fun time', 'raul tim'))
        self.assertTrue(solutions.anagramCheck('astronomer', 'moonstarer'))
        self.assertFalse(solutions.anagramCheck('flat earth', 'non sense'))








        
        

if __name__ == "__main__":
    unittest.main()
