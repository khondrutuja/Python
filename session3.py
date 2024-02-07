# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:14:00 2023

@author: Dell
"""
#Returning dictionary
def build_person(first_name,last_name):
    #returning dectionary of information of person
    person={'first':first_name,'last':last_name}
    return person
musician = build_person('ram','thorat')
print(musician)
###########################
#passing list or return list
def greed_users(username):
     for name in username:
         msg=f"hello,{name.title()}!"
         print(msg)
username=['rutuje','rohini','pranjal']   
greed_users(username)
##################################
#passing arbitary number of argumentdef
def make_pizza(*topping):
    #print the list of toppings that have been requested
    print(topping)
make_pizza('pipponari')
make_pizza('mashrom','extra_chees','extra_chees')
#now we can replace the print() call with loop that run
#list of topping and discribe the pizza being recorded
def make_pizza(*toppings):
    #print the list of toppings that have been requested
    print("making pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pipponari')
make_pizza('mashrom','chees','extra_chees')
########################################
#mixing positional argument and arbitary argument
def make_pizza(size,*toppings): # size=positional argument and topping is arbitary argument
    #print the list of toppings that have been requested
    print("making pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pipponari')
make_pizza(12,'mashrom','chees','extra_chees')
##############################################           
import pizza
pizza.make_pizza(16,'pipponari')
pizza.make_pizza(12,'mashrom','chees','extra_chees')      
################################################
 #importing specific fungction
  
from pizza import make_pizza   
pizza.make_pizza(16,'pipponari')
pizza.make_pizza(12,'mashrom','chees','extra_chees')

###########################
#using as to give a function an alias
from pizza import make_pizza as mp 
mp(16,'pipponari')
mp(12,'mashrom','chees','extra_chees')
###########################################
#using as to give a module an alias
import pizza as p   
p.make_pizza(16,'pipponari')
p.make_pizza(12,'mashrom','chees','extra_chees')
####################################################
#import all function in module
from pizza import*
make_pizza(16,'pipponari')
make_pizza(12,'mashrom','chees','extra_chees')
############################################
#scope of variable
x=x+1  #can not call variable befor initiallization
x=6  
print(x) 
##########################
#lambda function- anonimus function-initialize   \\IMP or list comprehention
#advantages-hardwaire perspective
#name of function=lambda argument : bissuness logic
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6)) #//simple function call
add=lambda a,b,c:a+b+c #lambda function for addition
add(4,5,6) #lambda function call
########################################
#write lambda function for multiplication
def mul(a,b,c):
    mul=a*b*c
    print(mul(4,5,6))
mul=lambda a,b,c:a*b*c
mul(4,5,6)    
##############################################
#arbitary arguments
val=lambda *args:sum(args)  #name of function=lambda arbitary
                            #arguments:bissnes logic
val(1,2,3,5,6)    
val(1,2,3,5,7,8)
#######################################
#two type of argument keyword argument and non key word argument we pass in python function
#there are special symbol assign to represent key word argument and non key word argument
#*args is non key word argument
#**kwargs is key word argument
 #what is non key word args
# *args is use to pass variable number of arguments to the function.it is use to pass non key word variable lenth
#############################################
#key word argument
#when we pass key word argument then resultant argument will be a dictionary
def porson(name,**data):
    print(name)
    print(data)
porson(name='navin',age='28',place='mumbai',mo_no='985060')
################################################
def person(name,**data):
    print( name)
    for i,j in data.items():
        print(i,j)
person('navin',age='28',place='mumbai',mo_no=985060) #output will be in vertical manner
###################################
valu=lambda **data:sum(data.values())
valu(a=2,b=6,c=7,d=10)
###################################
# if condition in lambda function
max=lambda a,b:x if(a>b)else b #error lambda function not accept if without else
print(max(1,2))
#####################################
max=lambda a,b:a if(a>b)else b
print(max(1,2))
#####################################
#python collection type
#tuple-tuple are use to store multiple items in single variable
#tuple is order and imutable(not changeble)
#tuple are written with raound breaket
#tuple hold different data type
tup1=(1,3,5,7)
#accessing element of tuple
print(f'tup[0]:\t{tup1[0]}')
print('tup[1]:\t',tup1[1])
print('tup[2]:\t',tup1[2])
print('tup[3]:\t',tup1[3])     
##########################################
#tuple hold different data type
tup2=(1,'john',True,-23.45)
print(tup2)
#############################
#iterating over tuple use for loop
tup3=('apple','orange','plum','apple')  
for x in tup3:
    print(x)
#######################################
#find the lenth of tuple using len function   
len(tup3) 
############################
#appears in a tuple
tup4=('apple','orange','plum','apple','apple')
tup4.count('apple')
###########################
# find 1st index of value in tuple
print(tup4.index('apple'))
print(tup4.index('plum'))
#chack if element exists
#holipython.com-solve all assignment at home=all tuple example
#hackerrank
if 'orange' in tup3:
    print("orange is in the tuple")
############################################           
           