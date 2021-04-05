from processorparser import ProcessorParser


class CalculateMinStringDistCommand():
    pass

    def __init__(self):
        pass

    def execute(self, processor_parser: ProcessorParser, first_list, second_list, settings):
        index = 0

        while index < first_list.len() or index < second_list.len():
            change = processor_parser.need_to_change_author(first_list[index]),second_list[index])
            if(change == True)