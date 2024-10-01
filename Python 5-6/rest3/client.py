import requests,json, sys

base_url = "http://127.0.0.1:8080"

def GetDatiCittadino():
    nome = input("quale è il nome")
    cognome = input("quale è il cognome")
    dataN = input("Quale è la data di nascita")
    codF = input("quale è il codice fiscale?")
    datiCittadino = "mammeta" 
    return datiCittadino

print("Operazioni disponibili:")
print("1. Inserisci cittadino (es.atto di nascita) )")
print("2. Richiedi cittadino( cert. Residenza)")
print("3. Modifica cittadino(cambio di residenza)")
print("4. Elimina cittadino(es.trasferimento a un altro comune)")
print("5. Esci")
soper = input("Cosa vuoi fare?")
while soper!="5":
    if soper == "1":
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url,json=jsonDataRequest)
        try:
            #print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except Exception:
            print("Problemi di connessione con il server, riprovare")
    if soper == "5":
        print("Buona Giornata")
        sys.exit()
print("Operazioni disponibili:")
print("1. Inserisci cittadino (es.atto di nascita) )")
print("2. Richiedi cittadino( cert. Residenza)")
print("3. Modifica cittadino(cambio di residenza)")
print("4. Elimina cittadino(es.trasferimento a un altro comune)")
print("5. Esci")
