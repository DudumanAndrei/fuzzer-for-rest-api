class HttpResponse:
    """!
    @brief Represents an HTTP response received from the target.
    """
    def __init__(self, status_code, text, headers):
        """!
        @brief Initializes a new HttpResponse.
        @param status_code The HTTP status code (e.g., 200, 404).
        @param text The response body text.
        @param headers Dictionary of response headers.
        """
        self.status_code = status_code
        self.text = text
        self.headers = headers