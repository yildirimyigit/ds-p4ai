from datetime import date


class Customer:
    def __init__(self, n, sn, ph, addr, rd, lsd):
        self.name = n
        self.surname = sn
        self.phone = ph
        self.address = addr
        self.reg_date = rd
        self.last_shopping_date = lsd

    def shop(self, shopping_list):
        summ = 0
        for item in shopping_list:
            summ += 0  # products[item]

        self.last_shopping_date = date.today()

        return summ

