sentence1=input("enter sentence 1:")
sentence2=input("enter sentence 2:")
a=sentence1.split()
b=sentence2.split()
a=set(a)
b=set(b)
print(a.symmetric_difference(b))
