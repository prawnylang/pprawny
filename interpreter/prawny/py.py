from traceback import format_exc


class Py:
    def __init__(self, py):
        self.py = py

    def run(self):
        try:
            exec(self.py)
        except Exception as err:
            print('\x1b[1;31m{}\x1b[0m'.format(format_exc()))
