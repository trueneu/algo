def getFieldCell(field, x, y):
    if y < 0 or y >= len(field) or x < 0 or x >= len(field[y]):
        return -1
    return field[y][x]

def bombAdjacentCells(field, x_list, y_list):
    for y in y_list:
        for x in x_list:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x0 = x + dx
                    y0 = y + dy
                    if getFieldCell(field, x0, y0) == 1:
                        if not(x0 in x_list and y0 in y_list):
                            return False
                        else:
                            field[y0][x0] = 2
                    elif getFieldCell(field, x0, y0) == -1:
                        pass
                    else:
                        field[y0][x0] = 2
    return True


def validateShip(field, x, y):
    x_list = list()
    y_list = list()
    vert = (getFieldCell(field, x, y - 1) == 1 or getFieldCell(field, x, y + 1) == 1)
    hor = (getFieldCell(field, x - 1, y) == 1 or getFieldCell(field, x + 1, y) == 1)
    if vert and hor:
        return False

    elif not vert and not hor:
        x_list.append(x)
        y_list.append(y)
        bombAdjacentCells(field, x_list, y_list)
    elif vert:
        x_list.append(x)
        y_list.append(y)

        if getFieldCell(field, x, y - 1) == 1:
            y0 = y - 1
            while getFieldCell(field, x, y0) == 1:
                y_list.append(y0)
                y0 -= 1

        if getFieldCell(field, x, y + 1) == 1:
            y0 = y + 1
            while getFieldCell(field, x, y0) == 1:
                y_list.append(y0)
                y0 += 1

    elif hor:
        x_list.append(x)
        y_list.append(y)

        if getFieldCell(field, x - 1, y) == 1:
            x0 = x - 1
            while getFieldCell(field, x0, y) == 1:
                x_list.append(x0)
                x0 -= 1

        if getFieldCell(field, x + 1, y) == 1:
            x0 = x + 1
            while getFieldCell(field, x0, y) == 1:
                x_list.append(x0)
                x0 += 1

    if not bombAdjacentCells(field, x_list, y_list):
        return -1
    else:
        return len(x_list) * len(y_list)

def validateBattlefield(field):
    submarines = 0
    destroyers = 0
    cruisers = 0
    battleships = 0
    y = 0
    while y < len(field):
        x = 0
        while x < len(field[y]):
            if field[y][x] == 1:
                r = validateShip(field, x, y)
                if r == -1:
                    return False
                elif r == 1:
                    submarines += 1
                elif r == 2:
                    destroyers += 1
                elif r == 3:
                    cruisers += 1
                elif r == 4:
                    battleships += 1
                else:
                    return False
            x += 1
        y += 1
    if submarines == 4 and destroyers == 3 and cruisers == 2 and battleships == 1:
        return True
    else:
        return False


battleField = [  [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validateBattlefield(battleField))