"""Слайд 2 For """

"""1 задание"""
print("1 задание")
def sumTwoNumberPast(n):
    l=[1,1,1]
    for i in range(2,n):
        l[2]=l[1]+l[0]
        l[0]=l[1]
        l[1]=l[2]
    print(l[2])

sumTwoNumberPast(1)
sumTwoNumberPast(2)
sumTwoNumberPast(3)
sumTwoNumberPast(4)
sumTwoNumberPast(5)
sumTwoNumberPast(6)
sumTwoNumberPast(7)


print("2 задание")
def sumThreeNumberPast(n):
    l=[1,1,1,1]
    for i in range(3,n):
        l[3]=l[1]+l[0]+l[2]
        l[0]=l[1]
        l[1]=l[2]
        l[2]=l[3]
    print(l[3])

sumThreeNumberPast(1)
sumThreeNumberPast(2)
sumThreeNumberPast(3)
sumThreeNumberPast(4)
sumThreeNumberPast(5)
sumThreeNumberPast(6)
sumThreeNumberPast(7)


print("3 задание")
def squareOddNumbers(n):
    l=[i*i for i in range(1,n,2)]
    print(l)
squareOddNumbers(20)


print("4 задание")
def summAndComposition(a,b):
    sum=0
    comp=1
    for i in range(a,b+1):
        sum=sum+i
        comp=comp*i
    print("Сумма: "+str(sum))
    print("Произведение: "+str(comp))
    print()

summAndComposition(1,5)
 
print("5 задание")
def evenAndOddSeparately(a,b):
    even=[i for i in range(a+(a%2),b+1,2)]
    odd=[i for i in range(a+((a%2-1)*-1),b+1,2)]
    print(even)
    print(odd)
    print()

evenAndOddSeparately(1,23)
evenAndOddSeparately(2,23)
evenAndOddSeparately(3,23)
evenAndOddSeparately(4,23)
evenAndOddSeparately(5,23)



print("6 задание")


def divineDivider(l):
    positive=[i for i in l if i>-1]
    negative=[i for i in l if i<0]
    print(positive) 
    print(negative)

divineDivider([1,4,-3,0,-7,10,12,-10,-3])