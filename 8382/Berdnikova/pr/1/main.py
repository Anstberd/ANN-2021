a = int(input())
sum = 0
if a > 0:
    A2 = str(bin(a))
    for i in range(len(A2)):
        if A2[i]=="1":
            sum += 1
print("Количество бит равных 1 в введенном числе:" ,sum)
