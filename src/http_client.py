class HttpClient:
    """Abstract base class/interface for HTTP Clients."""
    def get(self, url, headers=None):
        raise NotImplementedError
        
    def post(self, url, body=None, headers=None):
        raise NotImplementedError