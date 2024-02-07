# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:55:17 2023

@author: Dell
"""

int_value =100
float_value = '1.5'
float_value = float(int_value)
print('int value as a float:',float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:',float_value)
print(type(float_value))
######################################
# complex Numbers
c1 = 1
c2 =  2j
print('c1:',c1,',c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
##################################################
#boolean value
# python support another type called as boolean;
# boolean means true or false;
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))
##############################################
#we can also convert

status = bool(input('ok it is confirmed?:'))
print(status)
print(type(status))
##########################################
#Arthmatic operater
home = 10
away = 15
print(home+away)
print(type(home+away))
print(10*4)
print(type(10*4))
goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))
#######################################
# division of two number must be float
print(100/20)
print(type(100/20))
##################
#double
print(100//20)
print(type(100//20))
########################
#moduloes oprator:- modulos oprator give quashent
print('modulus division 100 % 13:',100 % 13)
print('modulus division 3 % 2:', 3 % 2)
####################
#power opration
a = 5
b = 3
print(a**b)
############################
#Assignment opreater
x = 0
x+=1  # x = x+1
#################
#None value
winner = None
print( winner is None)
print(winner is not None)
#########################
#flow of control
#tools differenses
#aditor
###################
#Else in an if statment
num = int(input('enter a number'))
if num > 0:
    print(num)
num = int(input('enter yet another a number'))   
if num<0:
    print('negative number')
else:
    print('positive number')    






#########################################
 
#elif condition
#when we check sum condition
#wether it is fruit?
saving = float(input("enter how much you have in saving"))
if saving == 0:
    print("sory no saving")
elif saving <500:
    print("well done")
elif saving <1000:
    
    print("thats a tedy sum")
elif saving <10000:
    print("welcome sir")
else:
    print("thank you")  
################
# while loop
count = 1
print("straing")
while count <= 10:
    print(count)
    count+=1
  ##################  
# for loop
print("print out value in range")
for i in range(2,10):
    print(i)
    print('done')
 #######################   
num = int(input('enter the number to check for:'))
for i in range(0,16): 
    if i == num:
     break
     print(i)
     print('done')
#################################     
for _ in range(0,10):
    print('.', end='')
    print()
###############################    
#Location of print is change
for i in range(0,6):
    if i == num:
        break
    print(i,'',end='')
    print('done')
 ###########################   
 # to find out odd numbers in given range
start,end = 4,19
 # iterate each number in list
for num in range(start,end + 1):
     #chaking condition
 if num % 2 != 0:
     print(num,end =" ")     
###############################
start,end = 4,19
 # iterate each number in list
for num in range(start,end + 1):
     #chaking condition
 if num % 2 == 0:
     print(num,end =" ")  
####################################
for even_numbers in range(4,15,2):
     print(even_numbers,end = ' ')     
######################################     
for odd_numbers in range(4,15,2):
     print(odd_numbers,end = ' ')
#########################################
start = int(input('enter the start of range:'))
end =int(input('enter the end of range:')) 
for num in range(start,end + 1):
    #chaking the condition
    if num % 2 == 0:
       print(num,end=' ')
###########################################   
# code prime numbers in given range
# leap year
# is palimdrom or not 
#mario paramid
####################################
#code of prime number in given range
start = int(input('enter the start of range:'))
end =int(input('enter the end of range:')) 
for num in range(start,end + 1):
    #chaking the condition
    if num<2:
        print("not a prime")
    elif num<=2:
        print("we have to check ")
    else:    
      if num%1 == 0 and num%2!=0:
        print(num,end=' ')

        
#############################################       
start,end = 2,30
 # iterate each number in list
for num in range(start,end + 1):
     #chaking condition
    if num % 1 == 0 and num % 2!=0:
       print(num,end =" ") 
##############################################
# leap year IMP
year = int(input('enter the year:')) 
if((year%400==0)or(year%100!=0 )and( year%4==0)):
     print('year is leap year')
else:
     print('year is not a leap year')
#################################################
  # is palimdrom or not 
num =input('enter the number:')

if (num==num[::-1]):
     print('palindrome')
else:
     print('not a palindrome')
#################################################
#palindrom string
string='nan'
rev=string[::-1]
print(rev)
if(string==rev):
    print("it is a palindrom string")
else:
    print("print it is not a palindrom string")

############################################
num=121
reverse=num[::-1] 
if num==reverse:
   print('palindrome')
else:
   print('not a palindrome')  
#############################################
#mario pyramid IMP
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()
   
for i in range(4):
     for j in range(4-i):
         print("#",end=" ")
     print()       
##########################################
 # the number is prime number or not 
def prime_num(num):
       for i in range(2,num):
          if(num%i==0):
             return " the number is not prime number"
          break
       return " the number is prime number"
##########################################
x,y,z=5,6,7
print(x)
print(y)
print(z)
######################################
#gloabal variable
x ="awesome"
def my_function():
     print("python is"+x)
my_function()    
 ################################
 #local variable and global variable
x ="awesome"
def my_function():
     x ="fantastic"
     print("python is"+x)
my_function() 
 ###################################
x ="awesome"
def my_function():
     x ="fantastic"
     
my_function()
print("python is"+x)
 ######################################
#dectionary
x={"name":"ram","age":34}
print(type(x))
 ######################################
#string
#if we wantg multiple strings
x=""" This is python.
 it is very powerful"""
print(x)
 #########################################
#string slicing we want to break our sentence then use string slicing
x=""" This is python.
 it is very powerful"""
print(x[2:6]) #count index from1
 ##################################
 #slice from the start
x=""" This is python.
 it is very powerful"""
 
print(x[:3])
 ######################################
# slicing from the end
x=""" This is python.
it is very powerful"""
print(x[4:])
###############################
#negative indexing
x=" This is python"
print(x[-5:-2])
###################################
#modify the string
x=" This is python"
print(x.upper())
########################################
#remove the white space // IMP use in machine learing
x=" This is python"
print(x.strip())
######################################
#replace world
x="Hello world"
print(x.replace("Hello","Gello"))
###########################################
# use of split which replace whilte space 
x="Hello,World"       # separator is a comma
print(x.split(","))    # Vectorization
##########################################
x="Hello World"   # separator is space
print(x.split()) 
#################################################
x="Hello World"
string1=x[::-1]   # :: start to end
print(string1)
####################################################
x="Hello World"
string1=x[::-2]   # :: start to end
print(string1)
######################################################
# we find perticular world // find method find the world
x="this is an python and it is very powerful"
print(x.find("and"))
###########################################
#string concatination
x="hello"
y="world"
print(x+y)

x="hello"
y="world"
print(x+" "+y)  #adding white space
###############################################
# string formate
x=36
y="  my name is rutuja"
# print(x+y)    # give error
   
print(f"{y} and my age is {x}")  #give correct
 ##############################################
quantity = 3
item_no=54
price=67
print(f"I want{quantity} pieces and item number is{item_no},its price is{price}")
 #####################################################
my_order="I want{} pieces and item number is{},its price is{}"
print(my_order.format(quantity,item_no,price))
 ####################################################
quantity = 3
item_no=54
price=67
my_order="I want{0} pieces and item number is{1},its price is{2}"
print(my_order.format(quantity,item_no,price))
###################################################
#escape character allow double quotes inside double quotes   \-escape character
text=  


###########################################
