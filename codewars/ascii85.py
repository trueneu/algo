def toAscii85(data):
    i = 0
    res = ""
    while i < len(data):
        dword_to_encode = 0
        chars_to_chop = 0
        for j in range(0, 4):
            pos = i + j
            dword_to_encode *= 256
            if pos < len(data):
                dword_to_encode += ord(data[pos])
            elif not chars_to_chop:
                chars_to_chop = 4 - j

        piece = ""
        if dword_to_encode == 0 and chars_to_chop == 0:
            piece = "z"
        else:
            for j in range(0, 5):
                c = dword_to_encode % 85 + 33
                dword_to_encode = int(dword_to_encode / 85)
                piece = chr(c) + piece

        res += piece[:len(piece) - chars_to_chop]

        i += 4

    return '<~' + res + '~>'


def fromAscii85(data):
    data_unwrapped = data[2:-2].replace(' ', '').replace('\n', '')  # chop off boundaries <~ ~>, remove whitespace
    print(data)
    i = 0
    res = ""
    while i < len(data_unwrapped):
        encoded_piece = ""
        chars_to_chop = 0
        if data_unwrapped[i] == 'z':
            res += chr(0) * 4
            i += 1
            continue

        for j in range(0, 5):
            pos = i + j
            if pos < len(data_unwrapped):
                encoded_piece += data_unwrapped[pos]
            elif not chars_to_chop:
                chars_to_chop = 5 - j
                encoded_piece += 'u'
            else:
                encoded_piece += 'u'

        encoded_dword = 0
        #for j in range(4, -1, -1):
        for j in range(0, 5):
            encoded_dword += (ord(encoded_piece[j]) - 33) * (85 ** (4 - j))

        piece = ""
        for j in range(0, 4):
            byte = encoded_dword % 256
            encoded_dword = int(encoded_dword / 256)
            piece = chr(byte) + piece

        res += piece[:len(piece) - chars_to_chop]
        i += 5


    return res

#print(toAscii85('somewhat difficult'))
#print(fromAscii85('<~ARTY*~>'))
#print(fromAscii85('<~F)Po,GA(E,+Co1uAnbatCif~>'))
#print(toAscii85(chr(0)))
print(fromAscii85('<~GA(]4ATMg!@	q?d)ATMr91B~>'))