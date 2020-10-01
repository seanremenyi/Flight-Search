from unittest.mock import patch
import unittest
from IataCode import IataCode
from mock import patch

class TestIataCodeClass(unittest.TestCase):
    def test_IataCode_methods(self):
        with patch.object(IataCode, "__init__", lambda x, y: None):
            test_object=IataCode("what")
        
            test_values = test_object.load_iata_codes()
        
            self.assertEqual(type(test_values), dict)
            self.assertEqual(test_values["Aarhus"][1], "AAR")
            self.assertEqual(test_values["Bintulu"][1], "BTU")
            self.assertEqual(test_values['Whale Cove, NT'][1], "YXN")

            test_options = test_object.multiple_options("montreal")
            print(test_options) 
    
    # def test_init(self):

    #     with patch.object(IataCode, "__init__", lambda x, y: None):
    #         c=IataCode("what")
    #         print(c.__dict__)

  