from smartphone import Smartphone

catalog = [
Smartphone("Sony",12, "+7 987 478 46 64"),
Smartphone("Nokia",8, "+7 974 847 98 09"),
Smartphone("IPhon",17, "+7 987 865 96 84"),
Smartphone("Honor",24, "+7 980 086 09 78"),
Smartphone("Huawei",15, "+7 944 456 76 23")
]

for phon in catalog:
    print (f"{phon.phone_brand} - {phon.phone_model}. {phon.number}")