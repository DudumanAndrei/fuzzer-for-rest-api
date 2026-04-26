from src.analysis_result import AnalysisResult

class ResponseAnalyzer:
    def __init__(self):
        print("ResponseAnalyzer initialized.")

    def analyze(self, response, request=None):
        if self._check_for_server_error(response.status_code):
            return AnalysisResult(True, "Server Error", f"Received a 5xx status code: {response.status_code}")
        
        if self._check_for_sql_error(response.text):
            return AnalysisResult(True, "Potential SQL Injection", "Response body contains a common SQL error string.")

        if request:
            if "createdb" in request.endpoint and response.status_code == 200:
                return AnalysisResult(True, "Exposed Sensitive Endpoint", "The /createdb endpoint is exposed and returned 200 OK. State-changing or administrative actions should not be accessible without strict authentication and generally not via GET requests.")
            
            sensitive_endpoints = ["/me", "/users/v1", "/users/v1/_debug", "/users/v1/admin", "/books/v1", "/books/v1/book1"]
            if request.method == "GET" and response.status_code == 200 and "Authorization" not in request.headers and request.endpoint in sensitive_endpoints:
                return AnalysisResult(True, "Unauthenticated Access / Missing Auth", f"The endpoint {request.endpoint} returned 200 OK for an unauthenticated GET request, potentially leaking sensitive data.")
        
        return AnalysisResult(False)

    def _check_for_server_error(self, status_code):
        return 500 <= status_code < 600

    def _check_for_sql_error(self, body):
        error_signatures = ["sql syntax", "mysql", "unclosed quotation mark", "odbc", "oracle"]
        body_lower = body.lower()
        return any(sig in body_lower for sig in error_signatures)