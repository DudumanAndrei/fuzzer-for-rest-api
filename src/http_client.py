class HttpClient:
    """!
    @brief Abstract base class/interface for HTTP Clients.
    """
    def get(self, url, headers=None):
        """!
        @brief Performs an HTTP GET request.
        @param url The target URL.
        @param headers Optional HTTP headers.
        @return An HttpResponse object.
        """
        raise NotImplementedError
        
    def post(self, url, body=None, headers=None):
        """!
        @brief Performs an HTTP POST request.
        @param url The target URL.
        @param body The request body payload.
        @param headers Optional HTTP headers.
        @return An HttpResponse object.
        """
        raise NotImplementedError

    def put(self, url, body=None, headers=None):
        """!
        @brief Performs an HTTP PUT request.
        @param url The target URL.
        @param body The request body payload.
        @param headers Optional HTTP headers.
        @return An HttpResponse object.
        """
        raise NotImplementedError
        
    def delete(self, url, headers=None):
        """!
        @brief Performs an HTTP DELETE request.
        @param url The target URL.
        @param headers Optional HTTP headers.
        @return An HttpResponse object.
        """
        raise NotImplementedError