class Product:

    def __init__(self, nm, brnd, amnt, best_bef, ppu):
        self.name = nm
        self.brand = brnd
        self.amount = amnt
        self.bb = best_bef
        self.price_per_unit = ppu

    def add_inventory(self, new_amount):
        self.amount += new_amount

