"""
Variable = a name or a reference of any data stored in the memory is called variable. the variable should not have a space
any special characters at the beginning of its name.
for eg = name = 'manohar naik' name here is variable storing the data manohar naik

"""
"Install python and pycharm & Python"

print('Your Names')
"=================================================================================================="
"""
Integer (numbers) in Python, There are three numeric types in Python: A data that can perform any mathematical calculation is an int/number in python
int  = A roundup Number Eg. 1, 2, 3, 4, 5, 100, 200, 2000
float = A number with a perfect decimal of it Eg. 1.1, 2.2, 3,1,100,01

"""

number = 10 # int Number
fnumber = 10.0 # Float number

"Checking datatype of number & fnumber"
print(type(number))  # <Class int>
print(type(fnumber)) # <Class Float>

"# Working with int and operators[ +, -, *, /]"
# Pluse (+)
num1 = 10 
num2 = 20 
result = num1 + num2
print(result)    # 10 + 20 = 30

# Pluse (-)
num1 = 10 
num2 = 20 
result = num1 - num2
print(result)    # 10 - 20 = -10

# Pluse (-)
num1 = 10 
num2 = 20 
result = num1 - num2
print(result)    # 10 - 20 = -10

# into (*)
num1 = 10 
num2 = 20 
result = num1 * num2
print(result)    # 10 * 20 = 200

# divide by (/)
num1 = 10 
num2 = 20 
result = num1 / num2
print(result)    # 10 / 20 = 0.5

# divide by (//)
num1 = 10 
num2 = 20 
result = num1 // num2

print(result)    # 10 / 20 = 0


"=================================================================================================="

"""
String Or Text : The data which is a collection of characters or collections is called as string. 
Here the values will have naming, not any values. and strings will be defied in python with “ ” or ‘ ’  marks

Method as str()
class as str
data as ''
"""

# Creating String Data:

name = 'manohar naik'
phase = """hi dear student
how are u guys doing"""

print(type(name))   #---> <Class str>
print(type(phase))  #---> <Class str>

# Adding data to a empty string
str_data="" # empty list
str_data="manohar"+"naik" # adding 2 string or collection of data
print(a)   # ----> manoharnaik

# String Method

str_data.index("m")     # ---> 0 gives the position of the letter in the list
str_data.join("mr")     # ---> [mrmanohar, mrnaik] Join the data in the seq to all the strin seq
str_data.count("m")     # ---> 1 Count the number of time a character is used in the string
str_data.split()        # ---> string to list[] Split the string and conver into list
str_data.isalpha()      # ---> True / False check the Alpha in the string
str_data.isnumeric()    # ---> True / False Check the number in the list
str_data.format()       # ---> formating data / Arraange the veriable in the positional manner
str_data.format_map()   # Conver the data into dictionery
str_data.casefold()     # Conver the data into lower case
str_data.capitalize()   # Convert the word's first letter into upper case
str_data.upper()        # Convert all the character to upper case
str_data.encode()       # encode the data
str_data.strip()        # Remove the spaces from left & right in the String
str_data.center()       # returns the center value in the list
str_data.find()         # returns the index position of the text or word
str_data.endswith()     # returns the end letter of the string
str_data.startswith()   # returs the first case of the string
str_data.islower()      # ---> True / False identify the lower case in the string
str_data.isupper()      # ---> True / False identify the upper case in the string

newstr=str() # copping the methed of string 



"=================================================================================================="
"""
List the data which we store in sequence or in the order is called list type data or array type of data and Lists are used to store multiple items in a single variable.

-> Ordered
-> Changeable
-> Accept Duplicates
-> Store data n-1

syntax of list = variable name = []
class list
method = list()

eg. Below
"""

listdata = ['manohar',100,"naik",'school']

"""
The above listdata has some items inside of various data types which store in position wise starting from 0 to n.
the 0 th position data if "manohar" and n-1 is "school"

list has index position of data as well as ordered and take data continuously till its limitation
"""
# Operation of List

"Adding items in List: list.append(data here str / int / tuple / dict)"
listdata.append('new data')
print(listdata) # ['manohar',100,"naik",'school',''new data]

"Knowing index position of the item in list : list.index('item of list')"
print(listdata.index('manohar')) # 0

"Updating the data in list : list[index] = new value / data"
listdata[0] = 'naik'
print(listdata) # 

"Deleting the data from list using index : list.pop(index of the list)"
listdata.pop(1) 
print(listdata)  # ['manohar',"naik",'school',''new data]

"Deleting the data from list directly by item or object : list.remove(item name)"
listdata.remove('manohar') # ["naik",'school',''new data]

