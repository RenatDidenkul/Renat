a = int(input('a = '))
b = int(input('b = '))

def number(a, b):
    if a % b == 0:
        return b
    else:
        return number(b, a%b)

print (number(a, b))