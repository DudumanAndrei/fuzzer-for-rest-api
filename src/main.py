from src.requests_http_client import RequestsHttpClient
from src.request_generator import RequestGenerator
from src.response_analyzer import ResponseAnalyzer
from src.fuzzer import Fuzzer

def main():
    print("Starting REST API Fuzzer...")
    
    http_client = RequestsHttpClient()
    request_generator = RequestGenerator()
    response_analyzer = ResponseAnalyzer()
    
    fuzzer = Fuzzer(http_client, request_generator, response_analyzer)
    
    fuzzer.run()
    
    fuzzer.generate_report()
    print("Fuzzing finished.")

if __name__ == "__main__":
    main()