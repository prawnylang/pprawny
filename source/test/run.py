from prawny.py import Py
from prawny.parser import Parser
from prawny.lexer import Lexer
import sys
import os

with open('program.prawn', 'r') as file:
    code = file.read()

print('source code:\x1b[93;1m')
print(code)
print('\x1b[0m')

lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser(tokens)
py = Py(parser.parse())
print('compiled py code:\x1b[93;1m')
print(py.py)
print('\x1b[0m')
py.run()
