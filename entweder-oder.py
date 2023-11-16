
def level1():
    print("hello")
    # option1 = None
    option2 = None
    stagecounter = 1
    while stagecounter < 6:
        if stagecounter== 1:
            option1="Vanilleeis"
            option2="Schokoeis"
        if stagecounter== 2:
            option1="Pizza"
            option2="Burger"
        if stagecounter== 3:
            option1="fein geriebene Haferflocken"
            option2="grob geriebene Haferflocken"    
        if stagecounter== 4:
            option1="Ketchup"
            option2="Mayo"
        if stagecounter== 5:
            option1="Wilder bernd Käse"
            option2="müritzer herzhafter Schnittkäse"
        print(option1+" or "+option2)
        chosen = input ("Press 1 or 2: ")
        if chosen:= 1:
            chosen=option1
        if chosen:= 2:
            chosen=option2
        print ("You chose option: " + chosen)
        stagecounter += 1
    menu1()

def level2():
    option1 = None
    option2 = None
    stagecounter = 1
    while stagecounter < 6:
        if stagecounter== 1:
            option1="Zierlicher-Prachtkäfer"
            option2="Fleckhals-Prachtkäfer"
        if stagecounter== 2:
            option1="Schwarzgesichtklammeraffe"
            option2="Kaiserschnurrbarttamarin"
        if stagecounter== 3:
            option1="schwarze Ameise"
            option2="Rote Ameise"    
        if stagecounter== 4:
            option1="komischer Kauz"
            option2="vertrauenvolle Amsel"
        if stagecounter== 5:
            option1="1000 beiniger tausendfüßler"
            option2="999 beiniger tausendfüßler"
        print(option1+" or "+option2)
        chosen = input ("Press 1 or 2: ")
        if chosen:= 1:
            chosen=option1
        if chosen:= 2:
            chosen=option2
        print ("You chose option: " + chosen)
        stagecounter += 1
    menu1()

def level3():
    option1 = None
    option2 = None
    stagecounter = 1
    while stagecounter < 6:
        if stagecounter== 1:
            option1="Fortnite"
            option2="Minecraft"
        if stagecounter== 2:
            option1="Golf"
            option2="Bowling"
        if stagecounter== 3:
            option1="Bücher"
            option2="Filme"    
        if stagecounter== 4:
            option1="Tennis"
            option2="Badminton"
        if stagecounter== 5:
            option1="Bier brauen"
            option2="Rebhühner füttern"
        print(option1+" or "+option2)
        chosen = input ("Press 1 or 2: ")
        if chosen:= 1:
            chosen=option1
        if chosen:= 2:
            chosen=option2
        print ("You chose option: " + chosen)
        stagecounter += 1
    menu1()
    
def menu1():
    print("Level 1: Essen")
    print("Level 2: Tiere")
    print("Level 3: Freizeit")
    level = input("Choose level: ")
    if level == 1:
        level1()
    if level == 2:
        level2()
    if level == 3:
        level3()
        
menu1()