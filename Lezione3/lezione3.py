#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
#For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
favourite_pizza=["pizza margherita", "pizza diavola", "pizza con le patate"]
for elem in favourite_pizza:
    print(f"This", (elem), "is amazing")
print("I really like pizza!!!")
#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. 
#You could print a sentence, such as Any of these animals would make a great pet!
mammiferi=["cat", "dog", "fox"]
for animal in mammiferi:
    print(f"the", (animal), "would make a great pet")
print("Any of these animals are mammals")
#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
count=1
while count <=20:
    count+=1
    print(count)
#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print
l=[]
#for i in range(1000001):
    
 #   l.append(i)
#print(l)
#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.





#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
l=[]
for i in range(1,20,2):
    l.append(i)
print(l)
#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
l=[]
for i in range(3, 33, 3):
    l.append(i)
print(l)
#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
l=[]
for i in range(1,11):
    cube= i**3
    l.append(cube)
print(l)
#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
mammiferi=["cat", "dog", "fox", "elephant", "hippo", "bunny", "wolf", "pig", "horse"]
f_numbers=slice(0,3)
m_numbers=slice(3,6)
l_numbers=slice(6,9)
print(f"the first three items are:", mammiferi[f_numbers])
print(f"the first three items are:", mammiferi[m_numbers])
print(f"the first three items are:", mammiferi[l_numbers])
#My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
#Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
my_pizzas=["pizza margherita", "pizza diavola", "pizza con le patate", "pizza capricciosa"]
friends_pizzas=["pizza margherita", "pizza diavola", "pizza con le patate", "pizza wurstel e patate"]
for m_pizza in my_pizzas:
    print(f"This are my favourite pizzas:", (m_pizza))
for f_pizza in friends_pizzas:
    print(f"This are my friend's favourite pizzas:", (f_pizza))
#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.
