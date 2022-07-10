from argparse import ArgumentParser, BooleanOptionalAction
from prawny.lexer import Lexer
from prawny.parser import Parser
from prawny.py import Py
from autopep8 import fix_code
from functools import partial
from io import StringIO
import sys
import os


def main():
    parser = ArgumentParser(description='execute prawny (.prawn) code')
    parser.add_argument(
        '-f', '--file', help='the source file to execute')
    parser.add_argument(
        '-o', '--out', help='the file to output the compiled python code to')
    parser.add_argument(
        '-F', '--force', type=bool,
        help='force saving the compiled code even if a file already exists at '
        'the destination', default=False, action=BooleanOptionalAction)
    args = parser.parse_args()
    code = ''

    if not args.file:
        code = sys.stdin.read()
    elif not os.path.isfile(args.file):
        parser.error(f'{args.file}: file not found')

    if args.file:
        try:
            with open(args.file, 'r') as f:
                for chunk in iter(partial(f.read, 32), ''):
                    code += chunk
        except MemoryError:
            parser.error(
                f'{args.file}: file too large, unable to load into ram')
        except PermissionError:
            parser.error(
                f'insufficient permissions on {args.file}, unable to read')

    py = Py(Parser(Lexer(code).tokenize()).parse())

    if args.out:
        if os.path.isfile(args.out):
            if args.force:
                parser.error(
                    f'{args.file} already exists, use -F/--force to continue '
                    'or rename or delete the file')
            else:
                print(f'{args.file} already exists but -F/--force has been '
                      'specified, forcing save')

        file = StringIO(fix_code(py.py))

        try:
            with open(args.out, 'w') as outf:
                for chunk in iter(partial(file.read, 32), ''):
                    outf.write(chunk)
        except PermissionError:
            parser.error(
                f'insufficient permissions on {args.out}, unable to write')
        except IOError:
            parser.error(f'ran out of storage while writing to {args.out}')
    else:
        py.run()


if __name__ == '__main__':
    main()
