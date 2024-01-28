#!/usr/bin/env python3
import arcade
from base import BaseView, ControllerSupportWindow
from constants import *

class MassageView(BaseView):
    PLAYERSTARTX = SPRITEWIDTH * .5 + PADDING
    PLAYERSTARTY = SPRITEHEIGHT * .5 + PADDING
    def __init__(self):
        super().__init__()
        self.player = arcade.Sprite('images/jester.png', 2)
        self.king = arcade.Sprite('images/king.png', 2)
        self.king.center_x = PLAYERFINISHX
        self.king.center_y = 100
        self.player.center_x = self.PLAYERSTARTX
        self.player.center_y = self.PLAYERSTARTY
        self.steps = 0
        self.is_next_step_left = True
        self.timer = 0
        self.is_won = False
    def on_joybutton_press(self, joy, button):
        # print(button)
        if button == LBUTTON and self.is_next_step_left:
            self.steps += 1
            self.player.angle = PLAYERANGLE
            self.is_next_step_left = False
        elif button == RBUTTON and not self.is_next_step_left:
            self.steps += 1
            self.player.angle = -PLAYERANGLE
            self.is_next_step_left = True
    def on_update(self, dtime):
        self.timer += dtime
        self.player.center_x = self.PLAYERSTARTX + self.steps * PLAYERANGLE
        if self.player.center_x > PLAYERFINISHX:
            self.is_won = True
            self.window.next_view()
        elif self.timer > MAXTIME:
            self.window.next_view()



    def on_draw(self):
        super().on_draw()
        self.player.draw()
        self.king.draw()

def main():
    win = ControllerSupportWindow()
    win.show_view(MassageView())
    arcade.run()

if __name__ == '__main__':
    main()
