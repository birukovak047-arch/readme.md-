from address import Address
from mailing import Mailing

to_address = Address(123, "Москва", "Солнечная", 6, 32)
from_address = Address(177, "Питер", "Главная", 34, 345)

mailing = Mailing("to_address", "from_address","555", "56444444")

print(mailing)