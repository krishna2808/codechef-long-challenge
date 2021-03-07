N, H,x = map(int, input().split())
ar = list(map(int, input().split()))
for i in ar:
    if(x+i >= H):
        print('YES')
        break
else:
    print('NO')
