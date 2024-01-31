import tkinter
import random

# Vytvorenie plátna
canvas = tkinter.Canvas(width=700, height=800)
canvas.pack()

# Funkcia na vykreslenie lodičky
def vykresli_lodicku(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

# Vytvorenie a vykreslenie lodičiek
zoznam_lodicek = []
for i in range(15):
    y = 50 + i * 50
    vykresli_lodicku(50, y)
    zoznam_lodicek.append([50, y, i+1])  # Pozícia a číslo lodičky

# Funkcia na animáciu plávania lodičiek
def preteky():
    canvas.delete("all")
    for lodicka in zoznam_lodicek:
        posun = random.randint(1, 10)
        lodicka[0] += posun
        if lodicka[0] >= 650:  # Ak lodička dosiahla cieľ
            canvas.create_text(350, 400, text=f"Lodička číslo {lodicka[2]} bola prvá.", font=("Arial", 15), fill='red')
            return
        vykresli_lodicku(lodicka[0], lodicka[1])
    # Vykreslenie cieľovej čiary v červenej farbe po vymazaní plátna
    canvas.create_line(650, 0, 650, 800, fill='red')
    canvas.after(50, preteky)  # Zmena na 0,5 sekundy

# Spustenie pretekov kliknutím
canvas.bind("<Button-1>", lambda event: preteky())

# Spustenie hlavnej slučky
tkinter.mainloop()
