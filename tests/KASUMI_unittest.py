import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from KASUMI import KASUMI_EncryptBlock

class TestKASUMIEncryption(unittest.TestCase):
    def test_set_1(self):
        key = "2BD6459F82C5B300952C49104881FF48"
        input = "EA024714AD5C4D84"
        output = "DF1F9B251C0BF45F"
        result = KASUMI_EncryptBlock(input, key)
        self.assertEqual(result, output)

    def test_set_2(self):
        key = "8CE33E2CC3C0B5FC1F3DE8A6DC66B1F3"
        input = "D3C5D592327FB11C"
        output = "DE551988CEB2F9B7"
        result = KASUMI_EncryptBlock(input, key)
        self.assertEqual(result, output)

    def test_set_3(self):
        key = "4035C6680AF8C6D1A8FF8667B1714013"
        input = "62A540981BA6F9B7"
        output = "4592B0E78690F71B"
        result = KASUMI_EncryptBlock(input, key)
        self.assertEqual(result, output)

    def test_set_4_iterated_50x(self):
        key = "3A3B39B5C3F2376D69F7D546E5F85D43"
        input = "CA49C1C75771AB0B"
        output = "738BAD4C4A690802"
        result = input
        for _ in range(50):
            result = KASUMI_EncryptBlock(result, key)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
