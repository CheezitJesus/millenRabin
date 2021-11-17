def miller_rabin(n, k, a):

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


k = 1;

errorRates = []

for i in range(95000, 105000):
    if i % 2 == 0:
        pass
    else:
        prob = 0
        for a in range(2, i):
            if a % 2 == 0:
                pass
            elif miller_rabin(i, k, a) == False:
                prob += 1
        if prob == 0:
            #print(i)
            pass
        else:
            prob = prob / 2
            #print(str(i) + " is not prime with error rate: " + str(prob / i))
            if prob / i <= .25:
                errorRates.append((prob/i,i))
errorRates.sort(reverse=True)
for i in range(0,9):
    print(errorRates[i])
