import tkinter as tk


class GameInterface:
    def __init__(self, master, menu_callback, options):
        self.menu_button = None
        self.button_2 = None
        self.button_1 = None
        self.question_label = None
        self.master = master
        self.menu_callback = menu_callback
        self.master.title("Game")
        self.master.geometry("600x400")

        self.options = options
        self.current_question_index = 0
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", wraplength=500)
        self.question_label.pack(pady=20)

        self.button_1 = tk.Button(self.master, text="", wraplength=300, command=self.answer_1, width=30, height=5)
        self.button_1.pack(pady=10)

        self.button_2 = tk.Button(self.master, text="", wraplength=300, command=self.answer_2, width=30, height=5)
        self.button_2.pack(pady=10)

        self.menu_button = tk.Button(self.master, text="Back to Menu",
                                     command=lambda: return_to_menu(self.master), width=30, height=2)

        self.menu_button.pack(pady=10)

        self.show_next_question()

    def show_next_question(self):
        if self.current_question_index < len(self.options):
            question, option1, option2 = self.options[self.current_question_index]
            self.question_label.config(text=question)
            self.button_1.config(text=option1)
            self.button_2.config(text=option2)
            self.current_question_index += 1
        else:
            self.question_label.config(text="Game Over")

    def answer_1(self):
        # Handle answer for option 1
        self.show_next_question()

    def answer_2(self):
        # Handle answer for option 2
        self.show_next_question()


def play_level(options, window_title, window):
    window.withdraw()
    game_window = tk.Toplevel(window)
    game_window.title(window_title)
    game_window.geometry("600x400")

    # Create an instance of the GameInterface
    GameInterface(game_window, lambda: return_to_menu(game_window), options)


def return_to_menu(game_window):
    game_window.withdraw()  # Withdraw the game window
    interface_menu()  # Show the main menu window


def level1(window):
    options = [
        ("Vanilleeis oder Schokoeis?", "Vanilleeis", "Schokoeis"),
        ("Pizza oder Burger?", "Pizza", "Burger"),
        ("Fein geriebene Haferflocken oder grob geriebene Haferflocken?", "Fein geriebene Haferflocken",
         "Grob geriebene Haferflocken"),
        ("Ketchup oder Mayo?", "Ketchup", "Mayo"),
        ("Wilder bernd Käse oder müritzer herzhafter Schnittkäse?", "Wilder bernd Käse",
         "müritzer herzhafter Schnittkäse"),
    ]
    play_level(options, "Level 1: Essen", window)


def level2(window):
    options = [
        ("Zierlicher-Prachtkäfer oder Fleckhals-Prachtkäfer?", "Zierlicher-Prachtkäfer", "Fleckhals-Prachtkäfer"),
        ("Schwarzgesichtklammeraffe oder Kaiserschnurrbarttamarin?", "Schwarzgesichtklammeraffe",
         "Kaiserschnurrbarttamarin"),
        ("Schwarze Ameise oder Rote Ameise?", "Schwarze Ameise", "Rote Ameise"),
        ("Komischer Kauz oder Vertrauenvolle Amsel?", "Komischer Kauz", "Vertrauenvolle Amsel"),
        ("1000 beiniger tausendfüßler oder 999 beiniger tausendfüßler?", "1000 beiniger tausendfüßler",
         "999 beiniger tausendfüßler"),
    ]
    play_level(options, "Level 2: Tiere", window)


def level3(window):
    options = [
        ("Fortnite oder Minecraft?", "Fortnite", "Minecraft"),
        ("Golf oder Bowling?", "Golf", "Bowling"),
        ("Bücher oder Filme?", "Bücher", "Filme"),
        ("Tennis oder Badminton?", "Tennis", "Badminton"),
        ("Bier brauen oder Rebhühner füttern?", "Bier brauen", "Rebhühner füttern"),
    ]
    play_level(options, "Level 3: Freizeit", window)


def level4(window):
    options = [
        ("Kämpfe gegen 10 Trolle oder kämpfe gegen Omar Masari?", "Kämpfe gegen 10 Trolle", "Kämpfe gegen Omar Masari"),
        ("test", "test", "test"),
        ("Mach 1vs1 gegen Robin oder mach 1vs1 gegen Julian?", "Mach 1vs1 gegen Robin", "Mach 1vs1 gegen Julian"),
        ("Erfahre wann du stirbst oder erfahre wie du stirbst?", "Erfahre wann du stirbst", "Erfahre wie du stirbst"),
        (
            "Sei obdachlos aber sehr glücklich mit Freunden und Familie oder sei Topverdiener in DE aber hab keine "
            "Familie, Freunde und sei extrem unglücklich?",
            "Sei obdachlos aber sehr glücklich mit Freunden und Familie",
            "Sei Topverdiener in DE aber hab keine Familie, Freunde und sei extrem unglücklich"),
    ]
    play_level(options, "Level 4: Schwierige Situationen", window)


def level5(window):
    options = [
        ("Sei in einem Spiel von Saw gefangen oder sei in einem Haus mit The Nun gefangen?",
         "Sei in einem Spiel von Saw gefangen", "Sei in einem Haus mit The Nun gefangen"),
        ("Werde verfolgt von Mommy Longlegs oder werde verfolgt von Huggy Wuggy?", "Werde verfolgt von Mommy Longlegs",
         "Werde verfolgt von Huggy Wuggy"),
        ("Laufe durch einen Wald in dem Slender Man haust oder laufe durch einen Wald in dem Siren Head haust?",
         "Laufe durch einen Wald in dem Slender Man haust", "Laufe durch einen Wald in dem Siren Head haust"),
        (
            "Sei auf der Insel Sodor in der Welt von Thomas der Lokomotive gefangen oder sei auf der Insel gefangen "
            "in der Choo-Choo Charles lebt?",
            "Sei auf der Insel Sodor in der Welt von Thomas der Lokomotive gefangen",
            "Sei auf der Insel gefangen in der Choo-Choo Charles lebt"),
        ("Sei in einem Kinderzimmer mit Annabelle für 60 Minuten gefangen oder sei ...",
         "Sei in einem Kinderzimmer mit Annabelle für 60 Minuten gefangen", "Sei ..."),
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

    button_4 = tk.Button(window, text="Level 4: Schwierige Situationen", command=lambda: level4(window), width=30,
                         height=5)
    button_4.pack(pady=7.5)

    button_5 = tk.Button(window, text="Level 5: Horror", command=lambda: level5(window), width=30, height=5)
    button_5.pack(pady=7.5)

    window.mainloop()


def interface_game():
    pass


interface_menu()
