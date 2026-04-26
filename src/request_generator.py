import random
from src.fuzz_request import FuzzRequest

class RequestGenerator:
    """!
    @brief Generates fuzzing requests for various API endpoints.
    """
    def __init__(self):
        """!
        @brief Initializes the generator with a list of target endpoints.
        """
        self.endpoints = [
            "/",
            "/createdb",
            "/me",
            "/users/v1",
            "/users/v1/_debug",
            "/users/v1/register",
            "/users/v1/login",
            "/users/v1/admin",          
            "/users/v1/admin/email",    
            "/users/v1/admin/password", 
            "/books/v1",
            "/books/v1/book1"           
        ]
        self.current_endpoint_index = 0
        self.fuzzing_case = 0
        print(f"RequestGenerator initialized with {len(self.endpoints)} endpoints.")

    def get_next_request(self):
        """!
        @brief Constructs and returns the next fuzzing request.
        @return A FuzzRequest object or None if all endpoints are fuzzed.
        """
        if self.current_endpoint_index >= len(self.endpoints):
            return None 
        
        endpoint = self.endpoints[self.current_endpoint_index]
        
        if self.fuzzing_case == 0:
            # Case 0: GET request
            req = FuzzRequest("GET", endpoint)
            req.headers["User-Agent"] = "Fuzzer/0.1"
            req.headers["X-Custom-Fuzz-Header"] = self._generate_fuzzed_payload()
            self.fuzzing_case += 1
            return req
        elif self.fuzzing_case == 1:
            # Case 1: POST request
            payload = self._generate_fuzzed_payload()
            req = FuzzRequest("POST", endpoint)
            req.body = f'{{"username":"{payload}", "password":"\' OR 1=1 --"}}'
            req.headers["Content-Type"] = "application/json"
            self.fuzzing_case += 1
            return req
        elif self.fuzzing_case == 2:
            # Case 2: PUT request
            payload = self._generate_fuzzed_payload()
            req = FuzzRequest("PUT", endpoint)
            req.body = f'{{"email":"{payload}@example.com", "password":"{payload}"}}'
            req.headers["Content-Type"] = "application/json"
            self.fuzzing_case += 1
            return req
        else:
            # Case 3: DELETE request
            req = FuzzRequest("DELETE", endpoint)
            req.headers["User-Agent"] = "Fuzzer/0.1"
            self.fuzzing_case = 0
            self.current_endpoint_index += 1
            return req

    def _generate_fuzzed_payload(self):
        """!
        @brief Generates a random malicious payload.
        @return A string containing the selected payload.
        """
        payloads = [
            "'", "\"", "`", "<script>alert(1)</script>", "admin'--", "OR 1=1",
            "A" * 1024 # Buffer overflow attempt
        ]
        return random.choice(payloads)