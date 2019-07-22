from unittest import TestCase
from unittest.mock import patch

from starter_app.say_hello import say_hello


class TestSayHello(TestCase):
    def test_say_hello_can_be_called(self):
        say_hello()

    @patch('builtins.print')
    def test_prints_greeting_to_console(self, mocked_print):
        say_hello()

        console_output = "".join(mocked_print.call_args[0])

        self.assertIn('Hello', console_output)
