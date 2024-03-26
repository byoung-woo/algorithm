h=int(input("키를 입력하세요 : "))
w=int(input("몸무게를 입력하세요 : "))
bmi = w / ((h/100)*(h/100))
if bmi < 18:
    print("저체중")
elif 18<=bmi < 23:
    print("정상")
elif 23<=bmi < 25:
    print("과체중")
else:
    print("비만")

print('bmi: %.2f' %(bmi))
