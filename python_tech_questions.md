### 1. How do you print a key, value pair from a dictionary?  
```python
for i in d:
  print (i, d[i])
```
-> i is the *key*, and d[i] is the *value*

### 2. What is the order of operations in Python?  
Answer: PEDMAS (Parens, Exponents, Division, Multiplication, Addition, Subtraction)  

### 3. Operators with the same precedence are evaluated in which manner?  
Answer: Left to Right

### 4. Which of the following is not a keyword?  
```
a) eval  
b) assert  
c) nonlocal  
d) pass  
```
Answer: A, eval can be used as a variable

***
# REGEX

### 5. Which of the following creates a pattern object?  
a) re.create(str)  
b) re.regex(str)  
c) re.compile(str)  
d) re.assemble(str)  
Answer: c

### 6. What does the function re.match do?  
a) matches a pattern at the start of the string  
b) matches a pattern at any position in the string  
c) such a function does not exist  
d) none of the mentioned  
Answer: a  

### 7. What does the function re.search do?  
a) matches a pattern at the start of the string  
b) matches a pattern at any position in the string  
c) such a function does not exist  
d) none of the mentioned  
Answer: b  

### 8. What is the output of the following?  
```python
sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())
```
Answer: (‘we’, ‘are’, ‘humans’), returns all subgroups that have been matched  

### 9. What is the output of the following?  
```python
sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.group())
```
Answer: ‘we are humans’, returns the entire match  

### 10. What is the output of the following?  
```python
sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.group(2))
```
Answer: ‘humans’, returns 2nd index of the group  

***
# NUMERIC TYPES

### 11. What is the output of print 0.1 + 0.2 == 0.3?  
Answer: False
*Neither of 0.1, 0.2 and 0.3 can be represented accurately in binary. The round off errors from  
0.1 and 0.2 accumulate and hence there is a difference of 5.5511e-17 between (0.1 + 0.2) and 0.3.*  

### 12. Which of the following is not a complex number?  
```
a) k = 2 + 3j
b) k = complex(2, 3)
c) k = 2 + 3l
d) k = 2 + 3J
```
Answer: c, b/c l (or L) stands for long  

### 13. What does ~4 evaluate to?  
```
a) -5
b) -4
c) -3
d) +3
```
Answer: a, ~x is equivalent to -(x+1).  

### 14. Which of the following is incorrect?  
```
a) x = 0b101
b) x = 0x4f5
c) x = 19023
d) x = 03964
```
Answer: d  
Explanation: Numbers starting with a 0 are octal numbers but 9 isn’t allowed in octal numbers.  

### 15. What is the result of cmp(3, 1)?  
```
a) 1
b) 0
c) True
d) False
```
Answer: a  
Explanation: cmp(x, y) returns 1 if x > y, 0 if x == y and -1 if x < y.  

### 16. Which of the following is incorrect?  
```
a) float(‘inf’)
b) float(‘nan’)
c) float(’56’+’78’)
d) float(’12+34′)
```
Answer: d  
Explanation: ‘+’ cannot be converted to a float.  

### 17. What is the result of round(0.5) – round(-0.5)?  
```
a) 1.0
b) 2.0
c) 0.0
d) None of the mentioned
```
Answer: b  
Explanation: Python rounds off numbers away from 0 when the number to be rounded off is  
exactly halfway through. round(0.5) is 1 and round(-0.5) is -1.  

### 18. What does 3 ^ 4 evaluate to?  
```
a) 81
b) 12
c) 0.75
d) 7
```
Answer: d  
Explanation: ^ is the Binary XOR operator.  
*^ (XOR) copies the bit if it is in one operand, but not both*  

***
# FOR & WHILE LOOPS

### 19. What is the output of the following?  
```python
x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)
```
Answer: ['ab', 'cd'], b/c upper() doesn't modify strings in place, but returns  
a new string which isn't being stored anywhere  

### 20. What is the output of the following?  
```python
x = ['ab', 'cd']
for i in x:
    x.append(i.upper())
print(x)
```
Answer: the loop will run forever as new elements are added to the list  

### 21. What is the output of the following?  
```python
i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i + = 1
```
Answer: SyntaxError, there shouldn’t be a space between + and = in +=  

### 22. What is the output of the following?  
```python
i = 1
while True:
    if i%0O7 == 0:
        break
    print(i)
    i += 1
```
Answer: 1 2 3 4 5 6, control exits when i = 7;  
python apparently converts O to 0 and ignores leading zeroes;  
007 is an octal number which are base 8 numbers  

### 23. What is the output of the following?  
```python
i = 5
while True:
    if i%0O11 == 0:
        break
    print(i)
    i += 1
```
Answer: 5 6 7 8  
Explanation: 0o11 is an octal number which equals 1*(8**1) + 1*(8**0) = 9  
Therefore the numbers print until i = 9  

### 24. What is the output of the following?  
```python
i = 5
while True:
    if i%0O9 == 0:
        break
    print(i)
    i += 1
```
Answer: Error
Explanation: 9 isn’t allowed in an octal number, only 0 - 8.  

