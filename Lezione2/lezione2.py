# Philip Vicari
# 18/04/2024
#2-3 Personal Message: use a variable to represent a person's name, and print a message to that person. 
#your message should be simple like this: "Hello Eric, would you like to learn some python today?"


#name = "Mario"
#print(f"Hello", (name), ", would you like to learn some python today?")


#2-4 Use a variable to represent a person's name, and then print tht person's name in uppercase, lowercase and titlecase
name : str= "Federico"
uppername= name.upper()
lowername= name.lower()
titlename= name.title()
print(uppername, lowername, titlename)
#2-5 
#2-6
#2-8 Assign the value "python_notes.txt" to a variables called filename. 
#Then used the remoesuffix() method to display the filename without the file extension, like some file browsers do
filename : str= "python_notes.txt"
print(filename.removesuffix(".txt"))
#3-1
names=["Damiano", "Gioia", "Riccardo"]
print(names[0])
print(names[1])
print(names[2])

#3-2
print(f"ciao", (names[0]), "!")
print(f"ciao", (names[1]), "!")
print(f"ciao", (names[2]), "!")
#3-3
#3-4
Person=[ "Batman", "Brad Pitt", "Mike Tyson"]
print(f"Hello", (Person[0]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[1]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[2]), ", I would like to invite you in a dinner")