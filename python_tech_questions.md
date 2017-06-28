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

### 22. 


































