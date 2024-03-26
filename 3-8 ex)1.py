katok=[('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]
print(katok)

def insert_data(name, count):
    katok.append(None)
    kLen=len(katok)

    if count < katok[kLen-2][1]:
        katok[kLen-1] = name, count
    else:
        for i in range (kLen-1, 0, -1):
            if count < katok[i-1][1]:
                pos = i
                break
            else : pos = 0
        for j in range (kLen-1, pos, -1):
            katok[j] = katok[j-1]
        katok[j-1]=name, count

insert_data('미나',40)
print(katok)
