import tkinter as tk

def zeige_zweites_fenster():
    # Funktion, die aufgerufen wird, um das zweite Fenster zu erstellen
    hauptfenster.withdraw()
    zweites_fenster = tk.Toplevel(hauptfenster)
    zweites_fenster.title("Zweites Fenster")

# Hauptfenster erstellen
hauptfenster = tk.Tk()
hauptfenster.title("Hauptfenster")

# Button im Hauptfenster, um das zweite Fenster zu öffnen
button = tk.Button(hauptfenster, text="Öffne Zweites Fenster", command=zeige_zweites_fenster)
button.pack(pady=20)

# Tkinter starten
hauptfenster.mainloop()
