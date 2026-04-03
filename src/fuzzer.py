from src.http_client import HttpClient
from src.request_generator import RequestGenerator
from src.response_analyzer import ResponseAnalyzer

class Fuzzer:
    def __init__(self, http_client: HttpClient, request_generator: RequestGenerator, response_analyzer: ResponseAnalyzer):
        self.http_client = http_client
        self.request_generator = request_generator
        self.response_analyzer = response_analyzer
        
        # Target configuration
        self.target_host = "http://localhost"
        self.target_port = 5001
        print(f"Fuzzer initialized for target {self.target_host}:{self.target_port}")

    def run(self):
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
            else:
                print("Unsupported HTTP method.")
                continue
            
            print(f"  -> Received HTTP Status: {response.status_code}")
            
            result = self.response_analyzer.analyze(response)
            if result.is_vulnerable:
                print("!!! VULNERABILITY FOUND !!!")
                print(f"Type: {result.vulnerability_type}\nDetails: {result.details}")
                print(f"Request URL: {url}\nRequest Body: {fuzz_request.body}\n")

        print("Fuzzing loop finished.")