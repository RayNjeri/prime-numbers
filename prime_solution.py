def prime_num(n):
    if n<2:
        return False
    else:
        for i in range(2, n+1):
            if n % i == 0:
                return False
        return True
print(prime_num)



def prime_list(a):
    prime=[]
    for n in range(2, n):
        if prime_num (i):
            prime.append(n)
    return prime        








