from src.analysis_result import AnalysisResult

class ResponseAnalyzer:
    def __init__(self):
        print("ResponseAnalyzer initialized.")

    def analyze(self, response):
        if self._check_for_server_error(response.status_code):
            return AnalysisResult(True, "Server Error", f"Received a 5xx status code: {response.status_code}")
        
        if self._check_for_sql_error(response.text):
            return AnalysisResult(True, "Potential SQL Injection", "Response body contains a common SQL error string.")
        
        return AnalysisResult(False)

    def _check_for_server_error(self, status_code):
        return 500 <= status_code < 600

    def _check_for_sql_error(self, body):
        error_signatures = ["sql syntax", "mysql", "unclosed quotation mark", "odbc", "oracle"]
        body_lower = body.lower()
        return any(sig in body_lower for sig in error_signatures)