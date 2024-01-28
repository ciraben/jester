#!/usr/bin/env python3
import arcade
from base import BaseView, ControllerSupportWindow
import random
from constants import *

class Juggler(arcade.Sprite):

    SPEED = 200

    def __init__(self):
        self.window = arcade.get_window()
        super().__init__('images/juggle.png', 2)
        # self.center_x = SPRITEWIDTH * .5 + PADDING
        # self.center_y = SPRITEHEIGHT * .5 + PADDING
        self.center_x = PLAYERSTART_X
        self.center_y = PLAYERSTART_Y
    def on_update(self, dtime):
        driftless_joy_x = self.window.controller.x
        sign = driftless_joy_x/abs(driftless_joy_x)
        driftless_joy_x -= abs(driftless_joy_x) % 0.1 * sign
        self.center_x += dtime * self.SPEED * driftless_joy_x

class Ball(arcade.SpriteCircle):
    def __init__(self):
        super().__init__(10, arcade.color.AMARANTH_PURPLE)
        self.center_x = random.randrange(MINBALLX, MAXBALLX)
        # self.center_y = SCREEN_HEIGHT + PADDING
        self.center_y = 200


class JuggleView(BaseView):
    def __init__(self):
        super().__init__()
        self.king = arcade.Sprite('images/king.png', 2)
        self.king.center_x = SCREEN_WIDTH * 0.8
        self.king.center_y = 100
        self.scene.add_sprite('king', self.king)
        self.player = Juggler()
        self.scene.add_sprite('player', self.player)
        self.scene.add_sprite_list('balls')
        # self.physics_engine = arcade.PymunkPhysicsEngine(gravity=(0,-1))
        # self.physics_engine.add_sprite_list(self.scene.get_sprite_list('balls'))
    def on_update(self, dtime):
        self.scene.on_update(dtime)
        if random.randrange(100) < 5:
            self.scene.add_sprite('balls', Ball())
    def on_draw(self):
        super().on_draw()

def main():
    win = ControllerSupportWindow()
    win.show_view(JuggleView())
    arcade.run()

if __name__ == '__main__':
    main()
