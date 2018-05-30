# -*- coding:utf-8
#!/usr/bin/python
# ----------------------------------
# Jansen A. Simanullang
# (c) 29.05.2018
# ----------------------------------
"""
Count special numbers between boundaries (100 Marks)
For this challenge, you are given a range and you need to find how many prime numbers lying between the given range. 

Input Format
For this challenge, you need to take two integers on separate lines. These numbers defines the range. 

Constraints
1 < = ( a , b ) < = 100000

Output Format
output will be the single number which tells how many prime numbers are there between given range. 

Sample TestCase 1
Input
1
20
Output
7
Explanation
There are 7 prime numbers which lies in the given range. 
They are 3, 5, 7, 11, 13, 17, 19

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
        x = input()
        v,x = valid_type(x, dtype)
        if v and valid_range(x, vrange): 
            #print('valid input type: '+str(type(x)))
            break
        else: pass
    return x

def prime_numbers(xmin, xmax):

    primeset = []
    nonprimeset = [1]

    numbers = [x for x in range(xmin,xmax+1)]

    for num in numbers:
        for i in range(2, num):
            if (num % i) == 0:
                if num not in nonprimeset:
                    nonprimeset.append(num)                

        if num not in nonprimeset:
            primeset.append(num)

    return primeset

def main():
    valid_range = (1, 100000)
    a = valid_input('integer', valid_range) # as type of integer
    b = valid_input('integer', valid_range) # as type of integer

    primeset = prime_numbers(a, b)

    print(len(primeset))
    #print((primeset))


main()
