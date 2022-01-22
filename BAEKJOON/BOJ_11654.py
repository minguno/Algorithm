something = input()

if type(something) == str:
    print(ord(something))
elif type(something) == int:
    print(chr(something))