
def capitalization(x):
    a=x.split(" ")
    
    for i in range(0,len(a)):
        a[i]=a[i][0].upper() + a[i][1:]
    return " ".join(a)

print(capitalization("abcd efgh ijklm"))

