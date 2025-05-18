import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from KASUMI import KASUMI_EncryptBlock

def tests_kasumi():
    tests_vectors = [
        {
            "name": "Test Set 1",
            "key": "2BD6459F82C5B300952C49104881FF48",
            "input": "EA024714AD5C4D84",
            "output": "DF1F9B251C0BF45F"
        },
        {
            "name": "Test Set 2",
            "key": "8CE33E2CC3C0B5FC1F3DE8A6DC66B1F3",
            "input": "D3C5D592327FB11C",
            "output": "DE551988CEB2F9B7"
        },
        {
            "name": "Test Set 3",
            "key": "4035C6680AF8C6D1A8FF8667B1714013",
            "input": "62A540981BA6F9B7",
            "output": "4592B0E78690F71B"
        },
        {
            "name": "Test Set 4 (Iterated 50x)",
            "key": "3A3B39B5C3F2376D69F7D546E5F85D43",
            "input": "CA49C1C75771AB0B",
            "output": "738BAD4C4A690802",
            "iterations": 50
        }
    ]

    passed = failed = 0

    for vector in tests_vectors:
        key_int = int(vector["key"], 16)
        input_int = int(vector["input"], 16)
        output_int = int(vector["output"], 16)

        result_int = input_int
        iterations = vector.get("iterations", 1)

        for _ in range(iterations):
            result_int = KASUMI_EncryptBlock(result_int, key_int)

        try:
          assert result_int == output_int
          print(f"{vector['name']} - PASSED")
          passed += 1
        except AssertionError as e:
            print(f"{vector['name']} - FAILED: got {hex(result_int)[2:].upper()}, expected {hex(output_int)[2:].upper()}")
            failed += 1

    print("\n==== Test Summary ====")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if failed > 0:
        exit(1)

if __name__ == "__main__":
    tests_kasumi()
