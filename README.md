# Python_practice_5
Q1
다음은 Calculator 클래스이다.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자. 즉 다음과 같이 동작하는 클래스를 만들어야 한다.

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력
Q2
객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자. 즉 다음과 같이 동작해야 한다.

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력
단 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
Q3
다음 결과를 예측해 보자.

하나.

>>> all([1, 2, abs(-3)-3])
둘.

>>> chr(ord('a')) == 'a'
Q4
filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.

Q5
234라는 10진수의 16진수는 다음과 같이 구할 수 있다.

>>> hex(234)
'0xea'
이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.

※ 내장 함수 int를 활용해 보자.

Q6
map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.

Q7
다음 리스트의 최댓값과 최솟값의 합을 구해 보자.

[-8, 2, 7, 5, -3, 5, 0, 1]
Q8
17 / 3의 결과는 다음과 같다.

>>> 17 / 3
5.666666666666667
위와 같은 결괏값 5.666666666666667을 소숫점 4자리까지만 반올림하여 표시해 보자.

Q9
다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트(C:\doit\myargv.py)를 작성해 보자.

C:\> cd doit
C:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10
55
※ 외장 함수 sys.argv를 사용해 보자.
