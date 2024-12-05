import time
import os
import random
import subprocess



# Načtení jména uživatele
with open("jmeno.txt", "r") as soubor:
    jmeno = soubor.read().strip()

# Proměnné
hekeror = random.randint(100000, 9999999999999)
connected_server = None


# Základní přivítání
def welcome():
    print("Vítej v hackovacím simulátoru!")
    print("Použij příkazy, abys splnil úkoly.")
    print("Zadej 'help' pro seznam dostupných příkazů.")
    print()

# Funkce pro příkazy
def help_command():
    print("Dostupné příkazy:")
    print("  scan       - Naskenuje síť a zobrazí dostupné servery.")
    print("  connect    - Připojí se k serveru (např. 'connect FBI').")
    print("  hack       - Pokusí se hacknout server.")
    print("  gui        - Spustí grafické rozhraní.")
    print("  exit       - Ukončí simulátor.")
    print()

def zabavnehek():
    vgal = 0
    print("Spouštím Metasploit-Framework Console")
    time.sleep(5)
    print("Zadejte název serveru:")
    input(">> ")
    print("Hackování...")
    time.sleep(30)
    print("Hackování dokončeno!")
    vgal += 1  # Zvýšení počtu hacků
    with open("a.txt", "a") as soubor:
        soubor.write(f"Hack {vgal}: {connected_server}\n")

def scan():
    print("Skenuji síť...")
    time.sleep(2)
    print(f"Nalezené servery:")
    print(f"  [1] fbi")
    print(f"  [2] school")
    print(f"  [3] googledrive")
    print()

def connect(server_name):
    global connected_server
    servers = ["fbi", "school", "googledrive"]
    
    # Debug: Zobrazení názvu serveru, který uživatel zadal
    print(f"Pokouším se připojit k serveru: {server_name}")
    
    if server_name in servers:
        print(f"Připojuji se k {server_name}...")
        time.sleep(2)
        connected_server = server_name
        print(f"Úspěšně připojeno k {server_name}.")
        print()
    else:
        print("Server nebyl nalezen. Zkus 'scan' pro seznam dostupných serverů.")
        print()
vgal = 0
def hack():
    global vgal
    if connected_server is None:
        print("Nemáš připojení k žádnému serveru. Použij příkaz 'connect'.")
        print()
        return

    print(f"Pokouším se hacknout {connected_server}...")
    time.sleep(3)

    outcome = random.randint(1, 3)  # Náhodný výsledek hackování
    if outcome == 1:
        print(f"Úspěch! Server {connected_server} byl hacknut.")
        vgal += 1  # Zvýšení počtu hacků
        with open("a.txt", "a") as soubor:
            soubor.write(f"Hack {vgal}: {connected_server}\n")
    elif outcome == 2:
        print(f"Server {connected_server} byl kvůli bezpečnosti vypnut.")
        print(f"Kód chyby: {hekeror}")
    else:
        print("Stroj nedokázal automaticky hacknout server.")
        zabavnehek()



# Hlavní smyčka hry
def main():
    welcome()
    while True:
        command = input(f"{jmeno}@hacker-pc:~$ ").strip().lower()
        
        if command == "help":
            help_command()
        elif command == "scan":
            scan()
        elif command.startswith("connect"):
            try:
                _, server_name = command.split(maxsplit=1)
                connect(server_name)
            except ValueError:
                print("Použití: connect <název_serveru>")
                print()
        elif command == "hack":
            hack()
        elif command == "exit":
            print("Ukončuji simulátor...")
            break
        else:
            print("Neplatný příkaz. Použij 'help' pro seznam příkazů.")
            print()

#MENU Hry
print("---------------------------")
print("===========================")
print("           MENU            ")
print("===========================")
print("    Začít hrát <enter>     ")
print("---------------------------")
welcomr = input(">>  ")
if welcomr == "":
    main()

