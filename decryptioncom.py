import divideenc as de
import desc
import merge as m
import os

print("Decryption process started: -")
print()

l=de.stegnoimg()
de.DiviIn3(l)

os.remove("f2\mergeenc.bin")

desc.stegnoimg()

os.remove("s1.png")

desc.keygen()
desc.aesdec()
desc.desdec()
desc.rc4dec()

m.MergeIn3()

print("Decryption process completed")