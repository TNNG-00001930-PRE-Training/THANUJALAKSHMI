
1. Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
2. Use list comprehension to construct a new list but add 6 to each item.
3. Using list comprehension, construct a list from the squares of each element in the list.
4. Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
5. Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.'''

```python
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

#Type your answer here.
#1. Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
lst=[]
lst=[x for x in range(1200,2000,130)]
#2.Use list comprehension to construct a new list but add 6 to each item.
lst1=[x+6 for x in lst]
#3. Using list comprehension, construct a list from the squares of each element in the list.
lst2=[x**2 for x in lst1]
#4. Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
lst3=[x**2 for x in range(10) if x**2>50]
#5. Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.
lst4=[i.upper() for i in dict if dict[i]<500]

print(lst4)

```