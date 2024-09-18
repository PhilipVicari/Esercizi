def mappa_parole_a_lunghezza(words: list) -> dict:
    contaparole={}
    counter=0
    for w in words:
        contaparole={w}
        for l in w:
            counter+=1
            contaparole={w, counter}
    return contaparole

print(mappa_parole_a_lunghezza(["apple", "banana", "cherry"]))