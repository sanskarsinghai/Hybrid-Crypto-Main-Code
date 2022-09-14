import pyaes
from des import DesKey
from arc4 import ARC4
from stegano import lsb
import os

key=""
t=""
iv=""
di=""
lu=list()
o=""
use=int(input("Enter user id: -"))

userd={
    9691513053:['sanskar','singhai','12-09-2001',9691513053,'sanskar12singhai@gmail.com'],
    7247269405:['yajendra','prajapati','01-02-2000',7247269405,'yajendra@gmail.com'],
    8989154292:['sakshi','rohida','19-04-2002',8989154292,'sakshi@gmail.com'],
    9300479937:['vikram','abid','23-06-1999',9300479937,'vikram@gmail.com'],
}

def stegnoimg():
    global t,iv,di,lu,o,use
    print("Stegnographic process is in progress..............")
    
    clear_message = lsb.reveal("s1.png")
    s=clear_message.split(' ')
    c=''
    
    for i in range(0,len(s)-1):
       a=int(s[i],2)
       c+=chr(a)
    
    s=c.split(',')

    
    o=int(s[25])
    
    for i in s[25:]:
        #owner is also include in lu list
        lu.append(int(i))

    if use not in lu:
        print("You are no authorized to decypt this file")
        exit()

    iv=int(s[20])
    di=int(s[21])
    t=s[:20]
    print("Stegnographic process is completed")

def keygen():
    global t,key,o,userd

    print("Key generation is in progress...........")

    l=userd[o]
    s=""
    for i in range(1,6):
        if type(l[int(t[i])])!=str:
           s+=str(l[int(t[i])])
        else:
           s+=l[int(t[i])]

    d=''
    for i in range(6,len(t)):
        d+=s[int(t[i])]
    
    if t[0]=="l":
        d+=str(l[3])
    else:
        d=str(l[3])+d

    key=d.encode('utf-8')

    print("Key generated successfully")

def aesdec():
    global key,iv

    daes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))

    f=open('f2\BinfileName11.bin','rb')
    ciphertext=b''
    
    for i in f:
        ciphertext+=i

    f.close()

    try:
        if len(ciphertext)==0:
           raise Exception
    except Exception:
        print("\nEmpty file cannot be decrypted")
        exit()


    print("Decryption by aes is processing.........")

    try:
        decrypted = daes.decrypt(ciphertext)
        f3=open('f2\BinfileName11.bin','w')
        f3.write(decrypted.decode('utf-8'))
        f3.close()
    except UnicodeDecodeError as e:
        print("\nInvalid Key for decription")
        exit()

    print("Decryption by aes done")

def desdec():
    global key,di
    f=open('f2\BinfileName12.bin','rb')
    e=b''
    
    for i in f:
        e+=i

    f.close()

    try:
        if len(e)==0:
           raise Exception
    except Exception:
        print("\nEmpty file cannot be decrypted")
        exit()

    print("Decryption by des is processing.........")
    
    try:
       key0 = DesKey(key)
       d=key0.decrypt(e) 
       f2=open('f2\BinfileName12.bin','w')
       f2.write(d.decode('utf-8')[:len(d)-di])
       f2.close()
    except UnicodeDecodeError as e:
        print("\nInvalid Key for decription")
        exit()

    print("Decryption by des done")

def rc4dec():
    global key
    
    
    f=open('f2\BinfileName13.bin','rb')
    cipher=b''
    
    for i in f:
        cipher+=i

    f.close()
    
    try:
        if len(cipher)==0:
           raise Exception
    except Exception:
        print("\nEmpty file cannot be decrypted")
        exit()

    print("Decryption by rc4 is processing.........")

    try:
        arc4 = ARC4(key)
        d=arc4.decrypt(cipher)
        f2=open('f2\BinfileName13.bin','w')
        f2.write(d.decode('utf-8'))
        f2.close()
    except UnicodeDecodeError as e:
        print("\nInvalid Key for decription")
        exit()

    print("Decryption by rc4 done")

# stegnoimg()
# keygen()
# aesdec()
# desdec()
# rc4dec()
# os.remove("s1.png")