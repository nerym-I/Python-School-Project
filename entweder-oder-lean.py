def play_level(options, level_name):
    listindex = 1
    while listindex < 6:
        option1, option2 = options[listindex - 1]

        print(f"{option1} or {option2}")
        chosen = int(input("Press 1 or 2: "))

        while chosen not in (1, 2):
            chosen = int(input("Press 1 or 2: "))

        if chosen == 1:
            chosen=option1
        elif chosen==2:
            chosen=option2
        print("You chose option:", chosen)
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
        ("werde verfolgt von mommy longlegs", "werde verfolgt von Huggy Wuggy"),
        ("streite dich mit Julian", "streite dich mit Robin"),
        ("", ""),
        ("Bier brauen", "Rebhühner füttern"),
    ]
    play_level(options, "Level 4: Schwierige Situationen")


def menu1():
    print("Level 1: Essen")
    print("Level 2: Tiere")
    print("Level 3: Freizeit")
    print("Level 4: Schwierige Situationen")
    level = int(input("Choose level: "))
    if level == 1:
        level1()
    elif level == 2:
        level2()
    elif level == 3:
        level3()
    elif level == 4:
        level4()


menu1()
