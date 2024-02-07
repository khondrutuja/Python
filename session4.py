# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:10:07 2023

@author: Dell
"""

#write python program to add all the itam in the list
def sum_lst(items):
   sum=0
   for x in items:
      sum=sum+x
   return sum
lst1=[2,5,7,9,15]
print(sum_lst(lst1))  
########################################
#write python program to multiply all the item in the list
def mul_lst(items):
    mul=1
    for x in items:
        mul=mul*x
    return mul
lst1=[1,2,3,4]
print(mul_lst(lst1))
##########################################
#write python program to get largest number from the list
lst1=[1,2,3,4,5,]
print(max(lst1))
#############################################
#wrrite python program to get  smallest no from the list
lst1=[1,2,3,4,5,]
print(min(lst1))
#########################################
#write  a python program to count the no of string to satisfy the condition  that the string length 
#is 2 or more and 1st and last character should be same
 
def match_words(words):
     ctr=0
     for word in words:
         if len(word)>2 and word[0]==word[-1]:
             ctr+=1
     return ctr
print(match_words(['abc','aba','xyz','1221']))
########################################
#write a python program to get a list sorted in incresing 
#order by the last element in each tuple from given list of 
#non empty tuple
#sample list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
#expected result=[(2,1),(1,2),(2,3),(4,4),(2,5)]

def last(n):
    return n[-1]
    return[-1]
def sort_list_last(tuples):
    result=sorted(tuples,key=last)
    return result
print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))
##########################################
#write program to remove duplicate from given list

a=[10,20,30,40,50,10,30,90] # creating a list
b=set(a)                    #convert that list in to set becouse set not allowd doublicate item
c=list(b) #again convert that set in to list and print it
print(c)
#############################################
#Write python program to copy a list
original_list=[10,20,30,44]
new_list=list(original_list)
print(original_list)
print(new_list)
#######################################
#need to retry
#write python program to find the list of word that is 
#longer than n from given list of word
def long_words(n,str):
    word_len=[]
    txt=str.split(" ")
    for x in txt:
        if len(x)>n:
            word_len.append(x)
    return word_len
print(long_words(3,"the quick brown fox jump over the lazy dog"))
############################################
#write a python function that takes two list and returns 
#true if at least one comman entity
def  comman_data(list1,list2): # create a function and pass lst1 & lst2
    result=False
    for x in list1:
        for y in list2:
           if x==y:
                result = True
                return result
print(comman_data([1,2,3,4,5],[5,6,7,8,9]))            
print(comman_data([1,2,3,4,5],[6,7,8,9,10]))      
##########################################
#intersection of two list
#we use convert list in two set because  intersection ,union,difference are set opration
lst1=[1,2,3,4]      
lst2=[1,2,5,6]
b=set(lst1)
c=set(lst2)
print('intersection', b&c)
#############################################
#write a python program to calculate difference between two list
lst1=[1,3,5,2,7]
lst2=[1,2,6,8,3]
diff1=list(set(lst1)-set(lst2))
diff2=list(set(lst2)-set(lst1))
total_diff=diff1+diff2
print(total_diff)
###################################################
#write a python to convert list to string
s=['a','b','c','d']
str=''.join(s) #it is use to join the item in the list
print(str)
################################
#write python of program to find out index of item in specific list.
num=[10,30,4,-6]
print(num.index(30)) # it is use to find out index of specific number
##################################################
#write a python program to append list to the second list
lst1=[1,2,3]
lst2=[4,5]
final_lst=lst1+lst2
print(final_lst)
