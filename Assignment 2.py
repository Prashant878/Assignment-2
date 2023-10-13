#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# # Question-1
# Write a Python for loop that prints the numbers from 1 to 10.

# In[1]:


a=(1,2,3,4,5,6,7,8,9,10)

for item in a:
    print(item)

    #Another method we can run/print this   

for x in range(1,11):
    print(x,end='')


# # Question 2
# Create a list of fruits (e.g., ["apple", "banana", "cherry"]) and write a for loop to print each fruit in the list.

# In[2]:


fruits_name=['Mango','Apple','Kiwi','Grapes']
for item in fruits_name:
    print('My favourite fruit is: ',item)


# # Question 3
# Write a Python program that calculates the sum of all even numbers from 1 to 50 using a for loop.

# In[1]:


even_num_sum=0  #variable to store sum of even numbers

for x in range(1,51):
    if x%2==0:              #checking if number is even
        even_num_sum+=x

print("the sum of all even numbers from 1 to 50:",even_num_sum)
    


# # Question 4
# Create a list of integers, and using a for loop, find and print the largest number in the list.

# In[16]:


#list of integers
integers=[-4,-3,-2,-1,0,1,2,3,4,5,6]

for x in integers:
    x=max(integers)
           
print("The largest integer in the list is:",x)

#Another method we can use
print('\n')
listi=range(0,21)
list_i=list(listi)
print(list_i)
for x in list_i:
    print("The largest numbe in the lis is:",max(list_i))
  


# # Question 6
# -Write a Python program that takes a list of dictionaries, where each dictionary represents a person with keys "name" and "age." Find and print the average age of all the people in the list.
# 

# In[17]:


data=[]

person1={"name":"Jhon",
        "age":"25"}
data.append(person1)
person2={"name":"harry",
        "age":"21"}
data.append(person2)
person3={"name":"david",
        "age":"23"}
data.append(person3)
person4={"name":"amber",
        "age":"27"}
data.append(person4)
person5={"name":"luke",
        "age":"20"}
data.append(person5)
print(data,"\n")
agedata=[]
for x in data:
    agedata.append(int(x["age"]))
print("The give age data is:",agedata)
avgage=(sum(agedata))/5
print("The average age is:",avgage)


# # Question 7
# Create a dictionary representing a simple inventory system for a store. Implement a function that allows you to update the quantity of items in the inventory by specifying the item name and the new quantity.

# In[18]:


inventory = {'Egg': 3, 'Milk': 5}

print("original dictionary: ", inventory)

inventory['Egg'] = 10  # existing key, overwrite
inventory['Bread'] = 8  # new key, add
inventory['Chips'] = 5  # new key, add 

print("updated dictionary: ", inventory)


# In[ ]:




