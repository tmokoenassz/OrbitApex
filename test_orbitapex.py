# test_orbitapex.py
"""
Tests for OrbitApex module.
"""

import unittest
from orbitapex import OrbitApex

class TestOrbitApex(unittest.TestCase):
    """Test cases for OrbitApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OrbitApex()
        self.assertIsInstance(instance, OrbitApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OrbitApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
