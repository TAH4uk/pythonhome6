# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def evk(a, b):
    while(b > 0):
        a, b = b, a % b
    return a
    
def cut(pair):
    g = evk(pair[0], pair[1])
    return (pair[0] // g, pair[1] // g)
    
n = 11
lst = []
for i in range(1, n+1):
    for j in range(i+1,n+1):
        frac = cut((i, j))
        lst.append(frac)
sort = list(set(lst))
for q in sorted(sort, key = lambda x: x[0] / x[1]): 
    print(str(q[0]) + "/" + str(q[1]))