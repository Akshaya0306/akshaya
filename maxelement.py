a=[1,3,4,2,8]
first=second=a[0]
for i in range(len(a)):
    if(a[i]>first):
        second=first
        first=a[i]
    elif(a[i]>second and a[i]>first):
        second
print(second)
    
