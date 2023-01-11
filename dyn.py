import random 

l=['A','C','G','T']
str1=""
str2=""
for i in range(16):
    a=random.randint(0,3)
    str1+=l[a]
for i in range(16):
    a=random.randint(0,3)
    str2+=l[a]
    
str1='-'+str1
str2='-'+str2

mat=[[0 for col in range(16)] for row in range(16)]
i=0
j=0
def assing(mat,i,j):
    if(i!=15):
        if(str1[i+1]==str2[j+1]):
            mat[i+1][j+1]=mat[i][j]+5
            i+=1
            assing(mat,i,j,)
        elif(str1[i+1]!=str2[j+1]):
            a=max(mat[i+1][j],mat[i][j+1],mat[i][j])
            i+=1
            mat[i+1][j+1]=a-4
            assing(mat,i,j)
    elif(i==15):
        i=0
        j+=1
        assing(mat,i,j)
assing(mat,i,j)
for i in range(16):
    for j in range(16):
        print(mat[i][j])

    
    