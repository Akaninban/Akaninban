def maxArea (A, Len):
    area=0
    for i in range (Len):
        for j in range (i+1, Len):
            area=max(area, min (A[j],A[i])*(-i))
    return area
a=[1,5,4,3]
b-[3,1,2,4,5]
c-[1,1]
d-[1,8,6,2,5,4,8,3,7] 
lenl-len (a)
print (maxArea (a,len1))
only2=only (b)
print (maxArea (b, len2))
only3=only (c)
print (maxArea (c, len3))
len4=len (d)
print (maxArea (d. len4))
