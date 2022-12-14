def syracuse(n):
    while n !=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        print(n)

print(syracuse(3))






def testeConjecture(n_max):
    while n_max!=1:
        if n_max%2==0:
            n_max=n_max//2
        else:
            n_max=n_max*3+1
        print(n_max)
print(testeConjecture(10000))