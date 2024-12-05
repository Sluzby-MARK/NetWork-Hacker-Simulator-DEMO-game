import tkinter as tk
from tkinter import messagebox
import time

# Funkce pro příkazy
def show_help():
    output_text.set(
        "Dostupné příkazy:\n"
        "  - Skenovat síť (tlačítko Skenuj)\n"
        "  - Připojit se k serveru (vyber server a klikni Připojit)\n"
        "  - Hacknout server (vyber server a klikni Hackni)\n"
        "  - Ukončit hru (tlačítko Ukončit)"
    )

def scan():
    output_text.set("Skenuji síť...")
    root.update()
    time.sleep(1)
    available_servers.set(["Server_A", "Server_B", "Server_C"])
    output_text.set("Servery nalezeny: Server_A, Server_B, Server_C")

def connect():
    selected = server_var.get()
    if selected:
        output_text.set(f"Připojuji se k {selected}...")
        root.update()
        time.sleep(1)
        connected_server.set(selected)
        output_text.set(f"Úspěšně připojeno k {selected}.")
    else:
        messagebox.showwarning("Chyba", "Musíš vybrat server, ke kterému se chceš připojit!")

def hack():
    selected = connected_server.get()
    if selected:
        output_text.set(f"Pokouším se hacknout {selected}...")
        root.update()
        time.sleep(2)
        output_text.set(f"Úspěch! Server {selected} byl hacknut.")
    else:
        messagebox.showerror("Chyba", "Musíš se nejprve připojit k serveru!")

def exit_game():
    root.quit()

# Hlavní okno
root = tk.Tk()
root.title("Hackovací simulátor")
root.geometry("500x400")

# Výběr serverů
available_servers = tk.StringVar(value=[])
server_var = tk.StringVar(value="")

connected_server = tk.StringVar(value="")

# Textový výstup
output_text = tk.StringVar(value="Vítej v hackovacím simulátoru! Klikni na 'Nápověda', pokud si nevíš rady.")

# Layout
tk.Label(root, text="Hackovací simulátor", font=("Helvetica", 16, "bold")).pack(pady=10)
tk.Label(root, textvariable=output_text, wraplength=480, justify="left", bg="#f0f0f0", relief="solid", padx=10, pady=10).pack(pady=5)

# Tlačítka pro příkazy
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Nápověda", command=show_help, width=12).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Skenuj", command=scan, width=12).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Připojit", command=connect, width=12).grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Hackni", command=hack, width=12).grid(row=0, column=3, padx=5, pady=5)
tk.Button(button_frame, text="Ukončit", command=exit_game, width=12).grid(row=0, column=4, padx=5, pady=5)

# Seznam serverů
tk.Label(root, text="Dostupné servery:").pack(pady=5)
server_listbox = tk.Listbox(root, listvariable=available_servers, height=4)
server_listbox.pack(pady=5, fill="x")
server_listbox.bind("<<ListboxSelect>>", lambda e: server_var.set(server_listbox.get(server_listbox.curselection())))

# Spuštění aplikace
root.mainloop()