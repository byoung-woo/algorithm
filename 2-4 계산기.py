def multi(v1, v2):
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    res3 = v1 * v2
    res4 = v1 / v2
    retList.append(res1)
    retList.append(res2)
    retList.append(res3)
    retList.append(res4)
    return retList

myList = []
hap, sub, mul, div  = 0, 0, 0 , 0

myList = multi(100, 200)
hap = myList[0]
sub = myList[1]
mul = myList[2]
div = myList[3]
print("multi()에서 반환한 값 ==> %d, %d, %d, %.2f" %(hap, sub, mul, div))
