class LlmIndex:
    okr_id: str

    def __init__(self, okr_id: str):
        """Initializes okr_id

        Args:
          okr_id: okr uuid to initialize on page
        """
        self.okr_id = okr_id
