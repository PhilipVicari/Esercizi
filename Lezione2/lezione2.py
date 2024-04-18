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