L = [2,3,2,1,3,4,2,4,5]
length = len(L)
m = length

for i in range (0, length):
    count = 1
    for j in range (i+1, m):
        if L[i] == L[j]:
            count += 1
    print (L[i], 'is ', count, ' times repeated')




