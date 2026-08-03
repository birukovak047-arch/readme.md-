def month_to_season(m):
    if 1<= m <= 3:
        return "Зима"
    elif 4<= m <= 6:
        return "Весна"
    elif 7<= m <= 9:
        return "Лето"
    elif 10<= m <= 12:
        return "Осень"
    else:
        print("Неверное число месяца")

m = int(input("Введите название месяца цифрой: "))
print(f"Название сезона: {month_to_season(m)}")
