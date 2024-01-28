#!/usr/bin/env python3
import arcade
from game import BaseWindow, BaseView

LBUTTON = 4
RBUTTON = 5
PLAYERANGLE = 10 # depend this on game progress later
SPRITEWIDTH = 40
SPRITEHEIGHT = 90
PADDING = 20

class MassageView(BaseView):
    PLAYERSTARTX = SPRITEWIDTH * .5 + PADDING
    PLAYERSTARTY = SPRITEHEIGHT * .5 + PADDING
    def __init__(self):
        super().__init__()
        self.player = arcade.SpriteSolidColor(
            SPRITEWIDTH, SPRITEHEIGHT, arcade.color.AFRICAN_VIOLET)
        self.player.center_x = self.PLAYERSTARTX
        self.player.center_y = self.PLAYERSTARTY
        self.steps = 0
        self.is_next_step_left = True
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
        self.player.center_x = self.PLAYERSTARTX + self.steps * PLAYERANGLE
    def on_draw(self):
        super().on_draw()
        self.player.draw()

def main():
    win = BaseWindow()
    win.show_view(MassageView())
    arcade.run()

if __name__ == '__main__':
    main()
