t = int(input())

for j in range(t):
    n = int(input())
    c = 0
    l = ["" for _ in range(n)]
    for i in range(n):
        l[i] = input()
    for i in range(n):
        for j in range(n-1,i,-1):
            if i == j:continue
            elif i > j:break
            elif (l[i][0] == l[j][0] and l[i][1] != l[j][1]) or (l[i][0] != l[j][0] and l[i][1] == l[j][1]):c += 1
        if i > j:break
    print(c)
    # a = list(map(int,input().strip().split()))
    # d = {}
    # f = 1
    # e = -1
    # o = 0

    # for i in range(0,len(a),2):
    #     if a[i]%2 == 0:e = 1
    #     else: o = 1
    # for i in range(1,len(a),2):
    #     if a[i]%2 == 0:e = 2
    #     else: o = 2
    # if (e == o == 0) or (e == o == 2):print("NO")
    # else:print("YES")    
    
    # n,k = map(int,input().strip().split())
    # a = list(map(int,input().strip().split()))
    # a.sort()
    # # print("b",a)
    # for i in range(len(a)-2,-1,-1):
    #     for j in range(i-1,-1,-1):
    #         a[j] = a[j] - a[i]
    #     a[-1] = a[-1] - a[i]    
    # # print("a",a)
    # if a[-1] == k:
    #     print("YES") 
    # else:
    #     print("NO")
    
    # r,l,a = map(int,input().strip().split())
    # if r == l:
    #     if l == a:
    #         print(1)
    #     else:
    #         print((l//a) + (l%a))
    # elif l < a:print(l)
    # elif l == a:print(a-1)
    # else:
    #     if l%a != 0:print((l//a) + (l%a))
    #     else:print(((l-1)//a)+((l-1)%a))

    # s = input()
    # c = input()
    # if c in s:
    #     if(s.index(c)%2 == 0 and (len(s)-s.index(c)-len(c))%2 ==0):
    #         print("YES")
    #     else:
    #         print("NO")
    # else:
    #     print("NO")        
    # if len(s) == len(c):
    #     if s == c:
    #         print("YES") 
    #     else:
    #         print("NO")
    # else:
    #     j = 0
    #     n = len(s)
    #     while(j < n):
    #         if s[j] == c: 
    #             print("YES")
    #             break
    #         j  = j + 2    
    #     else:
    #         print("NO")      


