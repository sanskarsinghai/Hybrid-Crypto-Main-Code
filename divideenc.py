from stegano import lsb
import os

def stegnoimg():   
    print("Stegnographic process is in progress..............")
    clear_message = lsb.reveal("s1.png")
    s=clear_message.split(' ')
    c=''
    
    for i in range(0,len(s)-1):
        a=int(s[i],2)
        c+=chr(a)
    s=c.split(',')

    a=int(s[22])
    d=int(s[23])
    r=int(s[24])

    print("Stegnographic process is completed")

    return [a,d,r]

def DiviIn3(l):
    file_number = 0
    with open('f2\mergeenc.bin','rb') as f:
        while file_number<3:
            s=l[file_number]
            chunk = f.read(s)
            with open(('f2\BinfileName1' + str(file_number+1)+ '.bin'),'wb') as chunk_file:
                chunk_file.write(chunk)
            file_number += 1

    # os.remove("f2\mergeenc.bin")

l=stegnoimg()
DiviIn3(l)