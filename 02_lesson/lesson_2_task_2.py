def is_year_leap (year):
    if year % 4 == 0:
        return  "True"
    else:
        return "False"
a = int(input("Введите год числом"))
print(f"год {a}: {is_year_leap(a)}")