
n = int(input())   # Вводим число от 3 до 20
array = []

for i in range(1, 21):
    for j in range(1, 21):
        if n % (i + j) == 0 and i < j and (i + j) != 0:
            array.append(str(i))
            array.append(str(j))
print(''.join(array))
