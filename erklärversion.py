import tkinter as tk
from tkinter import font

# Funktion, um ein Level mit Optionen zu spielen und die Beschriftungen entsprechend zu aktualisieren
def play_level(options, window_title, window):
    # Initialisiere den Index des aktuellen Buttons in der Optionsliste
    buttonindex = 0
    
    # Verberge das Hauptmenü-Fenster
    window.withdraw()

    # Funktion zum Aktualisieren der Beschriftungen im Spiel-Fenster
    def update_labels():
        nonlocal buttonindex
        # Setze den Text der Spielbuttons basierend auf den aktuellen Optionen
        game_button1["text"], game_button2["text"] = options[buttonindex]
        buttonindex += 1
        # Wenn alle Optionen erschöpft sind, schließe das Spiel-Fenster und kehre zum Hauptmenü zurück
        if buttonindex == len(options):
            game_window.destroy()
            interface_menu()

    # Erstelle ein neues Spiel-Fenster
    game_window = tk.Toplevel(window)
    game_window.title(window_title)
    game_window.geometry("300x550")
    
    # Erstelle eine Leinwand mit farbigen Rechtecken als Hintergrund des Spiels
    canvas = tk.Canvas(game_window, width=300, height=550)
    canvas.pack()
    canvas.create_rectangle(0, 0, 300, 265, fill="blue", outline="blue")
    canvas.create_rectangle(0, 265, 300, 275, fill="black", outline="black")
    canvas.create_rectangle(0, 275, 300, 550, fill="red", outline="red")

    # Definiere die Schriftart für die Spielbuttons
    button_font = ('Arial Black', 10)
   
    # Erstelle zwei Buttons auf der Leinwand für das Spiel
    game_button1 = tk.Button(game_window, text="", font=button_font, command=update_labels, width=30, height=5, wraplength=200)
    canvas.create_window(150, 137.5, window=game_button1)
    game_button2 = tk.Button(game_window, text="", font=button_font, command=update_labels, width=30, height=5, wraplength=200)
    canvas.create_window(150, 412.5, window=game_button2) 
        
    # Initialisiere die Beschriftungen für den ersten Satz von Optionen
    update_labels() 
    
    # Starte die Ereignisschleife des Spiel-Fensters
    game_window.mainloop()

# Funktionen für verschiedene Level mit spezifischen Optionen
def level1(window):
    options = [
        ("Vanilleeis", "Schokoeis"),
        ("Pizza", "Burger"),
        ("fein geriebene Haferflocken", "grob geriebene Haferflocken"),
        ("Ketchup", "Mayo"),
        ("Wilder Bernd Käse", "Müritzer herzhafter Schnittkäse"),
    ]
    # Starte Level 1 mit den angegebenen Optionen
    play_level(options, "Level 1: Essen", window)

# (Ähnliche Kommentare gelten für level2, level3, level4 und level5 Funktionen)

# Funktion zum Anzeigen der Hauptmenü-Benutzeroberfläche
def interface_menu():
    window_title = "Menü"
    # Erstelle das Hauptmenü-Fenster
    window = tk.Tk()
    window.title(window_title)
    window.geometry("300x550")

    # Erstelle Buttons für jedes Level im Hauptmenü
    button_1 = tk.Button(window, text="Level 1: Essen", command=lambda: level1(window), width=30, height=5)
    button_1.pack(pady=7.5)

    # (Ähnliche Kommentare gelten für button_2, button_3, button_4 und button_5)

    # Starte die Ereignisschleife des Hauptmenüs
    window.mainloop()

# Rufe die Funktion für die Hauptmenü-Benutzeroberfläche auf, um das Programm zu starten
interface_menu()
