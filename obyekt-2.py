from dictionary import words, new_words
import random


def get_word():
    keys, values = random.choice(list(new_words.items()))
    tas = [keys, values]
    t = random.choice(list(tas))
    return t, keys, values

def test(x):
    q = []
    t = []
    n = []
    k = 1
    while k <= x:
        tas, en, uz = get_word()
        if tas in q:
            continue
        j = input(f"{tas}: ")
        if j in new_words.keys() or j in new_words.values():
            if j == en:
                t.append(tas)
                print(k)
                print("To'g'ri\n")
            elif j == uz:
                t.append(tas)
                print(k)
                print("To'g'ri\n")
            elif j != en:
                n.append(tas)
                print(k)
                print("Nato'g'ri\n")
            else:
                n.append(tas)
                print(k)
                print("Nato'g'ri\n")
        else:
            n.append(tas)
            print(k)
            print("Nato'g'ri\n")
        k += 1
        q.append(tas)
    otvet = f"Siz {len(t)}ta to'g'ri {len(n)}ta nato'g'ri javob topdingiz"
    return otvet
e = test(148)
print(e)
        
        