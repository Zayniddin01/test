from dictionary import words
import random

def get_word():
    keys, values = random.choice(list(words.items()))
    return keys, values

def test(x):
    t = []
    n = []
    r = []
    while x != 0:
        en, uz = get_word()
        t = [en, uz]
        tas = random.choice(list(t))
        if tas in r:
            continue
        j = input(f"{tas}: ")
        if j in words.values():
            if j == uz:
                t.append(en)
                print("to'gri\n")
            else:
                n.append(en)
                print("nato'g'ri\n")
        elif j in words.keys():
            if j == en:
                t.append(uz)
                print("to'g'ri\n")
            else:
                n.append(uz)
                print("nato'g'ri\n")
        r.append(tas)
        x -= 1
    otvet = f"Siz {len(t)}ta to'g'ri {len(n)}ta noto'g'ri javob topdingiz"
    otvet += f"\nto'g'ri javoblariz: {t}"
    otvet += f"\nnato'g'ri javoblariz: {n}"
    return otvet

q = test(40)
print(q)



