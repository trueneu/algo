s = '123 45 6'


def justify(orig_s, width):
    s = orig_s.split()
    result = ''
    while s:
        part = []
        for word in s:
            part.append(word)
            l = sum(map(len, part)) + len(part) - 1
            if l > width:
                part.pop()
                s = s[len(part):]
                break
        else:
            result += " ".join(part)
            return result
        spaces = [1] * (len(part) - 1)
        if spaces:
            while sum(map(len, part)) + sum(spaces) != width:
                min_space = min(spaces)
                for i, space in enumerate(spaces):
                    if space == min_space:
                        spaces[i] += 1
                        break
            r = ''
            for i, word in enumerate(part):
                r += word + ' ' * (spaces[i] if i < len(part) - 1 else 0)
        else:
            r = part[0]
        result += r + '\n'

    return result
print(justify(s, 4))
