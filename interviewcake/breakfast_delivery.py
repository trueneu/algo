from collections import Counter

delivery_id_confirmations = [1, 1, 2, 3, 2, 99, 99, 3, 5]

c = Counter(delivery_id_confirmations)
for delivery_id in c:
    if c[delivery_id] == 1:
        print(delivery_id)
        break

# or ...

d = set()
for delivery_id in delivery_id_confirmations:
    if delivery_id in d:
        d.discard(delivery_id)
    else:
        d.add(delivery_id)

for x in d:
    print(x)
