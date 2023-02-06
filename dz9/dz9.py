#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите положительное число N: '))
listValue =[]
for i in range(n*2 +1):
    listValue.append(-n+i)
print(listValue)

multiply =1
with open("file.txt", 'r') as data_file:
    for line in data_file:
        try:
            index=int(line)
            multiply *= listValue[index]
        except:
            pass
print(f'Произведение существующих знаений ={multiply3}')