s=input("Enter the sentence:")
str=s
n=len(str)
res=0
j=-1
k=0
parts=str.split(' ')
n=len(parts)
for i in range(0,n):
    w=len(parts[i])

    if ((res!=max(w,res)) or ( k==0 and i==n-1)):
        res = max(w, res)
        k=k+1
        j=i;


print(j,i,n)

print("The longest word is (",parts[j],") And its length is (",res,")")
