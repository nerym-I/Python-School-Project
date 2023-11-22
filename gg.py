import tkinter as tk
import time
def play_level(options, window_title, window):
    listindex = 1
    while listindex < 2:
        option1, option2 = options[listindex - 1]

        window.withdraw()
        game_window=tk.Toplevel(window)
        game_window.title(window_title)
        game_window.geometry("300x550")

        listindex += 1
    #game_window.withdraw()
    interface_menu()

def level1(window):
    options = [
        ("Vanilleeis", "Schokoeis"),
        ("Pizza", "Burger"),
        ("fein geriebene Haferflocken", "grob geriebene Haferflocken"),
        ("Ketchup", "Mayo"),
        ("Wilder bernd Käse", "müritzer herzhafter Schnittkäse"),
    ]
    play_level(options, "Level 1: Essen", window)


def level2(window):
    options = [
        ("Zierlicher-Prachtkäfer", "Fleckhals-Prachtkäfer"),
        ("Schwarzgesichtklammeraffe", "Kaiserschnurrbarttamarin"),
        ("schwarze Ameise", "Rote Ameise"),
        ("komischer Kauz", "vertrauenvolle Amsel"),
        ("1000 beiniger tausendfüßler", "999 beiniger tausendfüßler"),
    ]
    play_level(options, "Level 2: Tiere",window)


def level3(window):
    options = [
        ("Fortnite", "Minecraft"),
        ("Golf", "Bowling"),
        ("Bücher", "Filme"),
        ("Tennis", "Badminton"),
        ("Bier brauen", "Rebhühner füttern"),
    ]
    play_level(options, "Level 3: Freizeit",window)


def level4(window):
    options = [
        ("kämpfe gegen 10 trolle", "kämpfe gegen omar masari"),
        ("", ""),
        ("mach 1vs1 gegen Robin", "mach 1vs1 gegen Julian"),
        ("erfahre wann du stirbst", "erfahre wie du stirbst"),
        ("sei obdachlos aber sehr glücklich mit Freunden und Familie", "sei Topverdiener in DE aber hab keine Familie, Freunde und sei extrem unglücklich"),
    ]
    play_level(options, "Level 4: Schwierige Situationen", window)


def level5(window):
    options = [
        ("sei in einem Spiel von Saw gefangen", "sei in einem Haus mit the Nun gefangen"),
        ("werde verfolgt von mommy longlegs", "werde verfolgt von Huggy Wuggy"),
        ("laufe durch einen Wald in dem slender man haust", "laufe durch einen Wald in dem siren head haust"),
        ("sei auf der Insel Sodor in der Welt von thomas der Lokomotive gefangen", "sei auf der Insel gefangen in der choo-choo charles lebt"),
        ("sei in einem Kinderzimmer mit Annabelle für 60 min. gefangen", "sei "),
    ]
    play_level(options, "Level 5: Horror",window)

def interface_menu():
    window_title="Menü"
    window = tk.Tk()
    window.title(window_title)
    window.geometry("300x550")

    button_1 = tk.Button(window, text="Level 1: Essen", command=lambda: level1(window), width=30, height=5)
    button_1.pack(pady=7.5)

    button_2 = tk.Button(window, text="Level 2: Tiere", command=lambda: level2(window), width=30, height=5)
    button_2.pack(pady=7.5)

    button_3 = tk.Button(window, text="Level 3: Freizeit", command=lambda: level3(window), width=30, height=5)
    button_3.pack(pady=7.5)

    button_4 = tk.Button(window, text="Level 4: Freizeit", command=lambda: level4(window), width=30, height=5)
    button_4.pack(pady=7.5)

    button_5 = tk.Button(window, text="Level 5: Horror", command=lambda: level5(window), width=30, height=5)
    button_5.pack(pady=7.5 )

    # Start the Tkinter event loop
    window.mainloop()

def interface_game():
    pass

interface_menu()
