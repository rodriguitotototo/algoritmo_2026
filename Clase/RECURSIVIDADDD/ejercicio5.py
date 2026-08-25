
 #  Desarrollar una función que permita convertir un número romano en un
 #  número decimal.

def romano_decimal(r, i=0):
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    if i >= len(r):
        return 0

    if i < len(r)-1 and val[r[i]] < val[r[i+1]]:
        return (val[r[i+1]] - val[r[i]]) + romano_decimal(r, i+2)
    else:
        return val[r[i]] + romano_decimal(r, i+1)


num = input("romano: ").upper()
print(romano_decimal(num))