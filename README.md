# Prawny
A dynamically typed programming language made with Python, that compiles into Python.

## Syntax
The only thing different about Prawny from Python is its syntax.

Functions are called like so:
```
print<'Hello world!'> // compiled into print('Hello world!')
```

Properties are accessed like so:
```
use sys // compiled into import sys

sys:stdout:buffer:write<b'Hello world!'> // compiled into sys.stdout.buffer.write(b'Hello world!')
```

Operators:
```
x = 9 // compiled into x = 9

print<x -- 10> // compiled into print(x < 10)
print<x ++ 8> // compiled into print(x > 8)
print<x $ 2> // compiled into print(x % 2)
```

More:
```
using open<'file.txt'> named f do // compiled into with open('file.txt') as f:
	text = f.read<> // compiled into text = f.read()

print<text> // compiled into print(text)

// This is a comment, comments are compiled into Python comments as well

try do // compiled into try:
	raise Exception
except do // compiled into except:
	print<'caught exception'> // compiled into print('caught exception')
finally do // compiled into finally:
	print<'finally'> // compiled into print('finally')
```
