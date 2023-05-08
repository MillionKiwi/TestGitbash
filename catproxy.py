class Cat:
    def speak(self):
        print("meow")

class CatProxy:
    def __init__(self, cat:Cat):
        self.cat = cat
    def speak(self):
        print("before speak")
        self.cat.speak()
        print("after speak")

kitty = Cat()
kitty.speak()
kitty_proxy = CatProxy(kitty)
kitty_proxy.speak()