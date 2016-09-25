half1 = []
half2 = [5, 6, 7, 8]
deck = [5, 6, 7, 8]

def is_deck_riffled(deck, half1, half2):
    c1 = c2 = 0
    for card in deck:
        if len(half1) > c1 and half1[c1] == card:
            c1 += 1
        elif len(half2) > c2 and half2[c2] == card:
            c2 += 1
        else:
            return False
    return True

print(is_deck_riffled(deck, half1, half2))