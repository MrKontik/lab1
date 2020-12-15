"""Слайд 3 Рисовашки """

"""1 задание"""
print("1 задание")

def frame(w,h):
    print(w*"*")
    for i in range(h-2):
        print("*"+(w-2)*" "+"*")
    print(w*"*")


frame(3,4)
print()
frame(5,5)

print("2 задание")
def frame(w,h,s):
    print(w*s)
    for i in range(h-2):
        print(s+(w-2)*" "+s)
    print(w*s)
    

print()
frame(3,4,"-")
print()
frame(5,5,"-")

print("3 задание")

def frame(w,h,f):
    for i in range(f):
        print(w*"*")
    for i in range(h-f*2):
        print("*"*f+(w-f*2)*" "+"*"*f)
    for i in range(f):
        print(w*"*")
    

print()
frame(6,7,2)
print()
frame(8,8,3)