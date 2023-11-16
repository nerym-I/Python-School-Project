
def level1():
    # option1 = None
    option2 = None
    listindex = 1
    while listindex < 6:
        if listindex== 1:
            option1="Vanilleeis"
            option2="Schokoeis"
        elif listindex== 2:
            option1="Pizza"
            option2="Burger"
        elif listindex == 3:
            option1="fein geriebene Haferflocken"
            option2="grob geriebene Haferflocken"    
        elif listindex == 4:
            option1="Ketchup"
            option2="Mayo"
        elif listindex == 5:
            option1="Wilder bernd Käse"
            option2="müritzer herzhafter Schnittkäse"

        print(option1+" or "+option2)
        chosen = int(input ("Press 1 or 2: "))
        if chosen == 1:
            chosen=option1
        elif chosen == 2:
            chosen=option2
        elif chosen != (1, 2):
            false_chosen = 0
            while false_chosen == 0:
                chosen = int(input ("Press 1 or 2: "))
                if chosen == 1:
                    chosen=option1
                    false_chosen=1
                elif chosen == 2:
                    chosen=option2
                    false_chosen=1
        print ("You chose option: " + chosen)
        listindex += 1
    menu1()

def level2():
    option1 = None
    option2 = None
    listindex = 1
    while listindex < 6:
        if listindex== 1:
            option1="Zierlicher-Prachtkäfer"
            option2="Fleckhals-Prachtkäfer"
        elif listindex== 2:
            option1="Schwarzgesichtklammeraffe"
            option2="Kaiserschnurrbarttamarin"
        elif listindex== 3:
            option1="schwarze Ameise"
            option2="Rote Ameise"    
        elif listindex== 4:
            option1="komischer Kauz"
            option2="vertrauenvolle Amsel"
        elif listindex== 5:
            option1="1000 beiniger tausendfüßler"
            option2="999 beiniger tausendfüßler"

        print(option1+" or "+option2)
        chosen = int(input ("Press 1 or 2: "))
        if chosen == 1:
            chosen=option1
        elif chosen == 2:
            chosen=option2
        elif chosen != (1, 2):
            false_chosen = 0
            while false_chosen == 0:
                chosen = int(input ("Press 1 or 2: "))
                if chosen == 1:
                    chosen=option1
                    false_chosen=1
                elif chosen == 2:
                    chosen=option2
                    false_chosen=1
        print ("You chose option: " + chosen)
        listindex += 1
    menu1()

def level3():
    option1 = None
    option2 = None
    listindex = 1
    while listindex < 6:
        if listindex== 1:
            option1="Fortnite"
            option2="Minecraft"
        elif listindex== 2:
            option1="Golf"
            option2="Bowling"
        elif listindex== 3:
            option1="Bücher"
            option2="Filme"    
        elif listindex== 4:
            option1="Tennis"
            option2="Badminton"
        elif listindex== 5:
            option1="Bier brauen"
            option2="Rebhühner füttern"

        print(option1+" or "+option2)
        chosen = int(input ("Press 1 or 2: "))
        if chosen == 1:
            chosen=option1
        elif chosen == 2:
            chosen=option2
        elif chosen != (1, 2):
            false_chosen = 0
            while false_chosen == 0:
                chosen = int(input ("Press 1 or 2: "))
                if chosen == 1:
                    chosen=option1
                    false_chosen=1
                elif chosen == 2:
                    chosen=option2
                    false_chosen=1
        print ("You chose option: " + chosen)
        listindex += 1
    menu1()
    
def level4():
    option1 = None
    option2 = None
    listindex = 1
    while listindex < 6:
        if listindex== 1:
            option1="kämpfe gegen 10 trolle"
            option2="kämpfe gegen omar masari"
        elif listindex== 2:
            option1="werde verfolgt von mommy longlegs"
            option2="werde verfolgt von Huggy Wuggy"
        elif listindex== 3:
            option1="streite dich mit Julian"
            option2="streite dich mit Robin"    
        elif listindex== 4:
            option1=""
            option2=""
        elif listindex== 5:
            option1="Bier brauen"
            option2="Rebhühner füttern"

        print(option1+" or "+option2)
        chosen = int(input ("Press 1 or 2: "))
        if chosen == 1:
            chosen=option1
        elif chosen == 2:
            chosen=option2
        elif chosen != (1, 2):
            false_chosen = 0
            while false_chosen == 0:
                chosen = int(input ("Press 1 or 2: "))
                if chosen == 1:
                    chosen=option1
                    false_chosen=1
                elif chosen == 2:
                    chosen=option2
                    false_chosen=1
        print ("You chose option: " + chosen)
        listindex += 1
    menu1()
    
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