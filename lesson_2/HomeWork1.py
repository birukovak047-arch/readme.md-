# 1) Работа со списками

# employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
#
# print(f"{employee_list [1]}, {employee_list [-2]}")
#
# #2) Деление на три

# def dev_by_three (int):
#     if int % 3 == 0:
#         return "Да"
#     else:
#         return "Нет"
# a = int(input("Введите число: "))
# resalt = dev_by_three(a)
# print(f"Делится ли на три {a}? - {resalt}.")
#
# # альтернативное решение
# def dev_by_three(number):
#     return "Да" if number % 3 == 0 else "Нет"
#
# num = int(input("Введите число: "))
# result = dev_by_three(num)
# print(f"Делится ли на три {num}? - {result}")

# 3) Округление

# def min_boxes(things):
#     return math.ceil(things / 5)
# i = int(input("Введите число: "))
# min_boxes(i)
# print(f"Необходимо коробок: {min_boxes(i)}" )

# 4) Два делителя
# n = int(input("Введите число"))
#
# def check_divisibility(n):
#     for i in range (1,n+1):
#         if i % 4 == 0:
#             print(f"{i} - Делится и на 2, и на 4")
#         elif i % 2 == 0:
#             print(f"{i} - Делится на 2, но не на 4")
#         else:
#             print(i)
#
# check_divisibility(n)

# 5) Квартал
#
# def quarter_of_year(i):
#     if 1 <= i <= 3:
#         return "I квартал"
#     elif 4 <= i <= 6:
#         return "II квартал"
#     elif 7 <= i <= 9:
#         return "III квартал"
#     else:
#         return "Неверный номер месяца"
# i = int(input("Введите числовое название месяца"))
# print(quarter_of_year(i))

# 6) Фильтрация списка

# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
#
# result = [x for x in lst if x > 15 and x % 3 ==0]
# print(result)

# # 7) Range
# lists = [25, 20, 15, 10, 5]
# for x in range (25,0, -5):
#     print(x, end=' ')

# 8) Поменять значения местами

# var_1 = 50
# var_2 = 5
#
# temp = var_1
# var_1 = var_2
# var_2 = temp
#
# print("var_1 =", var_1)
# print("var_2 =", var_2)

