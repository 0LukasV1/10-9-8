import tkinter as tk
import random
from collections import Counter

class Game:
    def __init__(self, master):
        self.master = master
        self.plates = list('ABCDEFGHIJ')
        self.cracked_plate = random.choice(self.plates)
        self.clicked_plates = []
        self.canvas = tk.Canvas(master, width=500, height=200)
        self.canvas.pack()
        self.draw_plates()

    def draw_plates(self):
        for i, plate in enumerate(self.plates):
            self.canvas.create_oval(i*50, 75, i*50+50, 125, fill='blue')
            self.canvas.create_text(i*50+25, 100, text=plate, fill='white')
        self.canvas.bind("<Button-1>", self.click)

    def click(self, event):
        clicked_plate = self.plates[event.x // 50]
        self.clicked_plates.append(clicked_plate)
        if clicked_plate == self.cracked_plate:
            self.end_game()

    def end_game(self):
        self.canvas.delete('all')
        self.canvas.create_text(250, 100, text='Gratulujem, našiel si puknutý tanier!')
        multiple_clicks = [plate for plate, count in Counter(self.clicked_plates).items() if count > 1]
        if multiple_clicks:
            print('Klikol si viackrát na tieto taniere:', ', '.join(multiple_clicks))

root = tk.Tk()
game = Game(root)
root.mainloop()
