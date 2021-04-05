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

    def parse_diff_output(self, output):
        for line in output:
            current_line = line.split()
            if current_line[0] ==


    def parse_blame_output(self, output):
        for line in output:


        return list_of_authors, list_of_lines
