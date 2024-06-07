class Prodotto:
    def __init__(self, nome:str, quantità:int) -> None:
        self.nome= nome
        self.quantità= quantità
class Magazzino:
    def __init__(self) -> None:
        self.magazzino:list
    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.magazzino.append(prodotto)
        return self.magazzino
    def cerca_prodotto(self, nome:str):
        for prod in self.magazzino:
            if nome == prod:
                return nome
    def verifica_disponibilità(self, nome:str):
        for prod in self.magazzino:
            if prod==nome:
                return f"il prodotto {prod}è disponibile in negozio"
            else:
                return f"Questo prodotto non esiste"

oggetto_1=Prodotto("Bottiglia", 6)
print(oggetto_1= Magazzino.aggiungi_prodotto(oggetto_1))
