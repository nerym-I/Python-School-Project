import tkinter as tk
from tkinter import font 
from PIL import Image, ImageTk, ImageSequence
import time
import sys

def interface_menu():
    
    def on_button_click():
        input_text = entry.get()
        if input_text == "0808201466":
            bonus_level(window)
   
    window_title = "Menü"
    window = tk.Tk()
    window.title(window_title)
    window.geometry("300x620")

    button_1 = tk.Button(window, text="Level 1: Essen", font=('Arial Black', 10), command=lambda: level1(window), width=30, height=4)
    button_1.pack(pady=6)
    button_2 = tk.Button(window, text="Level 2: Tiere", font=('Arial Black', 10), command=lambda: level2(window), width=30, height=4)
    button_2.pack(pady=6)
    button_3 = tk.Button(window, text="Level 3: Freizeit", font=('Arial Black', 10), command=lambda: level3(window), width=30, height=4)
    button_3.pack(pady=6)
    button_4 = tk.Button(window, text="Level 4: Schwierige Situationen", font=('Arial Black', 10), command=lambda: level4(window), width=30, height=4)
    button_4.pack(pady=6)
    button_5 = tk.Button(window, text="Level 5: Horror", font=('Arial Black', 10), command=lambda: level5(window), width=30, height=4)
    button_5.pack(pady=6)
    
    entry = tk.Entry(window, width=30)
    entry.pack(pady=6)

    button = tk.Button(window, text="Bonus Level", font=('Arial Black', 10), command=on_button_click, width=30, height=4)
    button.pack()
        
    window.mainloop()
    
def level1(window):
    options = [
        ("Vanilleeis", "Schokoeis"),
        ("Pizza", "Burger"),
        ("fein geriebene Haferflocken", "grob geriebene Haferflocken"),
        ("Ketchup", "Mayo"),
        ("Wilder bernd Käse", "müritzer herzhafter Schnittkäse"),
        ("0","8"),
    ]
    play_level(options, "Level 1: Essen", window)

def level2(window):
    options = [
        ("Zierlicher-Prachtkäfer", "Fleckhals-Prachtkäfer"),
        ("Schwarzgesichtklammeraffe", "Kaiserschnurrbarttamarin"),
        ("Esel der Gold kackt", "bremer stadtmusikanten"),
        ("komischer Kauz", "vertrauenvolle Amsel"),
        ("1000 beiniger Tausendfüßler", "999 beiniger Tausendfüßler"),
        ("0","8"),
    ]
    play_level(options, "Level 2: Tiere", window)

def level3(window):
    options = [
        ("Fußball", "Basketball"),
        ("Golf", "Bowling"),
        ("Bücher", "Filme"),
        ("Tennis", "Badminton"),
        ("Bier brauen", "Rebhühner füttern"),
        ("2","0"),
    ]
    play_level(options, "Level 3: Freizeit", window)

def level4(window):
    options = [
        ("kämpfe gegen 10 Trolle", "kämpfe gegen Omar Masari"),
        ("habe die Fähigkeit unsichtbar zu sein", "habe die Fähigkeit die Zeit anhalten zu können"),
        ("mach ein youtube video mit Drachenlord", "mach ein youtube video mit mimon baraka"),
        ("erfahre wann du stirbst", "erfahre wie du stirbst"),
        ("sei obdachlos aber glücklich", "sei reich aber unglücklich"),
        ("1","4"),
    ]
    play_level(options, "Level 4: Schwierige Situationen", window)

def level5(window):
    options = [
        ("sei in einem Spiel von Saw gefangen", "sei in einem Haus mit The Nun gefangen"),
        ("werde verfolgt von Mommy Longlegs", "werde verfolgt von Huggy Wuggy"),
        ("laufe durch einen Wald, in dem Slender Man haust", "laufe durch einen Wald, in dem Siren Head haust"),
        ("sei in der Welt von Thomas der Lokomotive gefangen", "sei auf der Insel gefangen, in der Choo-Choo Charles lebt"),
        ("sei in einem Zimmer mit Annabelle gefangen", "entkomme aus dem Haus von granny"),
        ("6","6")
    ]
    play_level(options, "Level 5: Horror", window)

def bonus_level(window):
    options = [
        ("schwarze Schokolade", "weiße Schokolade"),
        ("A-Zweig", "B-Zweig"),
        ("Zawg", "Schlawg"),
        ("Baby bete für mich!", "Was machst du schon wieder?"),
        ("erst die Schüssel dann die Milch", "Erst das Müsli dann die Zahnpasta"),
        ("",""),
    ]
    play_level(options, "Bonus Level", window)
    
def play_level(options, window_title, window):
    buttonindex = 0
    window.withdraw()

    def update_labels():
        nonlocal buttonindex
        game_button1["text"], game_button2["text"] = options[buttonindex]
        buttonindex += 1
        if window_title != "Bonus Level":
            if buttonindex == 6:
                game_button1["text"], game_button2["text"] = options[5]
                game_window.update()
                time.sleep(0.5)
                game_window.destroy()
                interface_menu()
        elif window_title == "Bonus Level":
                if buttonindex == len(options):
                    end_game = 0
                    game_window.withdraw()

                    def play_gif(label, gif_index):
                        nonlocal end_game
                        label.configure(image=gif_frames[gif_index])
                        gif_index = (gif_index + 1) % len(gif_frames)
                        gif_window.after(50, play_gif, label, gif_index) 
                        if gif_index == 1:
                            end_game += 1
                        if end_game == 6:
                            gif_window.destroy()
                            sys.exit()

                    gif_window = tk.Toplevel(game_window)
                    gif_window.title("Bonus Scene")
                    gif_fnaf = Image.open("giphy.gif")

                    gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif_fnaf)]

                    label = tk.Label(gif_window, image=gif_frames[0])
                    label.pack()

                    play_gif(label, 0)

                    gif_window.mainloop()
                
    game_window = tk.Toplevel(window)
    game_window.title(window_title)
    game_window.geometry("300x550")
    
    canvas = tk.Canvas(game_window, width=300, height=550)
    canvas.pack()
    canvas.create_rectangle(0, 0, 300, 265, fill="blue", outline="blue")
    canvas.create_rectangle(0, 265, 300, 275, fill="black", outline="black")
    canvas.create_rectangle(0, 275, 300, 550, fill="red", outline="red")

    game_button1 = tk.Button(game_window, text="", font=('Arial Black', 10), command=update_labels, width=30, height=5, wraplength=200)
    canvas.create_window(150, 137.5, window=game_button1)
    game_button2 = tk.Button(game_window, text="", font=('Arial Black', 10), command=update_labels, width=30, height=5, wraplength=200)
    canvas.create_window(150, 412.5, window=game_button2) 
        
    update_labels() 
    
    game_window.mainloop()
    
interface_menu()
