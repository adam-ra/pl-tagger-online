#!/usr/bin/env python3
import argparse
import json

from pltaggeronline import utils


def nonempty_numbered_lines(fname):
    with open(fname) as stream:
        for line_no, line in enumerate(stream):
            line = line.strip()
            if line:
                yield line_no + 1, line


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read filenames and write simple JSON with tagged lines.')
    parser.add_argument('input', help='filenames to tag', nargs='+')
    args = parser.parse_args()
    for fname in args.input:
        file_structure = {'filename': fname, 'lines': []}
        for line_no, line in nonempty_numbered_lines(fname):
            token_list = utils.token_structure(line)
            file_structure['lines'].append({
                'content': line, 'line_no': line_no, 'tokens': token_list})
        with open(fname + '.json', 'w') as out_stream:
            json.dump(file_structure, out_stream)
