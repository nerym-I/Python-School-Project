from tkinter import *
from tkinter import ttk

def play_level(options, window_title):
    listindex = 1
    while listindex < 6:
        option1, option2 = options[listindex - 1]

        print(f"{option1} or {option2}")
        chosen = input("drücke 1 oder 2: ")

        while chosen not in ("1", "2"):
            chosen = input("drücke 1 oder 2: ")

        if chosen == "1":
            chosen=option1
        elif chosen=="2":
            chosen=option2
        print("wähle aus:", chosen)
        listindex += 1
    menu1()


def level1():
    options = [
        ("Vanilleeis", "Schokoeis"),
        ("Pizza", "Burger"),
        ("fein geriebene Haferflocken", "grob geriebene Haferflocken"),
        ("Ketchup", "Mayo"),
        ("Wilder bernd Käse", "müritzer herzhafter Schnittkäse"),
    ]
    play_level(options, "Level 1: Essen")


def level2():
    options = [
        ("Zierlicher-Prachtkäfer", "Fleckhals-Prachtkäfer"),
        ("Schwarzgesichtklammeraffe", "Kaiserschnurrbarttamarin"),
        ("schwarze Ameise", "Rote Ameise"),
        ("komischer Kauz", "vertrauenvolle Amsel"),
        ("1000 beiniger tausendfüßler", "999 beiniger tausendfüßler"),
    ]
    play_level(options, "Level 2: Tiere")


def level3():
    options = [
        ("Fortnite", "Minecraft"),
        ("Golf", "Bowling"),
        ("Bücher", "Filme"),
        ("Tennis", "Badminton"),
        ("Bier brauen", "Rebhühner füttern"),
    ]
    play_level(options, "Level 3: Freizeit")


def level4():
    options = [
        ("kämpfe gegen 10 trolle", "kämpfe gegen omar masari"),
        ("", ""),
        ("mach 1vs1 gegen Robin", "mach 1vs1 gegen Julian"),
        ("erfahre wann du stirbst", "erfahre wie du stirbst"),
        ("sei obdachlos aber sehr glücklich mit Freunden und Familie", "sei Topverdiener in DE aber hab keine Familie, Freunde und sei extrem unglücklich"),
    ]
    play_level(options, "Level 4: Schwierige Situationen")


def level5():
    options = [
        ("sei in einem Spiel von Saw gefangen", "sei in einem Haus mit the Nun gefangen"),
        ("werde verfolgt von mommy longlegs", "werde verfolgt von Huggy Wuggy"),
        ("laufe durch einen Wald in dem slender man haust", "laufe durch einen Wald in dem siren head haust"),
        ("sei auf der Insel Sodor in der Welt von thomas der Lokomotive gefangen", "sei auf der Insel gefangen in der choo-choo charles lebt"),
        ("sei in einem Kinderzimmer mit Annabelle für 60 min. gefangen", "sei "),
    ]
    play_level(options, "Level 5: Horror")

    

def menu1():
    print("Level 1: Essen")
    print("Level 2: Tiere")
    print("Level 3: Freizeit")
    print("Level 4: Schwierige Situationen")
    print("level 5: Horror")
    level = input("Choose level: ")

    while level not in ("1","2","3","4"):
            level = input("Choose level: ")

    if level == "1":
        level1()
    elif level == "2":
        level2()
    elif level == "3":
        level3()
    elif level == "4":
        level4()
    elif level == "5":
        level5() 
        
def interface():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()

interface()
