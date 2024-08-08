import random as r
import telebot
from uzwords import words

from topish import get_word, display



TOKEN = '7253711263:AAGrdREwg8KrIPS3suGxftN1fMNRh3klstE'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Asalomu aleykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob,)

@bot.message_handler(commands=['j']) 
def play(message):
    msg = message.text
    word = get_word()
    word_letters = set(word)  
    user_letters = ""

    s = f"Salom, men {len(word)} ta harfdan iborat so'z o'yladim topa olasizmi"
    while word_letters:
        s = display(user_letters, word)
        if user_letters:
            s= f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}"

        letter = msg.upper()
        if letter in user_letters:
            s= "Oldin bu harflarni kiritgansiz. Boshqa harf kiriting"
            continue
        elif letter in word:
            word_letters.remove(letter)
            s= f"{letter} harfi to'g'ri"
        else:
            s= "Bunday harf yo'q"
        user_letters += letter
    s= f"Tabriklayman {word} so'zini {len(user_letters)} ta urinishda topdingiz"
    bot.reply_to(message, s)
bot.polling()






