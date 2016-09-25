board = [['a', 'b', 'c', 'd', 'e'],
         ['a', 'b', 'c', 'd', 'e'],
         ['a', 'b', 'c', 'd', 'e'],
         ['a', 'b', 'c', 'd', 'e'],
         ['a', 'b', 'c', 'd', 'e']]

word = 'bbc'

def scrabble(pos_x, pos_y, used_letters, word_num_of_chars_found):
    if board[pos_y][pos_x] == word[word_num_of_chars_found - 1] and not used_letters[pos_y][pos_x]:
        if word_num_of_chars_found == len(word):
            return used_letters
        used_letters[pos_y][pos_x] = True
        i = -1
        j = -1
        while i < 2:
            while j < 2:
                if not pos_x < 0 and not pos_x > len(board[0]) - 1 and\
                    not pos_y < 0 and not pos_y > len(board) - 1:
                    scrabble(pos_x + i, pos_y + j, used_letters, word_num_of_chars_found + 1)
                j += 1
            i += 1
