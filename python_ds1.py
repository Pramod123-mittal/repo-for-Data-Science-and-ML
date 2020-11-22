#string
my_str = 'pramodmittal'

print(my_str.isalnum())  #check if all chars are numbers
print(my_str.endswith('l'))  #check if strings ends with l
print(my_str.isdigit()) #check if string contains digit
print(my_str.isupper()) #check if contains upper case
print(my_str.islower()) #check if string contains lower case
print(my_str.istitle()) # check if string contains title words
print(my_str.startswith('p')) # check if string starts with p
print(my_str.isalpha()) # check if all char in string are alphabetic


#list
'''A LIST IS A DATA STRUCTURE IN PYTHON THAT S CHANGABLE AND MUTABLE
,ORDERED SEQUENCE OF ELEMENTS. EACH ELEMENT OR VALUE THAT IS INSIDE 
OF A LIST IS CALLLED A ITEM. JUST AS STRINGS ARE DEFINED AS 
CHARACTERS BETWEEN QUOTES, LIST ARE DEFINED BY HAVING BETWEEN THE 
SQUARE BRACKETS '''

lst = list()
print(type(lst))

lst1 = ['maths','chemistry',100,200,300]
lst1.append(150) #append at the end poof list
lst1.insert(2,"physics") # can add any position
print(lst1)
print(lst1[:])
print(lst1[2:])
print(lst1[1:4])
lst1.append(["RCC","SOM"])
print(lst1)


lst2 = [1,2,3,4,5,6,7,8,8]
lst2.extend([9,10]) #not append as nested list
print(lst2)
print(lst2.pop())  #remove the element from last index
print(lst2)
print(lst2.count(8))  #count the occurence of 8 in list
print(lst2.index(8)) # get the index of 8
print(min(lst2))  #get the min value from list
print(max(lst2))  # get maximum value from list
