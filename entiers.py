def somme_n(n):
    somme = 0
    for i in range(1, n+1):
        somme += i
    return somme

print(somme_n(7))