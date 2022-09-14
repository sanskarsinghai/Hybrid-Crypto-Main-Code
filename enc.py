from telnetlib import PRAGMA_HEARTBEAT
import pyaes, secrets
from des import DesKey
from arc4 import ARC4
from stegano import lsb
import random as ra

# key = token_bytes(16)
key = ''

def keygen():
    global key
    
    print("Key generation is in progress...........")

    l=['sanskar','singhai','12-09-2001',9691513053,'sanskar12singhai@gmail.com']
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
    
    p=ra.choice(['s','l'])
    for _ in range(0,14):
       a=ra.choice(range(0,len(s)))
       t+=str(a)+','
       key+=s[a]

    if p=='l':
        key+=str(l[3])
    else:
        key=str(l[3])+key

    t=t[:len(t)-1]
    t=p+','+t

    key=key.encode('utf-8')
    
    print("Key generated successfully")

    return t

def aesenc():
    global key
    iv = secrets.randbits(64)
    
    f=open("f2\BinfileName11.bin")
    plaintext=''
    for i in f:
        plaintext+=i
    f.close()

    try:
        if len(plaintext)==0:
           raise Exception
    except Exception:
        print("\nEmpty file cannot be encrypted")
        exit()
    
    print("Encryption by aes is processing.........")

    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)

    f2=open('f2\BinfileName11.bin','wb')
    f2.write(ciphertext)

    print("Encryption by aes done")
    l=[iv,len(ciphertext)]
    return l

def desenc():
    global key
    
    f=open("f2\BinfileName12.bin")

    s=''
    for i in f:
        s+=i
    f.close()
    
    try:
        if len(s)==0:
           raise Exception
    except Exception:
        print("\nEmpty file cannot be decrypted")
        exit()
    
    print("Encryption by des is processing.........")

    key0 = DesKey(key)
    e=key0.encrypt(s.encode('utf-8'),padding=True)

    f2=open('f2\BinfileName12.bin','wb')
    f2.write(e)
    
    di=len(e)-len(s)

    print("Encryption by des done")
    l=[di,len(e)]
    return l

def rc4enc():
    global key
    
    f=open("f2\BinfileName13.bin")

    s=''
    for i in f:
        s+=i
    f.close()
    
    try:
        if len(s)==0:
           raise Exception
    except Exception:
        print("\nEmpty file cannot be decrypted")
        exit()

    print("Encryption by rc4 is processing.........")

    arc4 = ARC4(key)
    cipher = arc4.encrypt(s.encode('utf-8'))

    f2=open('f2\BinfileName13.bin','wb')
    f2.write(cipher)
    
    print("Encryption by rc4 done")
    return len(cipher)

def decauth():
    print("Process of detecting user who can decrypt the file is in progress...........\n")
    o=input("Enter the owner id: -")
    n=int(input("Enter the number of user who can decrypt tha file: -"))
    l=o+","
    for _ in range(0,n):
        s=input()
        l+=s+","

    print("Process of saving user who can decrypt the file is recorded successfully")
    return l[:len(l)-1]

def stegnoimg(k,iv,di,r,l):
    print("Stegnographic process is in progress..............")
    s=k+","+str(iv[0])+","+str(di[0])+","+str(iv[1])+","+str(di[1])+","+str(r)+","+l

    s=s.encode("utf-8")

    c=''
    for i in s:
        c+=format(i,'b')+' '

    secret = lsb.hide("sbushiv.jpg",c)
    secret.save("s1.png")
   
    print("Stegnographic process is completed")

# k=keygen()
# iv=aesenc()
# di=desenc()
# r=rc4enc()
# l=decauth()
# stegnoimg(k,iv,di,r,l)