# test_bootloader.py
"""
Tests for BootLoader module.
"""

import unittest
from bootloader import BootLoader

class TestBootLoader(unittest.TestCase):
    """Test cases for BootLoader class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BootLoader()
        self.assertIsInstance(instance, BootLoader)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BootLoader()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
