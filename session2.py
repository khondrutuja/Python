# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 09:22:48 2023

@author: Dell

"""
#################################
#the number is prime or not #when we use function then use return statment insted of using else
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return"the number is not prime number"
            break
        return"the number is prime num"
prime_num(44)
################################
#function without argument
def greet_user():
    #"""Display a simple greeting.""""
    print("Hello")
greet_user()    
####################################
#passing information to function
def greet_user(username):
    #"""Display a simple greeting.""""
    print(f"Hello,{username}!")
greet_user('sanjivani AI')   
######################################
#argument and parameters
def describe_pet(animal_type,pet_name):  # positional argument
    print(f"\nI have a{animal_type}.")
    print(f"my{animal_type}'s name is {pet_name}.")
describe_pet('Dog','moti')
###########################################
#Defalt value
#when writing a function you can define a defalt value for each padef describe_pet(animal_type,pet_name):  # positional argument
def describe_pet(pet_name,animal_type='dog'):  # positional argument
    print(f"\nI have a{animal_type}.")
    print(f"my{animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='moti')
#############################################
#Avoiding argument errors
def describe_pet(animal_type,pet_name):
    #display information about a pet
    
###################################
#create a program using maths and f string and tell us how many days,weeks and month we have left if wewill left until 18 year
#wrte program for roller poster if  hight is grater than 120 cm then you are elligible to pay roller poster 
#2) if your age is under  18 the tikit will be 20 Rs and is your age is >18 
 #   if hight is 120 cm yhen tikit 
####################################
# one year contain 365 days
#one year contain 52 weeks
#one year contain 12 months
 age=int(input("enter the current age:"))
final_age=int(input("enter the final age:"))
remaning_year=final_age-age
print("remaing year is:",remaning_year)
no_of_days_left=remaning_year*365
print("no of day left is:",no_of_days_left)
no_of_week_left=remaning_year*52
print("no of week left is :",no_of_week_left)
no_of_month_left=remaning_year*12
print("no of month left is:",no_of_month_left)
##################################################
#using function
def no_day(day,week,month):
    print(f"no of day left{day},no of week left is {week},no of month left {month}")
    age=int(input("enter the current age:"))
    final_age=int(input("enter the final age:"))
    remaning_year=final_age-age
    no_of_days_left=remaning_year*365
    no_of_week_left=remaning_year*52
    no_of_month_left=remaning_year*12
no_day('no_of_days_left','no_of_week_left','no_of_month_left')
    
################################################
#program for roller coaster
height=int(input("enter your height:"))
age=int(input("enter your age"))
if height==120 or height>120:
    if(age<18):
        print("ticket will be Rs20")
    elif(age>18 or age==18):
        print("ticket will be Rs50")
    elif(age<12 and height==120):
        print("ticket will be Rs10")
    elif(age>12 and age<18 and height==120):
        print("ticket will be Rs15")
else:
  print("your are not eligible")
###################################### 
print("welcome to the roller coster")
height=int(input("pleas enter the height in cm"))
bill=0 
if height>=120:
   print("your eligible for the rooler coster")
   age=int(input('please enter your age'))
   if age<12:
       print("child ticket are 55")
       bill=5 
   elif age<=18:
       print("youth tickets are 57")
       bill =7  
   else:
       print("audult ticket are $12")
       bill =12
       want_photo=input("do you want photo Y or N")  
   if want_photo=='Y':
       bill+=3
       print("your total bill will be{bill}")
   else:
       print("your total bill will be{bill}")
else:
    print("sorry you need to grow taller")      
##############################################
#we want to create 
users=["admin","manager","worker","staff"]
for user in users:
    if user=="admin":
        print("hello admin")
    elif user == "manager":
        print("hello manager")
    elif user == "worker":
        print("hello worker") 
    else:
         print("hello")
         
#############################################
  #password picker 
import string
adjectives=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green','blue','purpal','fiuffy','white','proud','brave'] 
#pic out the none
nouns=['apple','ball','dianasor','toster','goat','dragon','hammer','duck','panda']
#pick the words
import random
adjective = random.choice(adjectives)
noun = random.choice(nouns)
#select the number
number = random.randrange(0,100)
#select a special character
special_char=random.choice(string.punctuation)
#create new secure password
password = adjective + noun + str(number) + special_char
print('your new password is:%s'%password)
# 
while True:
 adjective = random.choice(adjectives)
noun=random.choice(nouns)
number = random.randrange(0,100) 
special_char = random.choice(string.punctuation)
password = adjective + noun +str(number) + special_char
print('your new password is:%s'%password)   
 responce= input(would you like generate another password?type y or n)
if responce == 'n'-:
    break
###########################################
print("welcome to the pizza hut")
size=input("enter the size of pizza S,M,L")
chees=input("enter you want to chees y/n") 
pipanior=input(" enter you want to pipanior y/n")
bill=0
if size=="S":
    print("the price of pizza 15")
    bill=5
elif size=="M":
    print("the price of pizza 20")
    bill=10
else:
     print("the price of pizza is25")
     bill=15
if chees==y:   
     bill+=1 
if pipnior==y:
     bill+=3
     print("print your bill",bill)
else:
     print("sorry")
###############################################     
     


   
         

 