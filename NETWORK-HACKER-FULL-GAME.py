import time
import os
import random
import subprocess

licence = """




LICENČNÍ PODMÍNKY PRO POUŽÍVÁNÍ SLUŽEB MARK

Děkujeme, že jste si vybrali naši hru! Před jejím používáním si prosím pozorně přečtěte tyto licenční podmínky („Podmínky“).
před spuštěním nebo používáním hry souhlasíte s těmito podmínkami.

### 1. Definice
1.1. „Hra“ označuje software MARK včetně všech aktualizací, rozšíření a obsahu poskytovaného autorem.
1.2. „Uživatel“ označuje osobu, která hru používá.
1.3. „Autor“ označuje vývojáře hry MARK.

### 2. Povaha hry
2.1. Hra je zábavní simulací a nenabádá k trestným nebo nelegálním činnostem.
2.2. Všechny události, postavy, organizace a zmínky (včetně vlády USA a skupiny Anonymous) jsou smyšlené a slouží pouze k zábavě.
2.3. Hra nepředstavuje skutečné hackování ani žádnou formu neoprávněného přístupu k datům.

### 3. Pravidla používání
3.1. Uživatel je povinen používat hru pouze v souladu s těmito podmínkami.
3.2. Je zakázáno manipulovat se soubory hry, zasahovat do jejího kódu nebo ji používat k jiným účelům, než které jsou uvedeny v misích.
3.3. Jakékoliv pokusy o přístup k datům, která nejsou součástí hry (např. citlivá data vlády USA), jsou přísně zakázány.
3.4. Jakékoliv zmínky o vládě USA ve hře jsou smyšlené a nejsou spojeny se skutečnými vládními institucemi.

### 4. Odpovědnost uživatele
4.1. Uživatel souhlasí s tím, že nebude používat hru k žádným nezákonným činnostem.
4.2. Užiatel nenese odpovědnost za jakékoliv přímé či nepřímé škody způsobené nesprávným používáním hry.

### 5. Omezení odpovědnosti
5.1. Hra je poskytována „tak, jak je“, bez jakýchkoliv záruk, výslovných či implicitních.
5.2. Autor nenese odpovědnost za ztrátu dat, přerušení provozu nebo jakékoliv jiné problémy vzniklé při používání hry.

### 6. Soukromí a ochrana údajů
6.1. Hra neshromažďuje žádné osobní údaje uživatele.
6.2. Jakékoliv informace poskytnuté uživatelem (např. kontakty s podporou) budou použity výhradně pro účely řešení problémů souvisejících s hrou.

### 7. Porušení podmínek
7.1. Poruší-li uživatel tyto podmínky, autor si vyhrazuje právo omezit přístup k hře nebo ukončit její používání.
7.2. Autor může přistoupit k právním krokům v případě vážného porušení těchto podmínek.

### 8. Závěrečná ustanovení
8.1. Tyto podmínky se řídí právními předpisy České republiky.
8.2. Autor si vyhrazuje právo tyto podmínky kdykoliv aktualizovat. O změnách bude uživatel informován prostřednictvím oficiálních kanálů.

Děkujeme za pochopení a přejeme příjemnou zábavu s naším produktem!

Dodatek

### 9. Pravidla misí hry
9.1. Při misi 'Hack the USA' prosím aby jste misi přeskočili
Proč?
Jedná se o všeobecný průzkum kdo si přečte licenční podmínky.

FIRMA SI MŮŽE KDYKOLI PODMÍNKY ZMĚNIT. PŘI ZMĚNĚ BUDETE INFORMOVÁNÍ.

© SLUŽBY MARK




"""


with open("licence.txt", "r") as souboor:
    stavlicence = souboor.read().strip()
print("Welcome to")
print("NETWORK HACKER")
print("Full Game")
time.sleep(1)
print("")
print("")
os.system('clear')
print("Thank you for purchasing a Mark product")
time.sleep(3)
print("Continue with czech language")
print("CZ - Čeština (Czech)...")
time.sleep(3)
print("Prosím přečtěte licenční podmínky pro používání")
print("služeb Mark")
time.sleep(4)
if stavlicence == "false":
    print(licence)
print("(NetWork Hacker)")
os.system('clear')

print("Zmáčkněte klávesu <enter> pro spuštění hry.")
input()












