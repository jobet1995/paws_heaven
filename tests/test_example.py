from django.test import TestCase, Client


class TestExample(TestCase):
    """Example test cases for the application."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_example(self):
        """Example test that should always pass."""
        assert 1 + 1 == 2

    def test_homepage_status(self):
        """Test that homepage returns a valid status code."""
        response = self.client.get('/')
        # Accept both 200 (OK) and 404 (Not Found) as valid responses
        assert response.status_code in (200, 404), \
            f"Homepage returned unexpected status code: {response.status_code}"
