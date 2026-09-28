class Engine:
    def start(self):
        print("Engine is starting.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Compostion\

c1 = Car()
c1.engine.start()