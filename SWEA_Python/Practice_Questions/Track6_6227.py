number = []

for i in range(100, 301):
    a = int(i/100)
    b = int(i/10)

    if a % 2 == 0 and b % 2 == 0 and i % 2 == 0:
        number.append(str(i))

print(",".join(number))