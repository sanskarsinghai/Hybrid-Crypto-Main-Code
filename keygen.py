import random as ra

#if any users have same name or same dob or other thing same so it may be risk of same key generation
# or attacker may generate the account by using user details

l=['sanskar','singhai','12-09-2001',9691513053,'sanskar12singhai']
v=list(range(0,5))
s=''
t=''
for _ in range(0,4):
    a=ra.choice(v)
    v.remove(a)
    t+=str(a)+','
    if type(l[a])!=str:
        s+=str(l[a])
    else:
        s+=l[a]

if type(l[v[0]])!=str:
    s+=str(l[v[0]])
else:
    s+=l[v[0]]
t+=str(v[0])+','
print(t,len(t))

print(s)

k=''
c=0

# for _ in range(0,16):
#     a=ra.choice(range(0,len(s)))
#     t+=str(a)+','
#     k+=s[a]
#     c+=1
# t=t[:len(t)-1]

p=ra.choice(range(0,14))
for _ in range(0,14):
       a=ra.choice(range(0,len(s)))
       t+=str(a)+','
       k+=s[a]
# if p=='l':
#         k+=str(l[3])
# else:
#         k=str(l[3])+k

k=k[:p]+str(l[3])+k[p:]

t=t[:len(t)-1]
t=str(p)+','+t
#till
print(k)

de=t.split(',')

# d=''
# for i in range(5,len(de)):
#     d+=s[int(de[i])]

d=''
for i in range(6,len(de)):
        d+=s[int(de[i])]
    
# if t[0]=="l":
#         d+=str(l[3])
# else:
#         d=str(l[3])+d

d=d[:int(de[0])]+str(l[3])+d[int(de[0]):]
#till

print(d)
