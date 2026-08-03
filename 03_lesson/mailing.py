from address import Address

class Mailing:
    def __init__(self, to_address:{Address}, from_address:{Address},cost:{int}, track:{string}):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        mailing_str = ", ".join([str(mailing) for mailing in self.mailing])
        return f"Отправление {track} из {to} в {from}. Стоимость {cost} рублей."

# {mailing_str}