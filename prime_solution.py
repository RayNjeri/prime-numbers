def prime_num(n):
    if n<2:
        return False
    else:
        for i in range(2, n+1):
            if n % i == 0:
                return False
        return True
print(prime_num)

def prime_list(n):
    prime=[]
    for k in range(2, n+1):
        for j in range(1, n+1):
            divisor = []
            if k%j ==0:
                divisor.append(j)
                if len(divisor) == 2:
                    print (divisor)
                    


    return prime_list                





