import tkinter as tk
from tkinter import font

def play_level(options, window_title, window):
    buttonindex = 0
    window.withdraw()

    def update_labels():
        nonlocal buttonindex
        game_button1["text"], game_button2["text"] = options[buttonindex]
        buttonindex += 1
        if buttonindex == len(options):
            game_window.destroy()
            interface_menu()

    game_window = tk.Toplevel(window)
    game_window.title(window_title)
    game_window.geometry("300x550")
    
    canvas = tk.Canvas(game_window, width=300, height=550)
    canvas.pack()
    canvas.create_rectangle(0, 0, 300, 265, fill="blue", outline="blue")
    canvas.create_rectangle(0, 265, 300, 275, fill="black", outline="black")
    canvas.create_rectangle(0, 275, 300, 550, fill="red", outline="red")

    button_font = ('Arial Black', 10)
   
    game_button1 = tk.Button(game_window, text="", font=button_font, command=update_labels, width=30, height=5, wraplength=200)
    canvas.create_window(150, 137.5, window=game_button1)
    game_button2 = tk.Button(game_window, text="", font=button_font, command=update_labels, width=30, height=5, wraplength=200)
    canvas.create_window(150, 412.5, window=game_button2) 
        
    update_labels() 
    
    game_window.mainloop()
    
def level1(window):
    options = [
        ("Vanilleeis", "Schokoeis"),
        ("Pizza", "Burger"),
        ("fein geriebene Haferflocken", "grob geriebene Haferflocken"),
        ("Ketchup", "Mayo"),
        ("Wilder bernd Käse", "müritzer herzhafter Schnittkäse"),
        ("",""),
    ]
    play_level(options, "Level 1: Essen", window)

def level2(window):
    options = [
        ("Zierlicher-Prachtkäfer", "Fleckhals-Prachtkäfer"),
        ("Schwarzgesichtklammeraffe", "Kaiserschnurrbarttamarin"),
        ("schwarze Ameise", "Rote Ameise"),
        ("komischer Kauz", "vertrauenvolle Amsel"),
        ("1000 beiniger tausendfüßler", "999 beiniger tausendfüßler"),
        ("",""),
    ]
    play_level(options, "Level 2: Tiere", window)

def level3(window):
    options = [
        ("Fortnite", "Minecraft"),
        ("Golf", "Bowling"),
        ("Bücher", "Filme"),
        ("Tennis", "Badminton"),
        ("Bier brauen", "Rebhühner füttern"),
        ("",""),
    ]
    play_level(options, "Level 3: Freizeit", window)

def level4(window):
    options = [
        ("kämpfe gegen 10 Trolle", "kämpfe gegen Omar Masari"),
        ("hallo", "mama"),
        ("mach 1vs1 gegen Robin", "mach 1vs1 gegen Julian"),
        ("erfahre wann du stirbst", "erfahre wie du stirbst"),
        ("sei obdachlos aber sehr glücklich mit Freunden und Familie", "sei Topverdiener in DE aber hab keine Familie, Freunde und sei extrem unglücklich"),
        ("",""),
    ]
    play_level(options, "Level 4: Schwierige Situationen", window)

def level5(window):
    options = [
        ("sei in einem Spiel von Saw gefangen", "sei in einem Haus mit The Nun gefangen"),
        ("werde verfolgt von Mommy Longlegs", "werde verfolgt von Huggy Wuggy"),
        ("laufe durch einen Wald, in dem Slender Man haust", "laufe durch einen Wald, in dem Siren Head haust"),
        ("sei auf der Insel Sodor in der Welt von Thomas der Lokomotive gefangen", "sei auf der Insel gefangen, in der Choo-Choo Charles lebt"),
        ("sei in einem Kinderzimmer mit Annabelle für 60 min. gefangen", ""),
        ("",""),
    ]
    play_level(options, "Level 5: Horror", window)

def interface_menu():
    window_title = "Menü"
    window = tk.Tk()
    window.title(window_title)
    window.geometry("300x550")

    button_1 = tk.Button(window, text="Level 1: Essen", command=lambda: level1(window), width=30, height=5)
    button_1.pack(pady=7.5)

    button_2 = tk.Button(window, text="Level 2: Tiere", command=lambda: level2(window), width=30, height=5)
    button_2.pack(pady=7.5)

    button_3 = tk.Button(window, text="Level 3: Freizeit", command=lambda: level3(window), width=30, height=5)
    button_3.pack(pady=7.5)

    button_4 = tk.Button(window, text="Level 4: Schwierige Situationen", command=lambda: level4(window), width=30, height=5)
    button_4.pack(pady=7.5)

    button_5 = tk.Button(window, text="Level 5: Horror", command=lambda: level5(window), width=30, height=5)
    button_5.pack(pady=7.5)

    window.mainloop()
    
interface_menu()
