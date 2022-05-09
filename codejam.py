#n,m,r,c = map(int,input().strip().split())
#l=list(map(int,input().strip().split()))[:n]
def solve():
    n = int(input())
    l = list(map(int,input().strip().split()))
    l.sort()
    i = 0
    c = 1
    while(i < n):
        if l[i] >= c:
            # print(l[i],i)
            c += 1
        else:
            c = c
        i += 1
    print(c-1)
    # r,c = map(int,input().strip().split())
    # nod = r*c
    # row1 = "+-" * c + "+"
    # row2 = "|." * c + "|"
    # for i in range(r):
    #     if i == 0:
    #             print(".."+("+-"*(c-1)) + "+")
    #             print(".."+"|."*(c-1) + "|")
    #     else:
    #         print(row2)    
    #     print(row1)


    '''vestigium
    n = int(input())
    l = [[]]*n
    t = 0
    rc = 0
    cc = 0
    for j in range(n):
        l[j] = list(map(int,input().strip().split()))[:n]
        l1 = [[0]*n]*n
    for i in range(n):
        for j in range(n):
            #l1[j][i] = l[i][j]
            if i == j:
                t = l[i][j] + t
    result = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]            
    print(result)    
    for i in range(n):
        for j in range(n):
            if l[i].count(l[i][j]) >1:
                rc = rc + 1
                break
    for i in range(n):
        for j in range(n):
            if result[i].count(result[i][j]) >1:
                cc = cc + 1
                break        
    print(t,rc,cc)              
    ''' 
    # n = int(input())
    # l =  list(map(int,input().strip().split()))[:n]
    # c = 0
    # for i in range(n-1):
    #     if l == sorted(l):
    #         c = c + n - i - 1
    #         break
    #     else:j = minvalue(l,i,n)
    #     if i <= j:
    #         c = j - i + 1 + c
    #     else:c = c + 1
    #     insert_sort(l,i,j)
    # print(c)
    
             
def insert_sort(l,k,j):
    for i in range(k,j+1):
        p = i
        while p>0 and l[p]<l[p-1]:
            (l[p],l[p-1])=(l[p-1],l[p])
            p=p-1             

def minvalue(l,i1,n1):
    m = 101
    j1 = 0
    for k in range(i1,n1):
        if m > l[k]:
            j1 = k
            m = l[k]
    return j1        

t = int(input())
i = 1
while(t>0):
    print("Case #",i,": ",sep = "",end="")
    solve()
    i = i + 1
    t = t - 1
