num = int(input('단 입력: '))

for i in range(1, 10):
    print('%d x %d = %d' % (num, i, num*i))

start = int(input('시작단 입력: '))
end =int(input('종료단 입력: '))
for i in range(start, end+1):
    i=1
    while i <= 9:
        print('%d x %d = %d' % (num, i, num*i))
        i += 1
print('구구단 프로그램 종료')
