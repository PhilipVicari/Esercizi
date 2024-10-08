
#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
#Call the function, and make sure the message displays correctly.
def display_message():
    print(
        'I am going to learn functions')
display_message()
#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
#The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.
def favorite_book(title):
    print(
        "One of my favorite books is", title)
favorite_book('IT')
#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
def make_shirt(size, text):
    print(
        'The size of the shirt is:', size, '\nThe text on her is:', text)
make_shirt('large', 'Baci e Abbracci')

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size = 'large', text= 'I love Python'):
    print(
        '\nThe size of the shirt is:', size, '\nThe text on her is:', text)
make_shirt()
def make_shirt(size = 'medium', text= 'I love Python'):
    print(
        '\nThe size of the shirt is:', size, '\nThe text on her is:', text)
make_shirt()
def make_shirt(size= 'S', text= 'I love Pizza'):
    print(
        '\nThe size of the shirt is:', size, '\nThe text on her is:', text)
make_shirt()
#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
#Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city, country= ' Italy'):
    print(city, '\nis in', country)
describe_city('Venezia')

def describe_city(city, country):
    print(city, 'is in', country)
describe_city('\nRome', 'Italy')
describe_city('Paris', 'France')
describe_city('Moscow', 'Russia')


#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
#The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
def city_country(City, Country):
    print(City, ',' , Country)
city_country('\nNapoli', 'Italy')
city_country('Madrid', 'Spain')
city_country('Warszawa', 'Poland')

#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
#The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
#Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. 
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
    #"non sono riuscito a farlo"

#If the calling line includes a value for the number of songs, add that value to the album�s dictionary. Make at least one new function call that includes the number of songs on an album.
    #"non sono riuscito a farlo"
def make_album(artist, album, track='0'):
    dict={
        'Name:': artist, 'Name Album': album}
    print(
        dict)
make_album('Pinkfloyd', 'The Dark Side of the Moon', )
make_album('Metallica', 'Ride the Lightning', )
make_album('Queen', 'A Night at the Opera', '8')
#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album�s artist and title. 
#Once you have that information, call make_album() with the user�s input and print the dictionary that�s created. Be sure to include a quit value in the while loop.
while True:
    album: str = input()
    if album == 'quit':
        break
    artist: str = input()
    if artist == 'quit':
        break
    album = make_album(artist, album)
    print(
        album)
#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
messages=['Hello there!', 'Come with me', 'How are you?']
def show_messages():
    for message in messages:
        print(
            message)
show_messages()
#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it�s printed. 
#After calling the function, print both of your lists to make sure the messages were moved correctly.
messages=[
    'Hello there!',
    'Come with me',
    'How are you?'
    ]
def show_messages():
    for message in messages:
        print(
            '\n', message)
show_messages()
messages=[
    'Hello there!',
    'Come with me',
    'How are you?'
    ]
def send_messages(
        messages):
    sent_messages=[]
    while messages:
        sent_messages.extend(messages)
        messages.clear()
    print('message sent:', '\n', messages, sent_messages)
send_messages(messages)
#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
#After calling the function, print both of your lists to show that the original list has retained its messages.
#messages=['Hello there!', 'Come with me', 'How are you?']
#def send_messages(messages):
#    sent_messages=[]
#    while messages:
#        sent_messages.extend(messages)
 #   print('message sent:', '\n', messages, sent_messages)
#send_messages(messages)
            

            #"Non sono riuscito a farlo"


#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that�s being ordered. 
#Call the function three times, using a different number of arguments each time.
def sandwitches(items):
    print('the sandwitch with', items, 'was made')
sandwitches('mozzarella, meat')
sandwitches('cheddar cheese')
sandwitches('cheese, tomato')

#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. 
#All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
def build_profile(Name, Surname, Colour_hair,
                  Colour_eyes, age):
    print('\n My name is:', Name)
    print('\n My surname is:', Surname)
    print( '\n My hair are:', Colour_hair)
    print('\n My eyes are:', Colour_eyes)
    print('\n I am', age, 'y.o')
build_profile('Philip', 'Vicari', 'blonde', 'blue', 19)
#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
#It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
#Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
#Print the dictionary that�s returned to make sure all the information was stored correctly. 
def car(
        manufacturer, model, HP, 
        Engine):
    car={'Manufacturer:': manufacturer, 'Model': model, 'HP': HP, 'Engine:':Engine}
    print (car)
car('Porsche', 'GT3RS', '518', 'V6')
#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
#Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
#Import the function into your main program file, and call the function using each of these approaches:
#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn
#from module_name import *
#8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section
