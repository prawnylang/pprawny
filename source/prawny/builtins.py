NAMES = {
    'from': 'from',
    'use': 'import',
    'for': 'for',
    'of': 'in',
    'named': 'as',
    'using': 'with',
    'do': ':',
}
OPS = {
    '<': '(',
    '>': ')',
    # '(': '<',
    # ')': '>',
    ':': '.',
    '>>': '))',
    '<<': '((',
    '//': '#',
    '$': '//',
}
LOGICOPS = {
    '&': 'and',
    '|': 'or',
}
OPS |= LOGICOPS
WAITOPS = (
    '&',
    '|',
    '-',
    '+',
)
DBLOPS = {
    '&&': 'and',
    '||': 'or',
    '--': '<',
    '++': '>',
}
