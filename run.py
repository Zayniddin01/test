import random as r
import random
def son_topish(max=10):
      son = list(r.sample(range(max), 1))

      if son[0] == 0:
            son[0]+=1
      ishora = True
      p = 0
      print(f"Men o'ylagan son 1 dan {max} gacha toping:")
      while ishora:
            p+=1
            son_top = input(f">>>")
            for n in son:
                  if n == int(son_top):
                        print(f"Siz {p} ta urunishda to'g'ri topdingiz: {son_top} raqami edi.")
                        ishora = False
                  elif n <= int(son_top):
                        print(f"Men o'ylagan son {son_top} dan kichik")
                  else:
                        print(f"Men o'ylagan son {son_top} dan katta")
                  
      return p

def son_oyla(x=10):
      print("Endi siz son o'ylisiz men topaman!")
      input("boshladikmi: ")
      min = 1
      max = x
      t = 0
      while True:
            t+=1
            if min != max:
                  son = random.randint(min, max)
            else:
                  son = min
            print(f"Siz o'ylagan son {son}: + bundan katta, - bundan kichkina, = to'g'ri")
            top = str(input(f">>>"))
            if top == "-":
                  max =son - 1
            elif top == "+":
                  min =son + 1
            else:
                  break
            
      print(f"Men {t} urunishda to'g'ri topdim: Siz {son} raqamini o'ylagan ekansiz")
      return t

def win(max=10):
      win1 = son_topish(max)
      win2 = son_oyla(max)
      if win1<=win2:
            print(f"Siz mendan {win2-win1} ta urunishda kam topdingiz Umumiy xisobda siz YUTINGIZ!!")
      elif win1>=win2:
            print(f"Men sizdan {win1-win2} ta urunishda kam topdim Umumiy xisobda men YUTDIM!!")
      else:
            print(f"Xisoblar teng DURANG!!")
      pass

t = win()
print(t)