#1.vektör=A
A=[]
ax=int(input("the first power of vector A"))
ay=int(input("the second power of vector A"))
az=int(input("the third power of vector A"))
A.append(ax)
A.append(ay)
A.append(az)
print(A)
#2.vektör=B
B=[]
bx=int(input("the first power of vector B"))
by=int(input("the second power of vector B"))
bz=int(input("the third power of vector B"))
B.append(bx)
B.append(by)
B.append(bz)
print(B)
abx=ay*bz-az*by
aby=ax*bz-az*bx
abz=ax*by-ay*bx
AcarpiB=[]
AcarpiB.append(abx)
AcarpiB.append(aby)
AcarpiB.append(abz)
print("Vector A product Vektor B=",AcarpiB)