"Clearing all the items in the list : list.clear()"
listdata.clear()
print(listdata) # []

"Reverse Order data arranging in list : list.reverse()"
datalist = [1,2,3,4,5,6,7,8]
datalist.reverse()
print(datalist) # [8,7,6,5,4,3,2,1]

"Copying data to another list or on the new list : newlist =list.copy()"
newlist =datalist.copy()
print(newlist) # [1,2,3,4,5,6,7,8]

"Count the items of list : list.count()"
count = datalist.count()
print(count) # 8

"Adding another list or Sequence type data to another list : listdata.extend(another list / seq. type data range)"
datalist.extend([1,2,3,4,5,6,7,8]) # seq data / list type data
datalist.extend(set(listdata))
print(datalist) # [,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,'manohar',"naik",'school',''new data]

"Data inserting at index level in list : list.insert(0,'new item str / int')"
datalist.insert(0,'idiot')

"Sorting the data : list.sort('sorting order fuction)"
datalist.sort() # continued more in fuct. level

a=datalist.sort() # It required an object to store the procedure
print(a)  # 1 to n-1

"=================================================================================================="

"""
Tuple data are similar to list but it is unchangeable, same here also we will store the date in seq. manner.

-> Ordered
-> Unchangeable
-> Allow Duplicates
-> Pass secure in conversion

Method = tuple()
class = tuple
a=()
"""

# Creating Tuple data
tuple_data = ("atleast one data inside",)
tuple_data.count()      # ---> Counts the items inside the tuple
tuple_data.index()      # ---> retuns the Position of the object

# adding 2 Tuple
tupled = tuple_data + tuple_data


"====================================================================================================="

"""
Set Datas are used to store multiple items in a single variable. A set is a collection which is unordered,
unchangeable*, and unindexed. but we can add the data and remove the data from the group

Method set() ---> Copy methods to the new object
class set
set_data = {1,}
"""

set_data = {"a","b","c","d","e","f"}
subset_data ={"a","b","c","d"}

set_data.add()                          # ---> Add an item to the Set
set_data.clear()                        # ---> Clear the set and keep it empty
set_data.copy()                         # ---> Copy the data to the other set
set_data.difference()                   # ---> retun the non-comman value from the 2 set
set_data.difference_update()            # ---> Delete the comman items from difrent sets
set_data.discard()                      # ---> Eliminate the particuler items from the group
set_data.intersection()                 # ---> Retun the Comman items from the 2 sets
set_data.intersection_update()          # ---> filter the item that are comman from diffrent set
set_data.isdisjoint()                   # ---> Gives True / False in any item of another Set is if it is exist(False) if not (True)
set_data.issubset()                     # ---> Check the Set if it is a part of the its own and gives True / False
set_data.issuperset()                   # ---> Cheks the self item with another and give it its own Boss set
set_data.pop()                          # ---> remove the last item in the set
set_data.remove()                       # ---> remove the Object in Set
set_data.symmetric_difference()         # ---> Hari Explanation on the Symmetric behaviour
set_data.symmetric_difference_update()  # ---> Hari Explanation on the Symmetric behaviour
set_data.union()                        # ---> join the 2 / more sets togerther
set_data.update()                       # ---> update the 2/ more set together

"====================================================================================================="

"""
A dictionary is a collection which is ordered, changeable and do not allow duplicates. initialy dictionery is unordered
python has consistancy in devlaping the sytem and this all featurs are getting change

Method = dict()
Class = dict
data = {'data':'anything here'}

"""

dict_data = {'manohar.naik':'admin@2021','user.name':'password'}


dict_data.clear()	                            # ---> Removes all the elements from the dictionary
dict_data.copy()	                            # ---> Returns a copy of the dictionary
a=dict.fromkeys(list / tuple,string / int)	    # ---> Returns a dictionary with the specified keys and default value
dict_data.get()	                                # ---> fatch the value of key / search word exist in the dictionery
dict_data.items()                               # ---> Provide the list of items only
dict_data.keys()	                            # ---> provide the keys of dictionery
dict_data.pop()                                 # ---> Eliminate the item of perticuler Key
dict_data.popitem()                             # ---> Removes the last inserted key-value pair
dict_data.update({dict})	                    # ---> Updates the dictionary with the specified key-value pairs
dict_data.values()	                            # ---> Returns a list of all the values in the dictionary

"====================================================================================================="

"""
Next Conditional Statements - Monday

if(conditon==True / False):
elif(conditon==True / False):
    else:

While (condition==True / False):
    Brake

"""