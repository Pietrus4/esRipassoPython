dizionario = {"a":1, "b":2, "c":3}
#dizionarioScambiato = dizionario.__reversed__
dizionarioScambiato = {valore: chiave for chiave, valore in dizionario.items()}
print(dizionarioScambiato)