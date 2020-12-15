"""1 слайд"""

"""1 задание"""
def runAllDays(x):
    sum=0
    scope=2
    i=0
    while (sum<x):
        sum=sum+scope
        i=i+1
        scope=scope*2 
    return i
print("Результат первого задания 1 слайда")
print(runAllDays(1000))

print(runAllDays(10000))


"""3 задание"""
print("Результат 3 задания 1 слайда")
start=10
percent=1.15
sum=0
i=0
while(i<16):
    sum=sum+ (start*percent)*2
    i=i+1
    start=start*percent
print(sum)


"""4 задание"""
print("Результат 4 задания а) 1 слайда")
start=10
percent=1.1
i=0
while(start<20):
    i=i+1
    start=start*percent
print(i)

print("Результат 4 задания б) 1 слайда")
start=10
percent=1.1
sum=0
i=0
while(sum<100):
    sum=sum+ (start*percent)*2
    i=i+1
    start=start*percent
print(i)