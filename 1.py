def is_prime(x):
    f=True
    for i in range (2,int(x**0.5)):
        if x%i == 0:
            f=False
    return(f)
n=int(input('PLEASE ENTER YOUR NUMBER: '))
print(is_prime(n))