### 25. What is the output of the following?  
```python
i = 1
while True:
    if i%2 == 0:
        break
    print(i)
    i += 2
```
Answer: 1 3 5 7 9 11 ...
Explanation: The loop does not terminate since i is never an even number.  

### 26. What is the output of the following?  
```python
i = 1
while False:
    if i%2 == 0:
        break
    print(i)
    i += 2
```
Answer: None  
Explanation: Control does not enter the loop because of False

### 27. What is the output of the following?  
```python
True = False
while True:
    print(True)
    break
```
Answer: SyntaxError, True is a keyword and it’s value cannot be changed.  

***
# STRINGS

### 28. The output of executing string.ascii_letters can also be achieved by:  
Answer: string.ascii_lowercase+string.ascii_upercase  

### 29. What is the output when the following code is executed ?  
```python
    >>> str1 = 'hello'
    >>> str2 = ','
    >>> str3 = 'world'
    >>> str1[-1:]
```
Answer: 0  
Explanation: -1 corresponds to the last index.  

### 30. What is the output when the following statement is executed?  
```python
    >>>print 'new' 'line'
```
Answer: newline  
Explanation: String literals seperated by white space are allowed. They are concatenated.  


### 31. What is the output when the following statement is executed ?  
```python
print '\x97\x98'
```
Answer: _~  
Explanation: \x is an escape sequence that means the following 2 digits are  
a hexadicmal number encoding a character.  

### 32. What is the output when following code is executed ?  
```python
str1="helloworld"
str1[::-1]
```
Answer: dlrowolleh  

### 33. print 0xA + 0xB + 0xC:  
Answer: 33  
Explanation:0xA and 0xB and 0xC are hexadecimal integer literals  
representing the decimal values 10,11 and 12 respectively. There sum is 33.  
*0x followed by number; means HEX number*  
*\x followed by number; means HEX ascii character*  

***
# LISTS

### 34. What is the output when we execute list(“hello”)?  
Answer: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]  

### 35. Suppose list1 is [1, 5, 9], what is sum(list1) ?  
Answer: 15  

### 35. To shuffle the list(say list1) what function do we use?  
```
a) list1.shuffle()
b) shuffle(list1)
c) random.shuffle(list1)
d) random.shuffleList(list1)
```
Answer:c, shuffle list1 in places, then return list1  

***
# DICTIONARIES

### 36. What will be the output?  
```python
d = {"john":40, "peter":45}
"john" in d
```
Answer: True  
*Explanation: 'in' can be used to check if the __key__ is int dictionary.*  

***
# TUPLES

### 37. What will be the output? 
```python
t1 = (1, 2, 4, 3)
t2 = (1, 2, 3, 4)
t1 < t2
```
Answer: False  
*Explanation: Elements are compared one by one in this case.*  

### 38. What will be the output?  
```python
my_tuple = (1, 2, 3, 4)
my_tuple.append( (5, 6, 7) )
print len(my_tuple)
```
Answer: Error  
*Explanation: Tuples are immutable and don’t have an append method. An exception is thrown in this case*  

### 39. What will be the output?  
```python
numberGames = {}
numberGames[(1,2,4)] = 8
numberGames[(4,2,1)] = 10
numberGames[(1,2)] = 12

sum = 0
for k in numberGames:
    sum += numberGames[k]

print len(numberGames) + sum
```
Answer: 3 + 30 = 33  
*Explanation: Tuples can be used for keys into dictionaries. Tuples can have mixed lengths  
and the order of the items in the tuple is considered when comparing the equality of the keys*  

***
# FILES

### 40. To open a file c:\scores.txt for reading, we use:  
```python
infile = open(“c:\\scores.txt”, “r”)
```

### 41. Which of the following statements are true? (multiple answers allowed)  
```
When you open a file for reading, if the file does not exist, an error occurs.
When you open a file for writing, if the file does not exist, a new file is created.
When you open a file for writing, if the file exists, the existing file is overwritten with the new file.
```
All statements are true  

### 42. To read the entire remaining contents of the file as a string from a file object infile, we use:  
`infile.read()`  
*Explanation: read function is used to read all the lines in a file.*  

### 43. What is the output?  
```python
f = None

for i in range (5):
    with open("data.txt", "w") as f:
        if i > 2:
            break

print f.closed
```
Answer: True  
*Explanation: The WITH statement when used with open file guarantees that  
the file object is closed when the with block exits*  

***
# FUNCTIONS

### 44. What is the output of the below program?  
```python
x = 50

def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)
```
Answer:  
```
x is 50
Changed global x to 2
Value of x is 2
```
*Explanation: The global statement is used to declare that x is a global variable – hence, when we assign a  value to x inside the function, that change is reflected when we use the value of x in the main block*  

