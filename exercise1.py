Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> type(85.4)
<class 'float'>
>>> type(-409)
<class 'int'>
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type(None)
<class 'NoneType'>
>>> type(-13.0)
<class 'float'>
>>> 12+5-2
15
>>> 4*9.0
36.0
>>> --16
16
>>> 9/3
3.0
>>> 10//3
3
>>> 10.0//4.0
2.0
>>> (2+5)*4
28
>>> 2+5*$
SyntaxError: invalid syntax
>>> 2+5*4
22
>>> 4**3+16
80
>>> 2.1**2.0
4.41
>>> 2.2*4.0
8.8
>>> 9>1
True
>>> 3.0>3.001
False
>>> 2>2
False
>>> 3+3==9
False
>>> True or False
True
>>> True
True
>>> not False
True
>>> 3>4 or (2<3 and 9>10)
False
>>> not(4>3 and 100>6)
False
>>> 2+7.0
9.0
>>> 1/2
0.5
>>> 1//2
0
>>> 1/2 ==1//2
False
>>> round(3.4)
3
>>> int(98.7)
98
>>> 2.0 + 4.0
6.0
>>> 5*2==5.0*2.0
True
>>> "n" + "AU"
'nAU'
>>> ("Go" * "3") + "Stallions!"
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    ("Go" * "3") + "Stallions!"
TypeError: can't multiply sequence by non-int of type 'str'
>>> ("go" * 3) + "Stallions!"
'gogogoStallions!'
>>> "Stallions"[2]
'a'
>>> "Stallions"[5:]
'ions'
>>> "Stallions"[:5]
'Stall'
>>> str1 = "Python is "
>>> str2 = "so "
>>> str3 = "much fun!"
>>> print(str1)
Python is 
>>> str[0]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    str[0]
TypeError: 'type' object is not subscriptable
>>> str1[0]
'P'
>>> str1[-1]
' '
>>> len(str1)
10
>>> str1[len(str1)]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    str1[len(str1)]
IndexError: string index out of range
>>> str1 + str2 + str3
'Python is so much fun!'
>>> "t" in str3
False
>>> "t" in str1
True
>>> str3[1:3]
'uc'
>>> str2[:-1]
'so'
>>> str4[1:10]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    str4[1:10]
NameError: name 'str4' is not defined
>>> (str1 + str2 + str3)[::-1]
'!nuf hcum os si nohtyP'
>>> str1 = "here comes the best part"
>>> str2 = "methods of strings"
>>> str1.upper()
'HERE COMES THE BEST PART'
>>> str1
'here comes the best part'
>>> str1.isupper()
False
>>> str2.islower()
True
>>> str2 = str2.capitalize()
>>> str2
'Methods of strings'
>>> str2 = swapcase()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    str2 = swapcase()
NameError: name 'swapcase' is not defined
>>> str1.index("e")
1
>>> str1.index("n")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    str1.index("n")
ValueError: substring not found
>>> str1.find(e)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    str1.find(e)
NameError: name 'e' is not defined
>>> str2.find("!")
-1
>>> str1.count("e")
5
>>> str1 = str1.replace("e", "x")
>>> str1
'hxrx comxs thx bxst part'
>>> str2.replace("of" , "with")
'Methods with strings'
>>> 
