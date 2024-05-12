#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
class restaurant:
    def __init__(self, name, cuisine_type) -> None:
        self.name= name
        self.cuisine_type= cuisine_type
    def describe_restaurant(self):
        print("\n", self.name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print(f"The", self.name, "is open!")
restaurant1=restaurant("La Parolaccia", "Roman cuisine")
restaurant2=restaurant("Da Vittorio","Roman cuisine")
restaurant3=restaurant("Zi teresa","Roman cuisine")
restaurant4=restaurant("Fratini","Roman cuisine")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant4.describe_restaurant()
restaurant4.open_restaurant()
