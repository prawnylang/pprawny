from tokenize import generate_tokens, TokenInfo
from typing import Tuple
from io import StringIO


class Lexer:
    def __init__(self, code: str) -> None:
        self.codeio = StringIO(code)

    def tokenize(self) -> Tuple[TokenInfo]:
        return tuple(generate_tokens(self.codeio.readline))
