#!/usr/bin/env python3
import arcade
import random
from base import BaseView, ControllerSupportWindow
from constants import *

class DanceMoveIconSprite(arcade.SpriteCircle):

    ICONRADIUS = 20
    ICONSIZE = ICONRADIUS * 2

    def __init__(self, index, color):
        super().__init__(self.ICONRADIUS, color)
        self.center_x = self.ICONSIZE * (index + 1) * 1.5 + PADDING
        self.center_y = SCREEN_HEIGHT - self.ICONSIZE * .5 - PADDING
        self.visible = False
        self.has_button_been_pressed = False
        self.pressed_correctly = False

class Up(DanceMoveIconSprite):
    def __init__(self, index):
        super().__init__(index, arcade.color.AERO_BLUE)
        self.associated_button = XBUTTON
class Left(DanceMoveIconSprite):
    def __init__(self, index):
        super().__init__(index, arcade.color.ALABAMA_CRIMSON)
        self.associated_button = YBUTTON
class Down(DanceMoveIconSprite):
    def __init__(self, index):
        super().__init__(index, arcade.color.APPLE_GREEN)
        self.associated_button = BBUTTON
class Right(DanceMoveIconSprite):
    def __init__(self, index):
        super().__init__(index, arcade.color.ANTIQUE_BRONZE)
        self.associated_button = ABUTTON

class DanceView(BaseView):

    MOVES = (Up, Left, Down, Right)
    NUMMOVES = 8
    BACKLIGHTRADIUS = DanceMoveIconSprite.ICONRADIUS * 2

    def __init__(self):
        super().__init__()
        self.timer = 0
        self.is_won = False
        self.scene.add_sprite_list('backlights')
        self.backlights = self.scene.get_sprite_list('backlights')
        self.scene.add_sprite_list('move_icons')
        self.move_icons = self.scene.get_sprite_list('move_icons')
        # self.scene.add_sprite('player', Player())[]
        self.current_move_index = -1

        for i in range(self.NUMMOVES):
            next_move_icon = random.choice(self.MOVES)(i)
            self.scene.add_sprite('move_icons', next_move_icon)
            backlight = arcade.SpriteCircle(
                int(self.BACKLIGHTRADIUS),
                arcade.color.ANTIQUE_BRASS,
                soft=True
            )
            backlight.center_x = next_move_icon.center_x
            backlight.center_y = next_move_icon.center_y
            backlight.visible = False
            self.scene.add_sprite('backlights', backlight)

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_update(self, dtime):
        self.timer += dtime

        if self.timer >= self.NUMMOVES + 1:
            self.window.next_view()
            return

        if self.timer > 1:
            self.current_move_index = int(self.timer // 1) - 1
            self.move_icons[self.current_move_index].visible = True
            self.backlights[self.current_move_index].visible = True

    def on_draw(self):
        super().on_draw()

    def on_joybutton_press(self, joy, button):
        current_move = self.move_icons[self.current_move_index]
        if current_move.has_button_been_pressed:
            return
        current_move.has_button_been_pressed = True
        if button == current_move.associated_button:
            current_move.pressed_correctly = True
            self.backlights[self.current_move_index].color = \
                arcade.color.GO_GREEN
        else:
            self.backlights[self.current_move_index].color = \
                arcade.color.BOSTON_UNIVERSITY_RED

    # def on_dpad_motion(self, joy, dpl, dpr, dpu, dpd):
    #     if dpup:
    #         print('dpup')
    #     if dpdown:
    #         print('dpup')
    #     if dpleft:
    #         print('dpup')
    #     if dpright:
    #         print('dpup')

def main():
    win = ControllerSupportWindow()
    win.show_view(DanceView())
    arcade.run()

if __name__ == '__main__':
    main()
