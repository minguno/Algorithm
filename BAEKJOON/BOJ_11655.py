# ROT13

from sys import stdin
rd = stdin.readline

s = rd()
sol = ''
for c in s:
    if c.isalpha():
        if c.isupper():
            if ord(c) > 77:
                sol += chr(ord(c) - 13)
            else:
                sol += chr(ord(c) + 13)
        else:
            if ord(c) > 109:
                sol += chr(ord(c) -13)
            else:
                sol += chr(ord(c) + 13)
    elif c.isdigit():
        sol += c
    else:
        sol += c
print(sol)
