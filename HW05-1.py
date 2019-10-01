#!/usr/bin/env python3

"""
Georgia Institute of Technology - CS1301
HW05 - Tuples and Modules
"""

__author__ = """Christos Alexopoulos"""
__collab__ = """I worked on the homework assignment alone, using only this semester's course material"""



"""
Function name: six_flags
Parameters: a list of tuples
Returns: a tuple
"""

def six_flags(alist):
    blist=[]
    mytup2=()
    mytup3=()
    mystr=''
    if alist==[]:
        return ()
    for item in alist:
        mytup=item[::-1]
        blist.append(mytup)
    blist.sort()
    for y in blist:
        minutes,name=y
        mytup3+=(name,)
    return mytup3




"""
Function name: medical_center
Parameters: a list of tuples, a tuple
Returns: a tuple
"""

def medical_center(hospitals, myloc):
    import math as m
    dist=10**10
    for i in range(len(hospitals)):
        location,x,y=hospitals[i]
        if m.sqrt(((x-myloc[0])**2)+((y-myloc[1])**2))<dist:
            dist=m.sqrt(((x-myloc[0])**2)+((y-myloc[1])**2))
            closest=location
    rounded_dist=round(dist,2)
    return (closest,rounded_dist)









"""
Function name: caffeinated
Parameters: a list of tuples, a list of strings
Return value: a tuple of strings
"""

def caffeinated(drinks,flavors):
    cannot=()
    for x in range(len(flavors)):
        flavors[x]=flavors[x].lower()
    for i in range(len(drinks)):
        drink,flavor1,flavor2=drinks[i]
        if flavor1.lower() in flavors and flavor2.lower() in flavors:
            cannot+=(drink,)
    return cannot







"""
Function name: study_abroad
Parameters: a list of tuples, an int (0-6 inclusive)
Returns: a list of tuples
"""

def study_abroad(dates,num):
    import calendar as c
    final=[]
    for i in range(len(dates)):
        year,day=dates[i]
        if (c.monthrange(dates[i][0],dates[i][1]))[0]!=num:
            new_tup=(dates[i][1],dates[i][0])
            final.append(new_tup)
    return final








"""
Function name: simplify
Parameters: a list of strings
Returns: a list
"""

def gcf(num1, num2):
    num1,num2 = abs(num1),abs(num2)
    return (num1 if num2 == 0 else num2) if (num1 == 0 or num2 == 0) else (gcf(num2, num1%num2) if num1 >= num2 else gcf(num1, num2%num1))

def simplify(alist):
    final=[]
    for item in alist:
        numerator=int(item[:item.find('/')])
        denominator=int(item[(item.find('/')+1):len(item)])
        greatest=gcf(numerator,denominator)
        numerator_simplified=numerator//greatest
        denominator_simplified=denominator//greatest
        simple="{}/{}".format(numerator_simplified,denominator_simplified)
        tup=(greatest,simple)
        final.append(tup)
    return final





