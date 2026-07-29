rate_as_string = input("Оцените работу оператора от 1 до 5")
rate = int(rate_as_string)

if(rate < 1):
    rate = 1
else(rate > 5):
    rate = 5

print(rate)

if rate == 1:
    feedback = input("расскажите, что нам поправить?")
elif rate ==2:
        feedback = input("расскажите, что вас смутило?")
elif rate == 3:
        feedback = input("расскажите, как дела?")
elif rate == 4:
        feedback = input("расскажите, что было хорошо?")
else:
        feedback = input("За что нам похвалить оператора?")
print(feedback)