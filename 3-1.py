katok =["다현","정연","쯔위","사나","지효"]
print(katok)

print(katok[0])
print(katok[1])

katok.append(None)
print(katok)

katok[5]="모모"
print(katok)

print("데이터 삽입 : 중간 삽입")
katok.append(None)
print(katok)

katok[6]=katok[5]
katok[5]=None
print(katok)

katok[5]=katok[4]
katok[4]=None
katok[4]=katok[3]
katok[3]=None
print(katok)

katok[3]="미나"
print(katok)

print("데이터 삭제 : 중간삭제")
katok[4]=None
print(katok)

katok[4]=katok[5]
katok[5]=None
katok[5]=katok[6]
katok[6]=None
print(katok)

del(katok[6])
print(katok)
