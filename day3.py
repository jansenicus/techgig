# -*- coding:utf-8
#!/usr/bin/python
# ----------------------------------
# Jansen A. Simanullang
# (c) 29.05.2018
# ----------------------------------
"""
Play with operators (100 Marks)
For this challenge, you will be given the values of principal, interest and year. You need to calculate the simple interest, round it to the nearest integer and print it. 

Input Format
There will be 3 lines of numeric input - 
'a' : principal which is of type double. 
'b' : interest which is of type integer. 
'c' : year which is again of type integer. 

Constraints
1 < = (a,b,c) < = 1000

Output Format
Just print the simple interest value after performing the calculation using the formula to the stdout. The result should be an integer. 

Sample TestCase 1
Input
1000
4
2
Output
80
Explanation
Given the value of principal, interest and year. 
You can calculate the simple interest using the formula 
Sample Interest = (principal * interest * year)/100 
Round the value to the nearest integer and print it.
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

def main():
    vrange = (1, 1000)
    a = valid_input('float', vrange) # must be type of double
    b = valid_input('integer', vrange) # as type of integer
    c = valid_input('integer', vrange) # as type of integer

    # (principal * interest * year)
    principal, interest, year = a, b, c

    # simple interest
    si = (principal * interest * year)/100

    print('{:.0f}'.format(si))

main()