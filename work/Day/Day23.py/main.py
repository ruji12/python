import time
from turtle import Screen
from player import Player
from car_manager import Cars
from scoreboard import Scoreboard






screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()
car_manager = Cars()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_car()
    car_manager.move_car()

    #detect collision with the car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False

    if player.go_to_finish_line():
        player.start_new()
        car_manager.level_up()
        scoreboard.update_level()


        



screen.exitonclick()