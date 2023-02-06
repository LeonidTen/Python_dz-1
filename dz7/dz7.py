#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number= int(input('введите число n: '))
count = 1
sum =1
while count <= number:
    for i in range(1, number +1):
        sum =sum*i
        print(sum)
        count+=1
