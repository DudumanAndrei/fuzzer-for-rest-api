from src.requests_http_client import RequestsHttpClient
from src.request_generator import RequestGenerator
from src.response_analyzer import ResponseAnalyzer
from src.fuzzer import Fuzzer

def main():
    print("Starting REST API Fuzzer...")
    
    # 1. Create instances of the components
    http_client = RequestsHttpClient()
    request_generator = RequestGenerator()
    response_analyzer = ResponseAnalyzer()
    
    # 2. Inject them into the Fuzzer
    fuzzer = Fuzzer(http_client, request_generator, response_analyzer)
    
    # 3. Run the fuzzer
    fuzzer.run()
    print("Fuzzing finished.")

if __name__ == "__main__":
    main()