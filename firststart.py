# První kód: Uložení uživatelského vstupu
jmeno = input("Pro začátek zadejte své jméno: ")
with open("jmeno.txt", "w") as soubor:
    soubor.write(jmeno)