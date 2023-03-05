import unittest
from ..src.conversations.conversation_resources import ConversationResources


class TestConversationResources(unittest.TestCase):
    def test_hello_world(self):
        resources = ConversationResources()
        get = resources.get()
        self.assertEqual(get, {'hi': 'hi'})  # add assertion here


if __name__ == '__main__':
    unittest.main()
