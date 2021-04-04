import fuzzywuzzy as fuzz


class ProcessorParser:
    pass

    def __init__(self):
        pass

    def need_to_change_author(self, first, second, setting_ratio):
        ratio = fuzz.ratio(first, second)
        if ratio >= setting_ratio:
            return True
        else:
            return False
