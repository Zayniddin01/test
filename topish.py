import random
from uzwords import words

# def code():
    # tasodif = list(r.sample(range(10), 4))
    # m = []
    # for n in tasodif:
    #     t = str(n)
    #     m.append(t)
    #     if m[0] == "0":
    #         u = list(r.sample(range(1,10),1))
    #         for i in u:
    #             m[0] = str(i)
    # return int(m[0]+m[1]+m[2]+m[3])

def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

# def play():
#     word = get_word()
#     word_letters = set(word)  
#     user_letters = ""

#     print(f"Salom, men {len(word)} ta harfdan iborat so'z o'yladim topa olasizmi")
#     while word_letters:
#         print(display(user_letters, word))
#         if user_letters:
#             print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")

#         letter = msg.upper()
#         if letter in user_letters:
#             print("Oldin bu harflarni kiritgansiz. Boshqa harf kiriting")
#             continue
#         elif letter in word:
#             word_letters.remove(letter)
#             print(f"{letter} harfi to'g'ri")
#         else:
#             print("Bunday harf yo'q")
#         user_letters += letter
#     print(f"Tabriklayman {word} so'zini {len(user_letters)} ta urinishda topdingiz")
