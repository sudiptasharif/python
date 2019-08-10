class Rocket():
    """Rocket simulates a rocket ship for a game, or a physics simulation"""
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1

my_rocket = Rocket()
msg = "Rocket altitude: " + str(my_rocket.y)
print(msg)

my_rocket.move_up()
msg = "Rocket altitude: " + str(my_rocket.y)
print(msg)

my_rocket.move_up()
msg = "Rocket altitude: " + str(my_rocket.y)
print(msg)
