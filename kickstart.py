#n,m,r,c = map(int,input().strip().split())
#l=list(map(int,input().strip().split()))[:n]
def solve():
    k = 0
    g =int(input())
    a = 8 * g
    n1 = g // 2
    for i in range(1,n1+1):
        if (((((2*i)-1)**2 + a)**0.5).is_integer()):
            k = k + 1

    print(k+1)        



t = int(input())
i = 1
while(t>0):
    print("Case #",i,": ",sep = "",end = "")
    solve()
    i = i + 1
    t = t - 1
