# -*- coding:utf-8
#!/usr/bin/python
# ----------------------------------
# Jansen A. Simanullang
# (c) 29.05.2018
# ----------------------------------
"""
Decide yourself with conditional statement (100 Marks)
For this challenge, you need to read a integer value(default name - age) from stdin, store it in a variable and then compare that value with the conditions given below - 
    - if age is less than 10, then print 'I am happy as having no responsibilities.' to the stdout. 
    - if age is equal to or greater than 10 but less than 18, then print 'I am still happy but starts feeling pressure of life.' to the stdout. 
    - if age is equal to or greater than 18, then print 'I am very much happy as i handled the pressure very well.' to the stdout.  

Input Format
A single line to be taken as input and save it into a variable of your choice(Default name - age). 

Constraints
1 < = age < = 100 

Output Format
Print the sentence according to the value of the integer which you had taken as an input. 

Sample TestCase 1
Input
8
Output
I am happy as having no responsibilities.

"""
def valid_type(x, dtype):

    if dtype == 'float':
        try: x=float(x); v = True
        except: v = False
    
    if dtype == 'integer':
        try: x=int(x); v = True
        except: v = False

    return v,x

def valid_range(x, vrange):
    xmin, xmax = vrange[0], vrange[1]
    if (x>=xmin) and (x <= xmax):
        v = True
    else:
        #print('number out of range! Please insert between ' + str(xmin) + '~' +str(xmax))
        v = False
    return v

def valid_input(dtype, vrange):
    while True:
        x = raw_input()
        v,x = valid_type(x, dtype)
        if v and valid_range(x, vrange): 
            #print('valid input type: '+str(type(x)))
            break
        else: pass
    return x

def message(x):
    if x < 10:
        msg = 'I am happy as having no responsibilities.'
    elif x < 18:
        msg = 'I am still happy but starts feeling pressure of life.'
    elif x >= 18:
        msg = 'I am very much happy as i handled the pressure very well.'
    return msg

def main():
    vrange = (1, 100)
    age = valid_input('integer', vrange) # as type of integer
    print(message(age))

main()
