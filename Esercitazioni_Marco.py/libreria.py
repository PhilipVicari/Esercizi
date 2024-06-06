#Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
#Classi:
#- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

#- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#    Metodi:
#    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.
#
#    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.
#
#    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.
#
#    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.
#
#Test Cases:
#- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
#- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
#- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
#- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.

class Libro:
    def __init__(self, title, author, state_of_borrow=True) -> None:
        self.title= title
        self.author= author
        self.state_of_borrow= state_of_borrow
class Biblioteca:
    def __init__(self) -> None:
        self.catalogo=[]
        libro={}
    def __str__(self) -> str:
        return self.catalogo
    
    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return f"IL libro è stato aggiunto:{self.catalogo}"
    def presta_libro(self, title):
        for libro in self.catalogo:
            prestito:bool
            if title in libro:
                if prestito == True:
                    return "Il libro è disponibile"
                prestito= False
    def restituisci_libro(self, title):
        for libro in self.catalogo:
            prestito:bool
            if title in libro:
                if prestito==False:
                    return "Il libro è tornato disponibile"
                prestito = True