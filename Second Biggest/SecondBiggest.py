# Finds the second biggest number in a list of inputs, very robust

print("Input N: ")
num = int(input())
record, record2 = float('-inf'), float('-inf')

for i in range(num):
    print("Input a number: ", end="")
    check = int(input())
    if check > record:
        record2 = record
        record = check
    else:
        if check > record2:
            record2 = check
print(record2)
