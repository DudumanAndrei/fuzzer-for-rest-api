import requests
from src.http_client import HttpClient
from src.http_response import HttpResponse

class RequestsHttpClient(HttpClient):
    """!
    @brief Concrete implementation using the 'requests' library.
    """
    def get(self, url, headers=None):
        """!
        @brief Performs a GET request using the requests library.
        @param url The target URL.
        @param headers Optional HTTP headers.
        @return An HttpResponse object.
        """
        # Using requests to perform the GET request
        r = requests.get(url, headers=headers)
        return HttpResponse(r.status_code, r.text, r.headers)
        
    def post(self, url, body=None, headers=None):
        """!
        @brief Performs a POST request using the requests library.
        @param url The target URL.
        @param body The request payload.
        @param headers Optional HTTP headers.
        @return An HttpResponse object.
        """
        # Using requests to perform the POST request
        # We use 'data=body' here to pass the raw string payload
        r = requests.post(url, data=body, headers=headers)
        return HttpResponse(r.status_code, r.text, r.headers)

    def put(self, url, body=None, headers=None):
        """!
        @brief Performs a PUT request using the requests library.
        @param url The target URL.
        @param body The request payload.
        @param headers Optional HTTP headers.
        @return An HttpResponse object.
        """
        r = requests.put(url, data=body, headers=headers)
        return HttpResponse(r.status_code, r.text, r.headers)
        
    def delete(self, url, headers=None):
        """!
        @brief Performs a DELETE request using the requests library.
        @param url The target URL.
        @param headers Optional HTTP headers.
        @return An HttpResponse object.
        """
        r = requests.delete(url, headers=headers)
        return HttpResponse(r.status_code, r.text, r.headers)