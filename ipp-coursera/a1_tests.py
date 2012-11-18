'''
Created on 18/10/2012

@author: repli
'''
from a1 import name_to_number, number_to_name
from numpy.testing.utils import assert_equal
import unittest








class Test(unittest.TestCase):


    def test_name_to_number(self):
        assert_equal(0, name_to_number('rock'))
        assert_equal(1, name_to_number('Spock'))
        assert_equal(2, name_to_number('paper'))
        assert_equal(3, name_to_number('lizard'))
        assert_equal(4, name_to_number('scissors'))


    def test_number_to_name(self):
        assert_equal('rock', number_to_name(0))
        assert_equal('Spock', number_to_name(1))
        assert_equal('paper', number_to_name(2))
        assert_equal('lizard', number_to_name(3))
        assert_equal('scissors', number_to_name(4))
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()