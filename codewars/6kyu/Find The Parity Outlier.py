def find_outlier(integers):
    evenorodd=0 
    for n in range(len(integers)):
        if integers[n]%2==0:
            evenorodd+=1
        else : evenorodd-=1
    if evenorodd>0 :
        for n in range(len(integers)):
            if integers[n]%2!=0:
                number=integers[n]
    elif evenorodd<0:
        for n in range(len(integers)):
            if integers[n]%2==0:
                number=integers[n]
    return number
