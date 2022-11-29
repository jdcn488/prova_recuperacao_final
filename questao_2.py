
num1 = 0
num2 = 0

for x in range(1, 1001):

    if num1 % 2 != 0 and num1 % 3 == 0:

        num1 += num1

        print("A soma dos múltiplos de 3 a é: {}.".format(num1))



for y in range(1, 1001):

    if num2 % 2 != 0 and num2 % 5 == 0:

        num2 += num2

print("A soma dos múltiplos de 5 é: {}.".format(num2))
