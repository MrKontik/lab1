"""Слайд 4 """
import re

def algMoon(card):
    l=[card[i]*2 for i in range(len(card)%2,len(card),2)]
    l=sum([i if i<10 else i-9 for i in l])
    k=sum([card[i] for i in range((len(card)+1)%2,len(card),2)])
    res=k+l
    return res%10==0

def checkCard(numberCard):
    print("Проверяется карта: "+numberCard)
    if (re.search(r'^[0-9 ]*$',numberCard)):
        numberCard= re.sub(r' ','',numberCard)
        l=[int(i) for i in numberCard]
        if (algMoon(l)):
            print("Проверка прошла успешно")
        else:
            print("Проверка провалилась. Проверьте правильность введеных чисел")
    else:
        print("Вы вели неправильный номер карты, вводите только числа и пробелы пожалуйста. Попробуйте еще раз")


print("4 задание (4 вариант)") 
checkCard("4123d4567 8901 2349")
checkCard("adsfadsf")
checkCard("4123 4567 8901 1349")
checkCard("4123 4567 8901 2349")
checkCard("4  5  6  1     2  6  1  2     1  2  3  4     5  4  6  7")

print("Введите карту для проверки: (Для выхода введите 0)") 
while (True):
    inp=input()
    if(inp=="0"):
        break
    checkCard(inp)

