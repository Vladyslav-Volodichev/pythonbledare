text = input("text fdp: ")

def capital_indexes():
    num = 0
    Xl = []


    while len(text) > num:
        if text[num].isupper():
            Xl.append(num)

        num = num + 1

    print(Xl)


capital_indexes()