### 45. Which of the following is a features of DocString?  
```
a) Provide a convenient way of associating documentation with Python modules, functions, classes, and methods
b) All functions should have a docstring
c) Docstrings can be accessed by the __doc__ attribute on objects
d) All of the mentioned
```
Answer: d  
*Explanation: Python has a nifty feature called documentation strings, usually referred to by its shorter  name docstrings. DocStrings are an important tool that you should make use of since it helps to document  the program better and makes it easier to understand*  

***
# EXCEPTION HANDLING

### 46. How many except statements can a try-except block have?  
Answer: more than zero  
*Explanation: There has to be at least one except statement*  

### 47. Is the following code valid?  
```python
try:
    # Do something
except:
    # Do something
finally:
    # Do something
```
Answer: finally cannot be used with except  

### 48. When is the finally block executed?  
Answer: The finally block is always executed.  

### 49. What is the output of the following code?  
```python
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
```
Answer: 2  
*Explanation: The finally block is executed even if there is a return statement in the try block*  
*Only one thing can be returned from a function, unless packed*

### 50. What happens when ‘1’ == 1 is executed?  
Answer: False  
*Explanation: It simply evaluates to False and does not raise any exception*  

***
# ARGUMENT PASSING 1

### 51. What is the type of each element in sys.argv?
Answer: String  
*Explanation: It is a list of strings*  

### 52. What is the length of sys.argv?  
Answer: number of arguments + 1
*Explanation: The first argument is the name of the program itself.  
Therefore the length of sys.argv is one more than the number arguments*  

### 53. What is the output of the following code?  
```python
def foo(k):
    k[0] = 1
q = [0]
foo(q)
print(q)
```
Answer: 1
*Explanation: Lists are passed by reference*

### 54. How are keyword arguments specified in the function heading?
`two stars followed by a valid identifier`  

### 55. What is the output of the following code?  
```python
def foo():
    return total + 1
total = 0
print(foo())
```
Answer: 1  
*Explanation: It is possible to read the value of a global variable directly*

### 56. What is the output of the following code?  
```python
def foo(x):
    x = ['def', 'abc']
    return id(x)
q = ['abc', 'def']
print(id(q) == foo(q))
```
Answer: False  
*Explanation: A new object is created in the function*  

### 57. What is the output of the following code?  
```python
def foo(i, x=[]):
    x.append(i)
    return x
for i in range(3):
    print(foo(i))
```
Answer: [0] [0, 1] [0, 1, 2]  
*Explanation: When a list is a default value, the same list will be reused*  

### 58. What is the output of print(k) in the following?  
```python
k = [print(i) for i in my_string if i not in "aeiou"]
print(k)
```
Answer: list of Nones  

***
# MAPPING FUNCTIONS

### 59. What is the output of the following?  
```python
x = ['ab', 'cd']
print(list(map(upper, x)))
```
Answer: Error  
*Explanation: A NameError occurs because upper is a class method*  

### 60. What is the output of the following?  
```python
x = ['ab', 'cd']
print(len(map(list, x)))
```
Answer: A TypeError occurs as map has no len().  

***
# STRINGS

### 61. What is the output of the following code?  
```python
class father:
    def __init__(self, param):
        self.o1 = param

class child(father):
    def __init__(self, param):
        self.o2 = param

obj = child(22)
print "%d %d" % (obj.o1, obj.o2)
```
Answer: Error  
*Explanation: self.o1 was never created*  

### 62. What is the output of the following code?  
```python
example = "snow world"
example[3] = 's'
print example
```
Answer: Error  
*Explanation:Strings cannot be modified*  

### 63. What is the output of the following code ?
```python
example="helloworld"
example[::-1].startswith("d")
```
Answer: True  
*Explanation: Starts with checks if the given string starts with the parameter that is passed*  

### 64. What is the output of the following code?  
```python
class Count:
    def __init__(self, count = 0):
       self.__count = count

c1 = Count(2)
c2 = Count(2)
print(id(c1) == id(c2), end = " ")

s1 = "Good"
s2 = "Good"
print(id(s1) == id(s2))
```
Answer: False True
*Explanation: Execute in the shell objects cannot have same id, however in the case of strings its different*

### 65.  What is the output of the following code?  
```python
class Name:
    def __init__(self, firstName, mi, lastName):
        self.firstName = firstName
        self.mi = mi
        self.lastName = lastName

firstName = "John"
name = Name(firstName, 'F', "Smith")
firstName = "Peter"
name.lastName = "Pan"
print(name.firstName, name.lastName)
```
Answer: John Pan  

### 66. Suppose x is 345.3546, what is format(x, “10.3f”) (_ indicates space)  
`Answer: ___345.355`
*Explanation: 10.3 indicates 10 digit spaces, including 3 decimal places*  

### 67. What is the output when following code is executed ?  
```python
names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0

for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print sum
```
Answer: 12  
*Explanation: When assigning names1 to names2, we create a second reference to the same list.  
Changes to names2 affect names1. When assigning the slice of all elements in names1 to names3,  
we are creating a full  copy of names1 which can be modified independently*  

### 68. Suppose list1 is [1, 3, 2], What is list1 * 2?
`[1, 3, 2, 1, 3, 2]`

### 69. 






























