from traceback import format_exc


class Py:
    def __init__(self, py: str) -> None:
        self.py = py

    def run(self) -> None:
        try:
            exec(self.py)
        except Exception:
            print('\x1b[1;31m{}\x1b[0m'.format(format_exc()))
