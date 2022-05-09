# from itertools import combinations

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


n = int(input())
r = int(input())
s = input().strip().split(",")
size_of_ps = 2**n
# ans = []
# for c in range(size_of_ps):
#     a = "("
#     for j in range(n):
#         if((c&(1<<j))>0):
#             a = a + s[j] + ","       
#     a = a + ")"
#     ans.append(a)   
#     r = r - 1        
# print(sorted(ans))        

if r == 1:
    print("{}")
else:
    for i in range(0,n+1):
        for e in combinations(s,i):
            if r == 1:
                print(e)
            r = r - 1    