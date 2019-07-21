from unittest import TestCase

from starter_app.helper.Greeter import Greeter


class TestGreeter(TestCase):
    def test_greet(self):

        world_greeter = Greeter('World')

        self.assertEqual(world_greeter.greet(), 'Hello World')
