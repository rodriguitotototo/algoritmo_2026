
 #  Desarrollar una función que permita convertir un número romano en un
 #  número decimal.
def romano_decimal(r):
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
    res = 0
    i = 0

    while i < len(r):
        if i < len(r)-1 and val[r[i]] < val[r[i+1]]:
            res = res + (val[r[i+1]] - val[r[i]])
            i += 2
        else:
            res = res + val[r[i]]
            i += 1

    return res


num = input("romano: ").upper()
print(romano_decimal(num))