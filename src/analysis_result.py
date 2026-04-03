class AnalysisResult:
    def __init__(self, is_vulnerable, vulnerability_type="", details=""):
        self.is_vulnerable = is_vulnerable
        self.vulnerability_type = vulnerability_type
        self.details = details