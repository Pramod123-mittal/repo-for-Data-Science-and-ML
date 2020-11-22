#SETS
'''A SET IS A UNORDERED COLLECTION DATA THAT IS ITERABLE,MUTABLE
AND HAS NO DUPLICATE ELEMENTS. PYTHON SET CLASS REPRESENTS THE
MATHEMEATICAL NOTION OF SET. THIS IS BASED ON A STRUCTURE 
KNOW AS has table'''


#defining an empty set
set_vars = set()
print(set_vars)
print(type(set_vars))

set_vars = {1,2,3,4,5,6,1,2}
print(set_vars)
set_vars2 = {"ironman",'avengers','hitman'}

#print(set_vars2[0])  #TypeError: 'set' object is not subscriptable
# sets  does not support indexing

set_vars2.add("hulk") # for adding a new value
print(set_vars2)


set1={"Avengers","IronMan",'Hitman'}
for value in set1:
    print(value)
set2={"Avengers","IronMan",'Hitman','Hulk2'}
print(set2.difference(set1))
print(set2)
print(set2.intersection(set1))
set2.difference_update(set1)
print(set2)

#dictionary
'''A DICTIONARY IS A COLLECTION WHICH IS UNORDERD AND CHANGABLE
AND INDEXED. IN PYTHON, DICTIONARIES ARE WRITTEN ARE WITH CURLY
BRACKETS AND THEY HAVE KEYS AND VALUES'''

#defining a empty dic

dic = dict()
print(type(dic))
my_dict={"Car1": "Audi", "Car2":"BMW","Car3":"Mercidies Benz"}
print(my_dict["Car1"])

for x in my_dict: #retrieving keys
    print(x)
for value in my_dict.values(): #retriving values
    print(value)

for key,value in my_dict.items(): #retriving keys and values
    print(key,value)

my_dict["car4"] = "Swift dezire"
print(my_dict)
my_dict["Car4"] = "Swift dezire"
print(my_dict)

my_dict["Car1"] = "Scorpio"
print(my_dict)
my_dict["car1"] = "scorpio"
print(my_dict)


#nested dictionary
car1_model={'Mercedes':1960}
car2_model={'Audi':1970}
car3_model={'Ambassador':1980}

car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model}

print(car_type['car1'])

print(car_type['car1']['Mercedes'])

#tuples
'''1 TUPLES ARE IMMUTABLE
    =>means whole tuple can be changed
    =>but single items can't be changed
2 INDEXING IS POSSIBLE IN TUPLES'''

## create an empty Tuples
my_tuple=tuple()
print(type(my_tuple))
my_tuple=("Krish","Ankur","John")

#my_tuple[0] = 'bhai' #TypeError: 'tuple' object does not support item assignment
#but single items can't be changed
#print(my_tuple)
'''
my_tuple = ('Hello','World')
print(my_tuple)
this is possible'''


## Inbuilt function
print(my_tuple.count('Krish'))
print(my_tuple.index('Ankur')) 






