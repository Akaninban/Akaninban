sentence1=input().split()
sentence2=input().split()
sentence3=input().split()
count1=len(sentence1)
count2=len(sentence2)
count3=len(sentence3)
print(count1)
print(count2)
print(count3)
if (count1>count2) and (count1>count3):
    print("sentence1 has maximum words")
elif(count2>count3):
    print("sentence2 has maximum words")
else:
    print("sentence3 has maximum words")
