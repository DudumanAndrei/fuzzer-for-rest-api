class FuzzRequest:
    def __init__(self, method, endpoint, headers=None, body=""):
        self.method = method
        self.endpoint = endpoint
        self.headers = headers if headers is not None else {}
        self.body = body