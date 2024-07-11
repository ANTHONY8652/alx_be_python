class iPhone:

    def __init__(self, model, year, color, version_num, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.version_num = version_num
        self.for_sale = for_sale

    def turn_on(self):
        print(f"This {self.year} {self.color} {self.model} is turned on")

    def turn_off(self):
        print(f"This {self.year}{self.color} {self.model} is turned off")

    def unlock_phone(self):
        print(f"This {self.year} {self.color} {self.model} is unlocked")

    def reboot(self):
        print(f"This {self.year} {self.color} {self.model} is going to reboot")

    def restart(self):
        print(f"This {self.year} {self.color} {self.model} is going to restart")



