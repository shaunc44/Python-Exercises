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

### 12.   













