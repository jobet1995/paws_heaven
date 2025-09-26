from django.test import TestCase

class BasicTest(TestCase):
    def test_basic(self):
        """Basic test to verify test runner is working."""
        self.assertTrue(True)

    def test_homepage(self):
        """Test that homepage loads successfully."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
