import franzpy
import unittest

class Test_make_compliment(unittest.TestCase):

  def test_make_compliment(self):
    self.assertIsInstance(franzpy.make_compliment(), str)