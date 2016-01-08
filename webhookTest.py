# Webhook Test for GitHub API
# By JJ Berry and Corey Gillen
# Use this for whatever you want!

import unittest
from subprocess import call

class WebhookTestMethods(unittest.TestCase):
    def test_API_root(self):
        self.assertIsNotNone(call(["curl", "https://api.github.com"]))

if __name__ == '__main__':
    unittest.main()