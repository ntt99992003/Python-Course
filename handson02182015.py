Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #if else statement we use for decisions
>>> if 1:
	print('True')

	
True
>>> # if something is true, do this
>>> if not 1:
	print("true")

	
>>> else:
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> if not 1:
	print("True")
	else:
		
SyntaxError: invalid syntax
>>> if not 1:
	print("True")
else:
	print("False")

	
False
>>> x= 10
>>> if x>15
SyntaxError: invalid syntax
>>> if x > 15
SyntaxError: invalid syntax
>>> if x>15:
	print("Bigger than 15")
elif x < 15:
	print("smaller than 15")
else:
	print("exactly 15")

	
smaller than 15
>>> not True
False
>>> # < smaller than
>>> # > bigger than
>>> # bigger than or equal
>>> 12 ==10
False
>>> 67.0 = 67.1
SyntaxError: can't assign to literal
>>> 67.0 ==67.3
False
>>> # != not true
>>> "NAU" > "nau"
False
>>> if "a" == "a"
SyntaxError: invalid syntax
>>> if "a" == "a"
SyntaxError: invalid syntax
>>> if "a" == "a":
	print("yeah they are equal")

	
yeah they are equal
>>> x = -1
>>> if x > 0:
	print("IT is positive")
else:
	print("it is not positive")

	
it is not positive
>>> number = 2
>>> if type(number) == int:
	if number > 0:
		print("it is a positive integer number")
	elif number ==0:
		print("it is 0")
	else:
		print("it is a negative")
else:
	 print("This is not an integer")

it is a positive integer number
>>> number = 2.0
if type(number) == int:
	if number > 0:
		print("it is a positive integer number")
	elif number ==0:
		print("it is 0")
	else:
		print("it is a negative")
else:
	 print("This is not an integer")
	 
SyntaxError: multiple statements found while compiling a single statement
>>> number = 2.0
if type(number) == int:
	if number > 0:
		print("it is a positive integer number")
	elif number ==0:
		print("it is 0")
	else:
		print("it is a negative")
else:
	 print("This is not an integer")
	 
SyntaxError: multiple statements found while compiling a single statement
>>> number = 2.0
if type(number) == int:
	if number > 0:
		print("it is a positive integer number")
	elif number ==0:
		print("it is 0")
	else:
		print("it is a negative")
else:
	 print("This is not an integer")
	 
SyntaxError: multiple statements found while compiling a single statement
>>> x = 10
>>> x = x+1
>>> x
11
>>> x +=1 # x = x+1
>>> x-=1 # x = x-1
>>> 
>>> x
11
>>> 
>>> x
11
>>> n = 5
>>> while n > 0:
	print(n)
	n = n-1

	
5
4
3
2
1
>>> print)"blast off")
SyntaxError: invalid syntax
>>> print("blast off")
blast off
>>> n = 10
>>> while  True:
	print(n, end = " ")
	n = n-1

	
10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 -21 -22 -23 -24 -25 -26 -27 -28 -29 -30 -31 -32 -33 -34 -35 -36 -37 -38 -39 -40 -41 -42 -43 -44 -45 -46 -47 -48 -49 -50 -51 -52 -53 -54 -55 -56 -57 -58 -59 -60 -61 -62 -63 -64 -65 -66 -67 -68 -69 -70 -71 -72 -73 -74 -75 -76 -77 -78 -79 -80 -81 -82 -83 -84 -85 -86 -87 -88 -89 -90 -91 -92 -93 -94 -95 -96 -97 -98 -99 -100 -101 -102 -103 -104 -105 -106 -107 -108 -109 -110 -111 -112 -113 -114 -115 -116 -117 -118 -119 -120 -121 -122 -123 -124 -125 -126 -127 -128 -129 -130 -131 -132 -133 -134 -135 -136 -137 -138 -139 -140 -141 -142 -143 -144 -145 -146 -147 -148 -149 -150 -151 -152 -153 -154 -155 -156 -157 -158 -159 -160 -161 -162 -163 -164 -165 -166 -167 -168 -169 -170 -171 -172 -173 -174 -175 -176 -177 -178 -179 -180 -181 -182 -183 -184 -185 -186 -187 -188 -189 -190 -191 -192 -193 -194 -195 -196 -197 -198 -199 -200 -201 -202 -203 -204 -205 -206 -207 -208 -209 Traceback (most recent call last):
  File "<pyshell#78>", line 2, in <module>
    print(n, end = " ")
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> while True:
	line = input(">")
	if line == "done":
		break
	print(line)

	
>Enes Kemal
Enes Kemal
>How are you
How are you
>I am fine thanks
I am fine thanks
>done
>>> import time
>>> i  = 1
while true:
	print("Welcome", i, "times.  To stope press [Ctrl+c]")
	
SyntaxError: multiple statements found while compiling a single statement
>>> i  = 1
while true:
	print("Welcome", i, "times.  To stope press [Ctrl+c]")
	
SyntaxError: multiple statements found while compiling a single statement
>>> i  = 1
while True:
	print("Welcome", i, "times.  To stope press [Ctrl+c]")
	
SyntaxError: multiple statements found while compiling a single statement
>>> while True:
	print("Welcome", i, "times.  To stope press [Ctrl+c]")

	
Traceback (most recent call last):
  File "<pyshell#92>", line 2, in <module>
    print("Welcome", i, "times.  To stope press [Ctrl+c]")
NameError: name 'i' is not defined
>>> i = 1
>>> while True:
	print("Welcome", i, "times.  To stope press [Ctrl+c]")

	
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Welcome 1 times.  To stope press [Ctrl+c]
Traceback (most recent call last):
  File "<pyshell#95>", line 2, in <module>
    print("Welcome", i, "times.  To stope press [Ctrl+c]")
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> for i in "Python":
	print(i, end = "_")

	
P_y_t_h_o_n_
>>> 
