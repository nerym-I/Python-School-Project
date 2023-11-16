def level1():
    option1 = None
    option2 = None
    stagecounter = 1
    while stagecounter < 11:
        if stagecounter== 1:
            option1="Vanilleeis"
            option2="Schokoeis"
        if stagecounter== 2:
            option1="Pizza"
            option2="Burger"
        print(option1+" or "+option2)
        chosen = input ("Press 1 or 2: ")
        if chosen:= 1:
            chosen=option1
        if chosen:= 2:
            chosen=option2
        print ("You chose option: " + chosen)
        stagecounter += 1

        

level = input("Choose level: ")
if level := 1:
    level1()
    