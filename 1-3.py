h=int(input("점수을 입력하세요 : "))

if h >= 90:
    grade = 'A'
elif 80<= h < 90:
    grade = 'B'
elif 80<= h < 90:
    grade = 'C'
elif 80<= h < 90:
    grade = 'D'
else:
    grade='F'

print('%d점은 %c학점' % (h,grade))
