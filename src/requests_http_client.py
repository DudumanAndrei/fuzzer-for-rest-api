import requests
from src.http_client import HttpClient
from src.http_response import HttpResponse

class RequestsHttpClient(HttpClient):
    """Concrete implementation using the 'requests' library."""
    def get(self, url, headers=None):
        # Using requests to perform the GET request
        r = requests.get(url, headers=headers)
        return HttpResponse(r.status_code, r.text, r.headers)
        
    def post(self, url, body=None, headers=None):
        # Using requests to perform the POST request
        # We use 'data=body' here to pass the raw string payload
        r = requests.post(url, data=body, headers=headers)
        return HttpResponse(r.status_code, r.text, r.headers)