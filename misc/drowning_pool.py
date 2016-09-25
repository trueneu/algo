pool = [1, 3, 6, 2, 2, 2, 4, 1]

def drown_the_pool(pool):
    i = 0
    volumes1 = [0] * len(pool)
    volumes2 = [0] * len(pool)
    water_volume = 0
    max_height = -1
    while i < len(pool):
        if max_height > pool[i]:
            volumes1[i] = max_height - pool[i]
        else:
            max_height = pool[i]
        i += 1

    max_height = -1
    i = len(pool) - 1
    while i >= 0:
        if max_height > pool[i]:
            volumes2[i] = max_height - pool[i]
        else:
            max_height = pool[i]
        i -= 1

    for index, value in enumerate(volumes1):
        water_volume += min(value, volumes2[index])


    # end error correction

    return water_volume


print(drown_the_pool(pool))