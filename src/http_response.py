class HttpResponse:
    def __init__(self, status_code, text, headers):
        self.status_code = status_code
        self.text = text
        self.headers = headers