import unittest
from unittest.mock import Mock, patch

from github_api import fetch_repo_commit_data


class TestGitHubAPI(unittest.TestCase):

    @patch('github_api.requests.get')
    def test_valid_user(self, mock_get):
        # Mock the response for repo request
        mock_repo_response = Mock()
        mock_repo_response.status_code = 200
        mock_repo_response.json.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'}
        ]

        # Mock the response for commits request
        mock_commit_response = Mock()
        mock_commit_response.status_code = 200
        mock_commit_response.json.return_value = [1, 2, 3]  # 3 commits for example
        
        mock_get.side_effect = [mock_repo_response, mock_commit_response, mock_commit_response]  # as there are two repos

        data = fetch_repo_commit_data("harshaArma")
        expected_data = [('repo1', 3), ('repo2', 3)]
        self.assertEqual(data, expected_data)

    @patch('github_api.requests.get')
    def test_invalid_user(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        data = fetch_repo_commit_data("harshaArma123")
        self.assertEqual(data, "Failed to fetch repositories for harshaArma123")

    @patch('github_api.requests.get')
    def test_empty_user(self, mock_get):
        # Here, you may not necessarily need to mock since the function should raise an error before making a request.
        # However, keeping the mock just ensures no API call is made.
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        self.assertRaises(ValueError, fetch_repo_commit_data, "")

    @patch('github_api.requests.get')
    def test_invalid_user_type(self, mock_get):
        # Same logic as test_empty_user regarding the mock
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        self.assertRaises(TypeError, fetch_repo_commit_data, 123)


if __name__ == '__main__':
    unittest.main()
