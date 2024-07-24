def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    
    for key, values in da_rimuovere.items():
        while values > 0:
            if da_rimuovere[key] in lista:
                lista.remove(key)
                values-=1
    return lista


print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))


def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int: int]) -> list[int]:
    for key, value in da_rimuovere.items():
        while value > 0:
            if key in lista:
                lista.remove(key)
                value -= 1
    return lista



#     Classe del Account:
#         Attributi:
#             account_id: str - identificatore univoco per l'account.
#             balance: float - il saldo attuale del conto.
#         Metodi:
#             deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#             get_balance(): restituisce il saldo corrente del conto.
#     Classe Bank:
#         Attributi:
#             accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#         Metodi:
#             create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#             deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#             get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
    """
        class Account():
            def __init__(self, account_id: str, balance) -> None:
                self.account_id= account_id
                self.balance= 0.0
            
            def deposit_A(self, amount: float):
                self.balance= self.balance + amount
        
            def get_balance(self):
                return self.balance

        class Bank():
            def __init__(self) -> None:
                self.accounts= {}
                
            def create_account(self, account_id: str):
                self.accounts[account_id]= (account_id)

            def deposit(self, account_id: str, amount: float):
                if account_id in self.accounts:
                    self.accounts[account_id]= Account.deposit_A(amount)
            
            def get_balance(self, account_id: str):
                return self.accounts[account_id].get_balance()


        class Account:
            def __init__(self, account_id: str):
                self.account_id = account_id
                self.balance = 0.0

            def deposit(self, amount: float):
                self.balance += amount

            def get_balance(self):
                return self.balance


        class Bank:
            def __init__(self):
                self.accounts = {}

            def create_account(self, account_id: str):
                if account_id in self.accounts:
                    raise ValueError("Account already exists")
                self.accounts[account_id] = Account(account_id)

            def deposit(self, account_id: str, amount: float):
                if account_id not in self.accounts:
                    raise ValueError("Account does not exist")
                self.accounts[account_id].deposit(amount)

            def get_balance(self, account_id: str):
                if account_id not in self.accounts:
                    raise ValueError("Account does not exist")
                return self.accounts[account_id].get_balance()

        bank1= Bank()
        account1= bank1.create_account("456")
        bank1.deposit("456", 200)
        print(bank1.get_balance("456"))
    
    
    
    DA RISOLVERE
    """

"""

class Veicolo():
    def __init__(self, marca, modello, anno) -> None:
        self.marca= marca
        self.modello= modello
        self.anno= anno
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca} Modello: {self.modello} Anno: {self.anno}")

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        self.marca= marca
        self.modello= modello
        self.anno= anno
        self.numero_porte= numero_porte

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca} Modello: {self.modello} Anno: {self.anno} Numero delle Porte: {self.numero_porte}")

class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        self.marca= marca
        self.modello= modello
        self.anno= anno
        self.tipo= tipo
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca} Modello: {self.modello} Anno: {self.anno} Tipo: {self.tipo}")
        
        
veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo() 
auto.descrivi_veicolo()
moto.descrivi_veicolo()
"""

def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    
    while tempo >= 0:
        print(f"Tempo {tempo}, altezza: {altezza}")
        tempo +=1
        altezza= altezza + velocita
        velocita= velocita - 96
        if altezza < 0:
            altezza = altezza * -0.5
            velocita = velocita * -0.5
            rimbalzi += 1
            if rimbalzi == 5:
                print(f"Tempo {tempo}, Rimbalzo!")
                break
            tempo+=1
            print(f"Tempo {tempo}, Rimbalzo!")
    return " "
print(rimbalzo())





class RecipeManager:
    def __init__(self) -> None:
            self.recipe= {}

    def __str__(self) -> str:
        return str (self.recipe)
    
    def create_recipe(self, name, ingredients):
        if name in self.recipe:
            return f"La ricetta esiste già"
        else:
            self.recipe[name]=ingredients
            return self.recipe

    def add_ingredient(self, recipe_name, ingredient):
        if ingredient in self.recipe:
            return f"l'ingrediente inserito esiste già oppure la ricetta non esiste"
        else:
            self.recipe[recipe_name].append(ingredient)
            return self.recipe

    def remove_ingredient(self, recipe_name, ingredient):
        if ingredient not in self.recipe or recipe_name in self.recipe:
            return f"l'ingrediente inserito esiste già oppure la ricetta non esiste"
        else:
            self.recipe[recipe_name].remove(ingredient)
            return self.recipe
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):

        if old_ingredient not in self.recipe or recipe_name in self.recipe:
            return f"l'ingrediente inserito esiste già oppure la ricetta non esiste"
        else:
            self.recipe.replace(old_ingredient, new_ingredient)
            return self.recipe
    def list_recipes(self):
        return self.recipe.keys()
    
    def list_ingredients(self, recipe_name):
        return self.recipe.values()
    
    def search_recipe_by_ingredient(self, ingredient):
        for i in self.recipe:
            if ingredient in self.recipe.values():
                return self.recipe(ingredient)
        else:
            return"Errore"
        
        
manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))



class Movie():
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented
    def rent(self):
        if self.is_rented == False:
            self.is_rented==True
        else:
            print(f"Il film {self.title} è già noleggiato")
    def return_movie(self):
        if self.is_rented == True:
            self.is_rented==False
        else:
            print(f"Il film {self.title} non attualmente noleggiato")
class Customer():
    def __init__(self, customer_id:str, name:str, rented_movies:list[Movie]) -> None:
        self.customer_id=customer_id
        self.name= name
        self.rented_movies=rented_movies
    def rent(self, movie:Movie):
        if self.is_rented == False:
            self.rented_movies.append(movie)
        else:
            print(f"Il film {self.title} è già noleggiato")
    def return_movie(self, movie:Movie):
        if self.is_rented == True:
            self.is_rented==False
        else:
            print(f"Il film {self.title} non attualmente noleggiato")