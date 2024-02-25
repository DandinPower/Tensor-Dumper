import unittest
import os
from dumper.utils import ensure_dir_exists_by_filename

class TestUtils(unittest.TestCase):
    def test_ensure_dir_exists(self):
        

        # Test when the directory does not exist
        filename = 'test/test.txt'
        dirname = os.path.dirname(filename)
        ensure_dir_exists_by_filename(filename)
        self.assertTrue(os.path.isdir(dirname))

        # Test when the directory already exists
        ensure_dir_exists_by_filename(filename)
        self.assertTrue(os.path.isdir(dirname))

        # Clean up
        os.rmdir(dirname)

if __name__ == '__main__':
    unittest.main()