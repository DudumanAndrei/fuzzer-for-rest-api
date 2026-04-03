class AnalysisResult:
    """!
    @brief A data class holding the result of a response analysis.
    """
    def __init__(self, is_vulnerable, vulnerability_type="", details=""):
        """!
        @brief Initializes the analysis result.
        @param is_vulnerable Boolean indicating if a vulnerability was found.
        @param vulnerability_type A string describing the type of vulnerability.
        @param details Additional details about the finding.
        """
        self.is_vulnerable = is_vulnerable
        self.vulnerability_type = vulnerability_type
        self.details = details