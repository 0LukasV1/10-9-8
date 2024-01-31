import tkinter as tk

def draw_crossword(file_name, square_size=40, gap_size=40):
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    root = tk.Tk()
    max_len = max([len(line.split(' ')[1]) for line in lines])
    canvas_width = square_size * max_len * 3 + gap_size * 4
    canvas_height = square_size * len(lines)
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    secret_word = ''
    for i, line in enumerate(lines):
        index, word = line.split(' ')
        index = int(index) - 1
        secret_word += word[index]
        for j in range(max_len):
            for k in range(2):  # Draw two identical crosswords side by side
                x1 = (j + k * (max_len + gap_size/square_size)) * square_size + gap_size
                y1 = i * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                color = 'white'
                char = ''
                if j == index:  # Color the square in both crosswords
                    color = 'lightblue'
                if j < len(word) and k == 1:  # Fill only the second crossword
                    char = word[j]
                if j >= len(word):  # Don't draw squares without letters in the crosswords
                    continue
                canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text=char)

    print('Secret word:', secret_word)
    root.mainloop()

# Test the function with your files
draw_crossword('krizovka1-1.txt')
draw_crossword('krizovka1-2.txt')
