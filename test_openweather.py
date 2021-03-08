import unittest

import openweather


class OpenWeatherTestCase(unittest.TestCase):
    """Tests for openweather.py."""

    # def setUp(self):
    #     """Call functions here, and test elements separately."""

    #     self.r = openweather.get_weather_results(self, self)

    def test_api_status_code(self):
        """Test that we get a valid response."""
        # self.assertEqual(self.r.status_code, 200)
        # self.assertEqual(self.r.status_code, 200)
        self.assertTrue(r.status_code == 200)


if __name__ == '__main__':
    unittest.main()
