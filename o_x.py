cells = "_________"

print("-" * 9)
for i in range(3):
    print("| " + cells[0 + 3 * i] + " " + cells[1 + 3 * i] + " " + cells[2 + 3 * i] + " |")
print("-" * 9)


def x_turn():
    return "X"


def o_turn():
    return "O"


moves_made = 1


def coordinates(x, y):
    global cells
    global moves_made
    cells = [q for q in cells]
    moves_made += 1
    if moves_made % 2 == 0:
        cells[(3 - y) * 3 + (x - 1)] = x_turn()
    else:
        cells[(3 - y) * 3 + (x - 1)] = o_turn()
    print("-" * 9)
    for j in range(3):
        print("| " + cells[0 + 3 * j] + " " + cells[1 + 3 * j] + " " + cells[2 + 3 * j] + " |")
    print("-" * 9)


while True:
    coord_input = input("Enter the coordinates: ").split()
    coord = "".join(coord_input)
    if not coord.isnumeric():
        print("You should enter numbers!")
        continue
    elif abs(int(coord_input[0])) > 3 or abs(int(coord_input[1])) > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    a, b = [int(i) for i in coord_input]
    cell_check = cells[(3 - b) * 3 + (a - 1)]

    if "X" in cell_check or "O" in cell_check:
        print("This cell is occupied! Choose another one!")
    else:
        coordinates(a, b)

    x_count = 0
    o_count = 0
    blank_count = 0

    # if x_count - o_count == 1:

    for i in cells:
        if i == "X":
            x_count += 1
        elif i == "O":
            o_count += 1
        else:
            blank_count += 1

    check = "".join(cells)
    string_check = check[0:3], check[3:6], check[6:9], check[0:7:3], check[1:8:3], check[2:9:3], check[0:9:4], check[2:7:2]

    if "XXX" in string_check:
        print("X wins")
        break
    elif "OOO" in string_check:
        print("O wins")
        break
    elif blank_count == 0:
        print("Draw")
        break
