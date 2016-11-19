# Find which number occurs most in a list of inputs

l = []
n = int(input())
for i in range(n):
    l.append(eval(input()))
rec = 0
recnum = 0

for i in range(n):
    count = 0
    for j in range(n):
        if l[i] == l[j]:
            count+=1
    if count > rec:
        rec = count
        recnum = l[i]

print(recnum)