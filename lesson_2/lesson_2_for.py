# for x in range(1,21):
#    print("x =",x, "x2=",x*x)

# students = ["Саша","Миша"]
# for i in range(0,len(students)):
#    print(students[i])

# word = "Test"
# for s in word:
#     print(s)
#
# for student in students:
#     print(student)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in nums:
    if n % 2 == 1:
        print(n)

# user_login = "adam"
# user_pass = "Esdkjfh3984"
#
# login = input("Login:")
# password = input("Password: ")
# if (login == user_login) and (password == user_pass):
#     print("Secret is open")
# else:
#     print("Locked")


crit1 = "red"
crit2 = "lock"
color = input("color:")
feature = input("feature: ")

if (color == crit1) or (feature == crit2):
    print("Buy it!")
else:
    print("Похожу, еще посмотрю")
