from src.analysis_result import AnalysisResult

class ResponseAnalyzer:
    """!
    @brief Analyzes HTTP responses to detect vulnerabilities.
    """
    def __init__(self):
        """!
        @brief Initializes the ResponseAnalyzer.
        """
        print("ResponseAnalyzer initialized.")

    def analyze(self, response, request=None):
        """!
        @brief Analyzes a single HTTP response against vulnerability rules.
        @param response The HttpResponse object to analyze.
        @param request The original FuzzRequest object (optional).
        @return An AnalysisResult object containing the findings.
        """
        if self._check_for_server_error(response.status_code):
            return AnalysisResult(True, "Server Error", f"Received a 5xx status code: {response.status_code}")
        
        if self._check_for_sql_error(response.text):
            return AnalysisResult(True, "Potential SQL Injection", "Response body contains a common SQL error string.")

        if request:
            if "createdb" in request.endpoint and response.status_code == 200:
                return AnalysisResult(True, "Exposed Sensitive Endpoint", "The /createdb endpoint is exposed and returned 200 OK. State-changing or administrative actions should not be accessible without strict authentication and generally not via GET requests.")
            
            sensitive_endpoints = ["/me", "/users/v1", "/users/v1/_debug", "/users/v1/admin", "/users/v1/admin/email", "/users/v1/admin/password", "/books/v1", "/books/v1/book1"]
            if response.status_code in [200, 201, 204] and "Authorization" not in request.headers and request.endpoint in sensitive_endpoints:
                return AnalysisResult(True, "Unauthenticated Access / Missing Auth", f"The endpoint {request.endpoint} returned {response.status_code} for an unauthenticated {request.method} request, potentially leaking sensitive data or allowing unauthorized actions.")
        
        return AnalysisResult(False)

    def _check_for_server_error(self, status_code):
        """!
        @brief Checks if the status code indicates a server error.
        @param status_code The HTTP status code.
        @return True if 5xx error, False otherwise.
        """
        return 500 <= status_code < 600

    def _check_for_sql_error(self, body):
        """!
        @brief Checks if the response body contains SQL error signatures.
        @param body The HTTP response body text.
        @return True if SQL error found, False otherwise.
        """
        error_signatures = ["sql syntax", "mysql", "unclosed quotation mark", "odbc", "oracle"]
        body_lower = body.lower()
        return any(sig in body_lower for sig in error_signatures)