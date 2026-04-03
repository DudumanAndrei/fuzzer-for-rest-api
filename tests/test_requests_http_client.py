import unittest
from unittest.mock import patch, MagicMock
from src.requests_http_client import RequestsHttpClient
from src.http_response import HttpResponse

class TestRequestsHttpClient(unittest.TestCase):
    """!
    @brief Unit tests for the RequestsHttpClient class.
    
    This test suite uses the unittest framework and the mock library
    to simulate HTTP requests and verify the behavior of the RequestsHttpClient.
    """

    def setUp(self):
        """!
        @brief Set up the HTTP client instance before each test.
        """
        self.client = RequestsHttpClient()

    @patch('src.requests_http_client.requests.get')
    def test_get_request_success(self, mock_get):
        """!
        @brief Tests a successful GET request.
        
        @param mock_get Mocked requests.get method to prevent actual network calls.
        """
        # Arrange: Setup our mock to simulate a successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"users": []}'
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_get.return_value = mock_response

        # Act: Execute the method we are testing
        response = self.client.get('http://localhost:5001/users/v1', headers={'Authorization': 'Bearer test-token'})

        # Assert: Verify the behavior and the result
        mock_get.assert_called_once_with('http://localhost:5001/users/v1', headers={'Authorization': 'Bearer test-token'})
        self.assertIsInstance(response, HttpResponse)

    @patch('src.requests_http_client.requests.post')
    def test_post_request_success(self, mock_post):
        """!
        @brief Tests a successful POST request.
        
        @param mock_post Mocked requests.post method to prevent actual network calls.
        """
        # Arrange: Setup our mock for a POST request
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.text = '{"message": "User created"}'
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_post.return_value = mock_response

        # Act
        response = self.client.post('http://localhost:5001/users/v1', body='{"username": "admin"}')

        # Assert
        mock_post.assert_called_once_with('http://localhost:5001/users/v1', data='{"username": "admin"}', headers=None)
        self.assertIsInstance(response, HttpResponse)
