import random
from src.fuzz_request import FuzzRequest

class RequestGenerator:
    def __init__(self):
        self.endpoints = ["/users/v1", "/books/v1", "/createdb"]
        self.current_endpoint_index = 0
        self.fuzzing_case = 0
        print(f"RequestGenerator initialized with {len(self.endpoints)} endpoints.")

    def get_next_request(self):
        if self.current_endpoint_index >= len(self.endpoints):
            return None # We've fuzzed all endpoints
        
        endpoint = self.endpoints[self.current_endpoint_index]
        
        if self.fuzzing_case == 0:
            # Case 0: GET request
            req = FuzzRequest("GET", endpoint)
            req.headers["User-Agent"] = "Fuzzer/0.1"
            req.headers["X-Custom-Fuzz-Header"] = self._generate_fuzzed_payload()
            self.fuzzing_case += 1
            return req
        else:
            # Case 1: POST request
            payload = self._generate_fuzzed_payload()
            req = FuzzRequest("POST", endpoint)
            req.body = f'{{"username":"{payload}", "password":"\' OR 1=1 --"}}'
            req.headers["Content-Type"] = "application/json"
            self.fuzzing_case = 0
            self.current_endpoint_index += 1
            return req

    def _generate_fuzzed_payload(self):
        payloads = [
            "'", "\"", "`", "<script>alert(1)</script>", "admin'--", "OR 1=1",
            "A" * 1024 # Buffer overflow attempt
        ]
        return random.choice(payloads)