import unittest
from server.app import app

# server/test_app.py

class TestFlaskConfig(unittest.TestCase):
    def test_debug_mode(self):
        """Test if Flask debug mode is disabled."""
        self.assertFalse(app.debug, "Debug mode should be disabled (debug=False).")

    def test_secret_key(self):
        """Test if SECRET_KEY is defined."""
        self.assertIsNotNone(app.config.get('SECRET_KEY'), "SECRET_KEY should be defined.")

if __name__ == '__main__':
    unittest.main()