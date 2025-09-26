from django.test import TestCase

class BasicTest(TestCase):
    def test_basic(self):
        """Basic test to verify test runner is working."""
        self.assertTrue(True)

    def test_homepage_not_500(self):
        """Test that homepage doesn't return server error (500)."""
        response = self.client.get('/')
        self.assertNotEqual(response.status_code, 500, "Homepage returned server error (500)")
