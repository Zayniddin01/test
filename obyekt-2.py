from dictionary import words
import random


def get_word():
    keys, values = random.choice(list(words.items()))
    tas = [keys, values]
    t = random.choice(list(tas))
    return t, keys, values

def test(x):
    q = []
    t = []
    n = []
    while x != 0:
        tas, en, uz = get_word()
        if tas in q:
            continue
        j = input(f"{tas}: ")
        if j in words.keys() or j in words.values():
            if j == en:
                t.append(tas)
                print("To'g'ri\n")
            elif j == uz:
                t.append(tas)
                print("To'g'ri\n")
            elif j != en:
                n.append(tas)
                print("Nato'g'ri\n")
            else:
                n.append(tas)
                print("Nato'g'ri\n")
        else:
            n.append(tas)
            print("Nato'g'ri\n")
        x -= 1
        q.append(tas)
    otvet = f"Siz {len(t)}ta to'g'ri {len(n)}ta nato'g'ri javob topdingiz"
    return otvet
e = test(120)
print(e)
        
        