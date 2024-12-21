import turtle
import keyboard
from snake import Snake
from turtle import Screen
from food import Food
import time
from scoreboard import Score_board

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.clear()
        self.screen.setup(width=600, height=600)
        self.screen.cv._rootwindow.resizable(False, False)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Score_board()

        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")


    def start_game(self):
        game_is_on = True

        while game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            if self.snake.head.distance(self.food) < 15:
                self.food.new_food_location()
                self.scoreboard.add_points()
                self.snake.extend()

            if self.snake.head.xcor() > 280 or self.snake.head.ycor() > 280 or self.snake.head.xcor() < -280 or self.snake.head.ycor() < -280:
                game_is_on = False
                self.scoreboard.game_over()

            for block in self.snake.blocks[1:]:
                if self.snake.head.distance(block) < 15:
                    game_is_on = False
                    self.scoreboard.game_over()


