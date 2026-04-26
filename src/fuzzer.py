from src.http_client import HttpClient
from src.request_generator import RequestGenerator
from src.response_analyzer import ResponseAnalyzer

class Fuzzer:
    """!
    @brief Main fuzzer class orchestrating the fuzzing process.
    """
    def __init__(self, http_client: HttpClient, request_generator: RequestGenerator, response_analyzer: ResponseAnalyzer):
        """!
        @brief Initializes the Fuzzer with required components.
        @param http_client The HTTP client to send requests.
        @param request_generator The generator for fuzzing requests.
        @param response_analyzer The analyzer for HTTP responses.
        """
        self.http_client = http_client
        self.request_generator = request_generator
        self.response_analyzer = response_analyzer
        
        # Target configuration
        self.target_host = "http://localhost"
        self.target_port = 5001
        self.findings = []
        print(f"Fuzzer initialized for target {self.target_host}:{self.target_port}")

    def run(self):
        """!
        @brief Starts the fuzzing loop, iterating through all generated requests.
        """
        print("Starting fuzzing loop...")
        
        while True:
            fuzz_request = self.request_generator.get_next_request()
            if not fuzz_request:
                break # No more requests
            
            url = f"{self.target_host}:{self.target_port}{fuzz_request.endpoint}"
            print(f"Fuzzing endpoint: {fuzz_request.endpoint}")
            
            if fuzz_request.method == "GET":
                response = self.http_client.get(url, headers=fuzz_request.headers)
            elif fuzz_request.method == "POST":
                response = self.http_client.post(url, body=fuzz_request.body, headers=fuzz_request.headers)
            elif fuzz_request.method == "PUT":
                response = self.http_client.put(url, body=fuzz_request.body, headers=fuzz_request.headers)
            elif fuzz_request.method == "DELETE":
                response = self.http_client.delete(url, headers=fuzz_request.headers)
            else:
                print("Unsupported HTTP method.")
                continue
            
            print(f"  -> Received HTTP Status: {response.status_code}")
            
            result = self.response_analyzer.analyze(response, fuzz_request)
            if result.is_vulnerable:
                print("!!! VULNERABILITY FOUND !!!")
                print(f"Type: {result.vulnerability_type}\nDetails: {result.details}")
                print(f"Request URL: {url}\nRequest Body: {fuzz_request.body}\n")
                self.findings.append({
                    "url": url,
                    "method": fuzz_request.method,
                    "type": result.vulnerability_type,
                    "details": result.details
                })

        print("Fuzzing loop finished.")

    def generate_report(self):
        """!
        @brief Generates a markdown vulnerability report based on findings.
        """
        print("\n--- Generating Vulnerability Report ---")
        report_path = "vulnerability_report.md"
        with open(report_path, "w") as f:
            f.write("# REST API Fuzzer Vulnerability Report\n\n")
            if not self.findings:
                f.write("No vulnerabilities were found during this fuzzing session.\n")
            else:
                f.write(f"**Total Vulnerabilities Found:** {len(self.findings)}\n\n")
                for idx, finding in enumerate(self.findings, 1):
                    f.write(f"## {idx}. {finding['type']}\n")
                    f.write(f"- **Endpoint**: `{finding['method']} {finding['url']}`\n")
                    f.write(f"- **Details**: {finding['details']}\n\n")
        print(f"Report saved to `{report_path}`\n")