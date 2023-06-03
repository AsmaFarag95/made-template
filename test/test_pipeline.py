import sys
import unittest
import pathlib as pl

class TestCase(unittest.TestCase):
    def test_SQLiteFileExists(self):
        filepath = pl.Path("project/data/wroclaw_nuremberg_public_transport.sqlite")
        self.assertEquals((str(filepath), filepath.is_file()), (str(filepath), True))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        TestCase.URL = sys.argv.pop()
    unittest.main()