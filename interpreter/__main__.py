#! /usr/bin/env python3

from argparse import ArgumentParser
from prawny.lexer import Lexer
from prawny.parser import Parser
from prawny.py import Py
from functools import partial
import sys
import os


def main():
    parser = ArgumentParser(description='execute prawny (.prawn) code')
    parser.add_argument(
        '-f', '--file', help='the source file to execute', default='')
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

    Py(Parser(Lexer(code).tokenize()).parse()).run()


if __name__ == '__main__':
    main()
