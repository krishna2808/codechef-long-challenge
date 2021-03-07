for _ in range(int(input())):
    s,count  = input(), 0
    if(s[0] == '1'):
        count += 1 
    for i in range(1,len(s)):
        if(s[i]=='1' and s[i] != s[i-1]):
            count += 1 
    print(count)        
            
