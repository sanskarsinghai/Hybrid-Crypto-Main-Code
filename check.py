f1=open('f2\d2.txt')
f2=open('f2\origin.txt')

s=''
for i in f1:
    s+=i

t=''
for i in f2:
    t+=i
f=0
for i in range(len(s)):
    if s[i]!=t[i]:
        print(False)
        f=1
        print(i,s[i],t[i])

if f==0:
    print("Process Successfully completed")      