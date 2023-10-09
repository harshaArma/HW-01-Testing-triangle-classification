import unittest

from github_api import fetch_repo_commit_data


class TestGitHubAPI(unittest.TestCase):

    def test_valid_user(self):
        # This is a basic test. For actual tests, you'd want to use a mock to simulate API responses.
        data = fetch_repo_commit_data("harshaArma")
        # Check if you receive data in a list of tuples format
        self.assertTrue(all(isinstance(i, tuple) and len(i) == 2 for i in data))

    def test_invalid_user(self):
        # This is a basic test. For actual tests, you'd want to use a mock to simulate API responses.
        data = fetch_repo_commit_data("harshaArma123")
        # Check if you receive data in a list of tuples format
        self.assertEqual(data, "Failed to fetch repositories for harshaArma123")
    
    def test_empty_user(self):
        # This is a basic test. For actual tests, you'd want to use a mock to simulate API responses.
        self.assertRaises(ValueError, fetch_repo_commit_data, "")
    
    def test_invalid_user_type(self):
        # This is a basic test. For actual tests, you'd want to use a mock to simulate API responses.
        self.assertRaises(TypeError, fetch_repo_commit_data, 123)


if __name__ == '__main__':
    unittest.main()
