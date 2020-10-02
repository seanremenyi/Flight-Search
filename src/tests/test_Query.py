import unittest
from mock import patch
from Query import Query


class TestQueryClass(unittest.TestCase):
    """test Query class"""
    def test_query_methods(self):
        with patch.object(Query, "__init__", lambda y: None):
            test_object = Query()
            # Error handled if no Flights received
            test_api_call = test_object.api_call()
            self.assertEqual(test_api_call, None)
