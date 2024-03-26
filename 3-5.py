px=[7,-4,0,5]
print(px)

x=2
pxVal=7*x**3-4*x**2+0*x**1+5*x**0
print(pxVal)

px=[7,-4,0,5]
polyStr="P(x) ="
polyStr += " + " + str(px[0]) + "x^" + str(3)
polyStr += " + " + str(px[1]) + "x^" + str(2)
polyStr += " + " + str(px[2]) + "x^" + str(1)
polyStr += " + " + str(px[3]) + "x^" + str(0)
print(polyStr)

def printPoly(p_x) :
    term =len(p_x) - 1
    polyStr = "P(x) = "

    for i in range(len(px)) :
        coef = p_x[i]

        if coef ==0 : # 계수가 0이면 생략 
            term -= 1
            continue
        if(coef >= 0 and i != 0) :
            polyStr += "+"
        
        polyStr +=str(coef)+"x^" + str(term)+" "
        term -= 1

    return polyStr

def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x) - 1
    for i in range(len(px)):
        coef=p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue

px = [7,-4,0, 5]

pStr= printPoly(px)
print(pStr)

xValue = int(input("X 값-->"))

pxValue = calcPoly(xValue,px)
print(pxValue)
