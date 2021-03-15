#################################################################################
#List functions (Append, Insert, Del, Remove)
#################################################################################
motorcycles = []

motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)

#################################################################################
#Sorting list
#################################################################################

"""these are permanant changes"""

cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.sort()
    #alphabetical
print(cars)

cars.sort(reverse = True)
    #reverse alphabetical
print(cars)

    #to do a temporary sort:
print(sorted(cars))

cars.reverse()
    #just reverses the list order
print(cars)

len(cars)
    #returns the length of list


#################################################################################
#looping through lists
#################################################################################

magicians = ['alice','david','carolina']
for mage in magicians:
    print(mage)


#making a list of numbers through looping

numbers = list(range(1,6))
print(numbers)




























