import unittest

from github_api import fetch_repo_commit_data


class TestGitHubAPI(unittest.TestCase):

    def test_valid_user(self):
        # This is a basic test. For actual tests, you'd want to use a mock to simulate API responses.
        data = fetch_repo_commit_data("harshaArma")
        # Check if you receive data in a list of tuples format
        self.assertTrue(all(isinstance(i, tuple) and len(i) == 2 for i in data))

if __name__ == '__main__':
    unittest.main()
