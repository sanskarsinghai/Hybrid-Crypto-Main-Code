import os

def MergeIn1():
    f3=open('f2\BinfileName11.bin','rb')
    f5=open('f2\BinfileName12.bin','rb')
    f6=open('f2\BinfileName13.bin','rb')

    s=b''
    for i in f3:
        s+=i

    for i in f5:
        s+=i

    for i in f6:
        s+=i

    f4=open('f2\mergeenc.bin','wb')
    f4.write(s)

    f4.close()
    f3.close()
    f5.close()
    f6.close()

    os.remove("f2\BinfileName11.bin")
    os.remove("f2\BinfileName12.bin")
    os.remove("f2\BinfileName13.bin")