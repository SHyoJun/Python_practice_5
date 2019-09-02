# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)
# Q2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value>=100:
            self.value=100

cal2 = MaxLimitCalculator()
cal2.add(50) # 50 더하기
cal2.add(60) # 60 더하기

print(cal2.value) # 100 출력
# Q3
# False
# True
# Q4
print(list(filter(lambda a : a>0, [1, -2, 3, -5, 8, -3])))
# Q5
print(int(0xea))
# Q6
print(list(map(lambda a : a*3, [1, 2, 3, 4])))
# Q7
test = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(test)+min(test))
# Q8
print(round(17 / 3, 4))
# Q9
import sys
b = sys.argv[1:]
b = list(map(lambda a : int(a), b))
num = 0
try:
    for i in b:
        num += i
    print(num)
except:
    print("no data")