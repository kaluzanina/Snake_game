from game import Game
import turtle
import keyboard

game = Game()
game.start_game()

while True:
    if keyboard.is_pressed('Enter'):
        turtle.clear()
        game = Game()
        game.start_game()
    elif keyboard.is_pressed('Escape'):
        turtle.bye()




