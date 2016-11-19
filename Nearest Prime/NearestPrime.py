# Finds the nearest prime to the inputted number

print("Input a number: ", end="")
num = int(input())
i = 2
ans = 0
rec = num
while i < num * 2:
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime:
        if abs(num - i) < rec:
            rec = abs(num-i)
            ans = i
    i += 1
print("The nearest prime to " + str(num) + " is: " + str(ans))
