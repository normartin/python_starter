from unittest import TestCase

from starter_app.colorize.colorize import colorize


class TestColorize(TestCase):
    def test_colorize_should_include_original_string(self):
        message = "some"

        colorized_message = colorize(message)

        self.assertIn(message, colorized_message)
