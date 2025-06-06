import pyperclip

#🟦Blue Square
#🟧Orange Square
#🟪Purple Square
#🟫Brown Square
#🟥Red Square
#🟨Yellow Square
#🟩Green Square
#⬜White Medium Square
#⬛Black Medium Square

colors = [['black', '⬛'],
          ['white', '⬜'],
          ['blue', '🟦'],
          ['orange', '🟧'],
          ['purple', '🟪'],
          ['brown', '🟫'], 
          ['red', '🟥'],
          ['yellow', '🟨'],
          ['green', '🟩']]

def to_ascii(grid, color):
#    if color not in colors[0]:
#        color = 'white'

    for name, emoji in colors:
        if color == name:
            square = emoji
            break

    grid_ascii = []

    for row in grid:
        row_ascii = []
        for pixel in row:
            if pixel == 1:
                row_ascii.append(square)
            else:
                row_ascii.append("⬛")
        grid_ascii.append(row_ascii)

    ascii_string = "\n".join("".join(row) for row in grid_ascii)
    pyperclip.copy(ascii_string)

