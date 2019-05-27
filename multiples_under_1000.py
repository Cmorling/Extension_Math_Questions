under = 1000
total = 0
multiples_3 = []
multiples_5 = []
for i in range(1, under + 1):
    if i % 3 == 0:
        multiples_3.append(i)
    if i % 5 == 0:
        multiples_5.append(i)
for i in multiples_3:
    total += i
for i in multiples_5:
    total += i
print(total)