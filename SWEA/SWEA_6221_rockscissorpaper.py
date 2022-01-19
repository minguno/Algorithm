L = ["가위", "바위", "보"]
Man1 = input()
Man2 = input()

if (Man1 == "바위" and Man2 == "가위") or (Man1 == "가위" and Man2 == "보") or (Man1 == "보" and Man2 == "바위"):
    print("Result : Man1 Win!")
elif (Man1 == Man2):
    print("Result : Draw")
else:
    print("Result : Man2 Win!")