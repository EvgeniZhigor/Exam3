#Задание 1
def karta(card):
    return '*'*len(card[:-4])+card[-4:]
print(karta('1111222233334444'))