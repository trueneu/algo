f = open('contacts.txt')

#n = int(input().strip())
n = int(f.readline().strip())

db = dict()
for _ in range(n):
    #query = input().strip().split()
    query = f.readline().strip().split()
    if query[0] == 'add':
        i = 1
        while i <= len(query[1]):
            try:
                db[query[1][:i]] += 1
            except KeyError:
                db[query[1][:i]] = 1
            i += 1
    else:
        try:
            print(db[query[1]])
        except KeyError:
            print(0)