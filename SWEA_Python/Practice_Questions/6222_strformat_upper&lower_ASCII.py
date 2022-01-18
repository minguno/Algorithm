A = str(input())

if (A.isalpha() != True):
    print(A)
elif (A.isupper() == True):
    result = A.lower()
    print("%s(ASCII: %d) => %s(ASCII: %d)" % (A, ord(A), result, ord(result)))
else:
    result = A.upper()
    print("%s(ASCII: %d) => %s(ASCII: %d)" % (A, ord(A), result, ord(result)))