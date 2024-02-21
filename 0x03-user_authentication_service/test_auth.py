#!/usr/bin/env python3

import unittest
from auth import _generate_uuid

class TestAuthFunctions(unittest.TestCase):

    def test_generate_uuid(self):
        uuid_result = _generate_uuid()
        self.assertIsInstance(uuid_result, str)
        # You can add more assertions as needed based on your requirements

if __name__ == '__main__':
    unittest.main()
