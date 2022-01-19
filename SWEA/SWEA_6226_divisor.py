number = []

for i in range(1, 201):
    if (i % 7 == 0) and (i % 5 != 0):
        number.append(i)

number_final = [str(a) for a in number]
print(",".join(number_final))