for t in range(int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    ar=sorted(ar)
    c=0
    for i in range(n):
        k=i+2
        for j in range(i+1,n):
                while (k<n) and (ar[i]+ar[j]>ar[k]):
                    k+=1
                c=c+(k-j-1)
    print(c)
