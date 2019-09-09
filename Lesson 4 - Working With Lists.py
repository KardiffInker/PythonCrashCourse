#!usr/bin/env Python3
#python Crash Course - Chapter 4

# Loops through an entire list
magicians =['harry houdini' , 'dynamo' , 'derren brown', 'Pen & Teller', 'david blane']
for magician in magicians:
	print ('\t' + magician.title() + ' I Like their magic!' ) 
print ("I really likez magic!")
 
animals = [ 'dog', 'cat', 'jaguar' ]
for animal in animals:
	print('\tA ' + animal + ' would make a great pet.')
print("They all have paws!")

pizzas=['Neapolitan', 'New York-Style','Mexican','Hawaiian', 'Meatball', 'Tandorri','Satay Pizza','Mushroom','Chicken','Beef']
for pizza in pizzas:
	print('\tI like ' + pizza + '.')
print ('I like pizza!')

#4.3 Count to Twenty
for number in range(0,21):
	print (number)
#4.4/5 Count to a million
million=[]
for number in range(0, 1000000):
	million.append(number)
#	print (number)
print ('Min: '+ str(min(million)) + ' Max: ' + str(max(million)))
#4.6 Odd Numbers 1 to 20
for x in range(1,21,2):
	print (x)
oddnumbers = [x for x in range(1,21,3)]
print (oddnumbers)
#4.7 Make a list of multiples of three to 30.
for x in range (0,31,3):
	print(x)
#4.8/9 Make a list of cubed number between 1 to 10
x=0
cubed = [x**3 for x in range(1,11)]
for x in cubed:
	print(x)
print (cubed)
#4.10 Slices
myFavFoods = ['chips', 'curry','rice','pasta', 'garlic bread']
print ('The first three items in the list are: ' + str(myFavFoods[:3]))
print ('The middle three items in the list are: ' + str(myFavFoods[1:4]))
print ('The last three items in the list are: ' + str(myFavFoods[-3:]))
#4.11 copy lists
freindsPizzas =pizzas[:]
pizzas.append('Chocolate')
freindsPizzas.append('Strawberry')
print ("My favourite pizza's are: " + str(pizzas))
print ("My freind's pizza's are: " + str(freindsPizzas))
#4.12 Write two more for loops
for x in cubed:
	print(x)
for x in pizzas:
	print(x)
#4.13 Tuples- A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
foods = ('chips','sausage','egg','ham','bacon')
for food in foods:
	
	print(food)
print(foods[1] + ' : foods[1]')#del (foods[1]) //Tuples can';t be modified but can be re-written
foods = ('spagbol','llasangne','Enchildias')
print(foods[1] + ' : Modified foods [1]')
#foods.append('Chicken & Bacon') tuples can't append
print (foods[-1])
foods = foods + ('Chicken & Bacon',) #However you can just add to a tuple
print (foods[-1])
#Storing a tuple inside a tuple
users= ('Joe','32','Dev',('Ice Cream', 'Chocolate'))
print (users)
print (str(users[3]) + ' Get Tuple')
print (str(users[3][1]) + ' Get Value inside the tuple inside tuple.')
print ('~~~MENU~~~')
for food in foods:
	print (food) 
foods =	(('Ice Cream', '£1.95'),('Chocloate Bar','50p'))
print ('~~~Menu~~~')

b=0
while b< len(foods) :
	print (str(foods[b][0]) + 'Price ' + str(foods[b][1]))
	b=b+1
