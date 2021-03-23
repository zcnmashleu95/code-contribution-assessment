class Input:
    entered_request
    pass

    def __init__(self):
        pass

    def ask_for_request(self):
        self.entered_request = input()

    def get_input(self):
        return self.entered_request
