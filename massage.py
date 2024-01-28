#!/usr/bin/env python3
import arcade
from base import BaseView, ControllerSupportWindow
from constants import *
import random

class MassageView(BaseView):
    bell1 = arcade.load_sound('sounds/bell1.wav')
    bell2 = arcade.load_sound('sounds/bell2.wav')
    bell3 = arcade.load_sound('sounds/bell3.wav')
    def __init__(self):
        super().__init__()
        self.king = arcade.Sprite('images/king.png', 2)
        self.king.center_x = KING_X
        self.king.center_y = KING_Y
        self.player_standing = arcade.Sprite('images/jester.png', 2)
        self.player_standing.center_x = PLAYERSTART_X
        self.player_standing.center_y = PLAYERSTART_Y
        self.player = arcade.Sprite('images/run.png', 2.1)
        self.player.visible = False
        self.player.center_x = PLAYERSTART_X
        self.player.center_y = PLAYERSTART_Y - 10
        self.steps = 0
        self.is_next_step_left = True
        self.timer = 0
        self.is_won = False

    def on_joybutton_press(self, joy, button):
        if button == LBUTTON and self.is_next_step_left:
            self.player_standing.visible = False
            self.player.visible = True
            self.steps += 1
            self.player.angle = PLAYERANGLE * 4
            self.is_next_step_left = False
            bells = [self.bell1, self.bell2, self.bell3]
            arcade.play_sound(random.choice(bells))
        elif button == RBUTTON and not self.is_next_step_left:
            self.player_standing.visible = False
            self.player.visible = True
            self.steps += 1
            self.player.angle = PLAYERANGLE * 3
            self.is_next_step_left = True
            bells = [self.bell1, self.bell2, self.bell3]
            arcade.play_sound(random.choice(bells))
    def on_update(self, dtime):
        self.timer += dtime
        self.player.center_x = PLAYERSTART_X - 10 + self.steps * PLAYERANGLE
        if self.player.center_x > PLAYERFINISHX:
            self.is_won = True
            self.window.next_view()
        elif self.timer > MAXTIME:
            self.window.next_view()



    def on_draw(self):
        super().on_draw()
        self.player_standing.draw()
        self.player.draw()
        self.king.draw()

def main():
    win = ControllerSupportWindow()
    win.show_view(MassageView())
    arcade.run()

if __name__ == '__main__':
    main()
