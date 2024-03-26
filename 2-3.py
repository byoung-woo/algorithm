Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def func1():
...     global a
...     a=10
...     print("func1()에서 a 값 %d" %a)
... 
>>> def func2():
...     print("func2()에서 a 값 %d" %a)
... 
...     
>>> a=20
>>> 
>>> fucn1()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    fucn1()
NameError: name 'fucn1' is not defined. Did you mean: 'func1'?
>>> func2()
func2()에서 a 값 20
>>> func1()
func1()에서 a 값 10
>>> func1()
func1()에서 a 값 10
>>> func2()
func2()에서 a 값 10
