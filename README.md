# Prawny
A dynamically typed programming language made with Python, that compiles into Python.

## Installation

To use Prawny on your machine, all you need is the interpreter, located at `/prawny`.

```sh
$ git clone https://github.com/prawnylang/pprawny
...
$ cd pprawny
$ ./prawny -h
usage: prawny [-h] [-f FILE] [-o OUT] [-F | --force | --no-force]

execute prawny (.prawn) code

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  the source file to execute
  -o OUT, --out OUT     the file to output the compiled python code to
  -F, --force, --no-force
                        force saving the compiled code even if a file already exists at the
                        destination (default: False)
```

### Interpreter: Basic Usage
* `$ ./prawny -f /path/to/program.prawn` executes the Prawny program at `/path/to/program.prawn`.
* `$ cat /path/to/program.prawn | ./prawny` does the same, except for the fact that here, the
contents of `/path/to/program.prawn` are read from `stdin`. This means that you can run
`$ ./prawny` and proceed to manually type in the code (hit ^D to confirm)
* Applying `-o/--out` (and `-F/--force` if the `out` file already exists) will output the
compiled Python code to your desired location.

## Syntax
The only thing different about Prawny from Python is its syntax.

Functions are called like so:
```py
print<'Hello world!'> // compiled into print('Hello world!')
```

Properties are accessed like so:
```
use sys // compiled into import sys

sys:stdout:buffer:write<b'Hello world!'> // compiled into sys.stdout.buffer.write(b'Hello world!')
```

Operators:
```py
x = 9 // compiled into x = 9

print<x -- 10> // compiled into print(x < 10)
print<x ++ 8> // compiled into print(x > 8)
print<x $ 2> // compiled into print(x % 2)
```

More:
```py
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

## Modules and Libraries

Since Prawny is just Python with a different syntax, compiled into Python and executed,
all of Python's builtin modules and installed libraries can be used in Prawny. For example,
if you want to use the `basencode` Python library in your Prawny program, you should first install the library with `pip install basencode`. Then you should be able to use `basencode`
in your programs:
```py
from basencode use *

myint = Integer<int<input<>>>

print<myint, 'in base 33 is', myint:to_base<33>>
```

If you get a `ModuleNotFoundError`, it is likely that the Prawny interpreter's default
Python interpreter is different from the Python interpreter on which you installed
the library. The Prawny interpreter uses `python3` by default. To override this,
you can run the interpreter using the appropriate Python interpreter. For example,
if `python3` points to Python 3.10 on your machine and  you installed `basencode`
on Python 3.9, you should run the Prawny interpreter with `python3.9` as shown below:

```sh
$ cat my_program.prawn | python3.9 /path/to/prawny
$ python3.9 /path/to/prawny -f my_program.prawn
```

## Support

The current version of Prawny supports Python 3.9 and higher.

## Conclusion

Prawny is just a joke, if you actually want to write code, just use something like Python,
it has many more features and much better syntax.