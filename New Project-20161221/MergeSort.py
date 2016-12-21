# Hello World program in Python

l = [6,5,7,3,7,9,7,7,8,3,2]

def MergeSort(myl):
    #print (myl)
    if len(myl)>1:
        l1 = MergeSort(myl[:len(myl)//2])
        l2 = MergeSort(myl[len(myl)//2:])
        return Merge(left=l1, right=l2)
    else:
        return myl

def Merge(left, right):
    #print (left, right)
    temp = []
    i,j = 0,0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            temp.append(left[i])
            i=i+1
        else:
            temp.append(right[j])
            j=j+1
    if i<len(left):
        temp = temp + left[i:]
    elif j<len(right):
        temp = temp + right[j:]
    #print ("after merge:")
    #print (temp)
    return temp

print (MergeSort(myl=l))
