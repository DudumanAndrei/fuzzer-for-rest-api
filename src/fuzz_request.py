class FuzzRequest:
    """!
    @brief Represents an HTTP request used for fuzzing.
    """
    def __init__(self, method, endpoint, headers=None, body=""):
        """!
        @brief Initializes a new FuzzRequest.
        @param method The HTTP method (e.g., GET, POST).
        @param endpoint The API endpoint path.
        @param headers Optional dictionary of HTTP headers.
        @param body Optional HTTP request body payload.
        """
        self.method = method
        self.endpoint = endpoint
        self.headers = headers if headers is not None else {}
        self.body = body