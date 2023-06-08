class Smartphone:

    def __init__(self):
        self.display = 'oled'
        self.battery = 2500

    def detail(self):
        print("display quality: ", self.display)
        print("MH of battery: ", self.battery)


s1 = Smartphone()
s1.detail()
