from email_gen.operations.readers import default_reader
from .parsers import make_parser


def make_filter(instance, parser_data):
    parser_list = []
    for field in parser_data.target_fields:
        for parser_name, parser_opts in parser_data.parser_opts(field):
            parser = make_parser(field, parser_name, parser_opts)
            parser_list.append(parser)

    def line_filter(line):

        line_items = default_reader(line)
        if not line_items:
            return False

        entity = instance.get_row_dict(line_items)

        return entity if all([f(entity) for f in parser_list]) else False

    return line_filter
