#Урок 1. Ввод-Вывод, операторы ветвления

# Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

#a = int(input("Введите трехзначное число: "))
#sum = 0
#while(a !=0):
#   sum = sum + a % 10
#   a = a // 10
#print("Сумма ", sum)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#    60 -> 10  40  10

#s = int(input("Введите s: "))
#k = s * 2 // 3
#p = c = (s-k) // 2
#print("{} -> {} {} {}".format(s,p,k,c))

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали 
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых 
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

#tiket = input("Введите номер билета: ")
#s1 = list(map(int, tiket))
#a = s1[0] + s1[1] + s1[2]
#b = s1[3] + s1[4] + s1[5]
#if a == b:
#    print (tiket, "-> yes")
#else:
#    print (tiket, "-> no")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если 
# разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

#n = int(input("Введите n: "))
#m = int(input("Введите m: "))
#k = int(input("Введите k: "))
#if k % n == 0 or k % m == 0:
#     print (n, m, k, "-> yes")
#else:
#     print (n, m, k, "-> no")