# Načtení jména uživatele
with open("jmeno.txt", "r") as soubor:
    jmeno = soubor.read().strip()

# Proměnné
hekeror = random.randint(100000, 9999999999999)
connected_server = None
mise = 2

tutorial = """


Tutorial pro plnění misí ve hře NetWork Hacker

Dostupné příkazy
    ls       - Zobrazí obsah složky nebo souboru
    cd <adresář> - Přesune se do složky
    nano <nazev-souboru> - Umožňuje upravit obsah souboru
    download <nazev-souboru> - Stáhne soubor
    Upload <nazev-souboru> - Nahraje na cílový PC soubor

Výrazně DOPORUČUJEME znát základní znalosti používání linux terminálu
před splnění misí.

Pro kopírování nepoužívejte klávesovou zkratku <ctrl> + <c> ale <ctrl> + <shift> + <c> / <v>

DĚKUJEME

© SLUŽBY MARK


"""


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
    print("  mision     - Získá misi od anonymous")
    print()

def help_mise():
    print("Dostupné příkazy:")
    print("    ls       - Zobrazí obsah složky nebo souboru")
    print("    cd <adresář> - Přesune se do složky")
    print("    nano <nazev-souboru> - Umožňuje upravit obsah souboru")
    print("    download <nazev-souboru> - Stáhne soubor")
    print("    Upload <nazev-souboru> - Nahraje na cílový PC soubor")


mise_id = 2
if mise_id == 1:
    misee = "Hack The USA"
if mise_id == 2:
    misee = """
dostaň přístup do banky a přičti si na účet 52 000,-
čislo účtu: 01001101
heslo do banky: 12*8
* = nezjištěný symbol
©Anonymous Hacker Group
"""

# Funkce pro interakci s počítačem během mise
def mission_interaction():
    print("From: Anonymous hacker group")
    print(f"to: {jmeno}")
    print("message:")
    print(misee)
    if misee == "Hack The USA":
        print("Chcete misi přeskočit(y/n)")
        smluvnipodminky = input()
        if smluvnipodminky == "y":
            print("Po splnění nebo ukončení mise restarutjte hru.")
            main
        if smluvnipodminky == "n":
            print("Porušili jste smluvní podmínky služeb mark")
            print("Můžete se veřejně nahlásit na email:")
            print("mvt.sro@gmail.com")
            print("Nebo vám může být odepřen přístup ke hře")
            print("autorem.")
            print("")
            print("Prosím přečtěte si smluvní podmínky")
            time.sleep(1)
            print("děkujeme.")
            time.sleep(3)
            print(licence)
    if misee == """
dostaň přístup do banky a přičti si na účet 52 000,-
čislo účtu: 01001101
heslo do banky: 12*8
* = nezjištěný symbol
©Anonymous Hacker Group
""":
        print("From: Anonymous hacker group")
        print(f"to: {jmeno}")
        print("message:")
        print(misee)
        print()
        print()
        print("Welcome to Ubuntu Server 24.10 LTS")
        print("Login: AirBank-PLATBA")
        while True:  
            password = input("Password: ")
            if password == "1298":
                print("Welcome To Ubuntu Server 24.10 Long-Time-Support")
                print("")
                print("")
                print("")
                print("")
                while True:
                    miseeee = input("AirBank-PLATBA@airbankserver:~$ ")
                    if miseeee == "PLATBA: OD: SLUZBY-MARK DO: 01001101 ČÁSTKA 52 000,- PŘES AirBank":
                        print("probíhá transakce...")
                        time.sleep(3)
                        print("Úspěch!!!")
                        time.sleep(1)
                        print("Exit...")
                        time.sleep(2)
                        print("MISE Byla Splněna!!!")
                        print("Ukončuji spojení se serverem...")
                        time.sleep(1)
                        print("You are in your PC:")
                        main()
                    else:
                        print("Bohužel příkaz neproběhl úspěšně")
                        print("")
                        print("")
                        print("                                      nápověda od anonymous: PLATBA: OD: Státní Rozpočet DO: 01001101 ČÁSTKA 52 000,- PŘES AirBank")
                        
        




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
        elif command == "mission":
            print("Čekání na misi od anonymous hacker group")
            time.sleep(3)
            mission_interaction
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





