from mock import patch
import unittest
from IataCode import IataCode


class TestIataCodeClass(unittest.TestCase):
    """Test IataCode Class"""
    def test_IataCode_methods(self):
        """initialize the instance to check methods"""
        with patch.object(IataCode, "__init__", lambda x, y: None):

            test_object = IataCode("which city?")

            test_values = test_object.load_iata_codes()
            """Test Json lookup is loaded properly"""
            self.assertEqual(type(test_values), dict)
            self.assertEqual(test_values["Aarhus"][1], "AAR")
            self.assertEqual(test_values["Bintulu"][1], "BTU")
            self.assertEqual(test_values['Whale Cove, NT'][1], "YXN")
