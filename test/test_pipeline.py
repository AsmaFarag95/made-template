import sys
import unittest
import pathlib as pl
import pandas as pd


class TestCase(unittest.TestCase):
    def test_SQLiteFileExists(self):
        directory_path = os.getcwd()
        assert os.path.exists(os.path.dirname(directory_path)+"\project\data\wroclaw_nuremberg_public_transport.sqlite")
         

if __name__ == "__main__":
    if len(sys.argv) > 1:
        TestCase.URL = sys.argv.pop()  
    unittest.main()