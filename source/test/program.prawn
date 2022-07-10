from basencode use *
use sys

print<'yes it works!'>;
print<8 + 9>;
print<'1 or 0 is', 1 || 0>;
integer = Integer<10>;
print<integer.to_base<36>>;

for i of range<18> do
	print<i>;

using open<'program.prawn', 'rb'> named f do
	print<'lmao im reading my own source code'>;
	sys:stdout:buffer:write<f.read<>>;

// this is a comment
print<'this is how u do floor division', 8 $ 3>;
x = int<input<>>;
print<f'x is {x}'>;

if x -- 10 do
	print<'x is less than 10'>;
elif x ++ 10 do
	print<'x is greater than 10'>;

print<'x + 9 + x + x is', x + 9 + x + x>;