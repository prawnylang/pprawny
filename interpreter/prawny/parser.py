from tokenize import *
from typing import Tuple, Union
from .builtins import *


class Parser:
    def __init__(self, tokens: Tuple[TokenInfo]) -> None:
        self.tokens = tokens
        self.py = ''

    def parse(self) -> str:
        indented: bool = False
        in_dbl_op: Union[None, str] = None

        for i, token in enumerate(self.tokens):
            if token.type == INDENT:
                indented = True
            elif token.type == DEDENT:
                indented = False

            if indented and token.start[-1] == 1:
                self.py += '\t'

            nls = (NEWLINE, INDENT, DEDENT, NL)
            add = '\n' if token.type in nls else token.string

            if token.string in NAMES:
                add = NAMES[token.string]
            elif token.type in (OP, ERRORTOKEN, NAME, NUMBER):
                if in_dbl_op:
                    potential_dbl_op = in_dbl_op + token.string

                    if potential_dbl_op in DBLOPS:
                        add = DBLOPS[potential_dbl_op]
                    else:
                        add = (OPS.get(in_dbl_op) or in_dbl_op) + \
                            (OPS.get(token.string) or token.string)

                    in_dbl_op = None
                elif token.string in WAITOPS:
                    in_dbl_op = token.string
                elif token.string in OPS:
                    add = OPS[token.string]

            if not in_dbl_op:
                self.py += add

            if token.type not in nls:
                self.py += ' '

        return self.py
