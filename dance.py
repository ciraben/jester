#!/usr/bin/env python3
import arcade
import random
from base import BaseView, ControllerSupportWindow
from constants import *

class DanceMoveIconSprite(arcade.Sprite):

    ICONRADIUS = 20
    ICONSIZE = ICONRADIUS * 2

    def __init__(self, index, image):
        super().__init__(image, .5)
        self.center_x = self.ICONSIZE * (index + 1) * 1.5 + PADDING
        self.center_y = SCREEN_HEIGHT - self.ICONSIZE * .5 - PADDING
        self.visible = False
        self.has_button_been_pressed = False
        self.pressed_correctly = False
        self.point_subtracted = False

class Up(DanceMoveIconSprite):
    def __init__(self, index):
        super().__init__(index, 'images/x-button.png')
        self.associated_button = XBUTTON
class Left(DanceMoveIconSprite):
    def __init__(self, index):
        super().__init__(index, 'images/y-button.png')
        self.associated_button = YBUTTON
class Down(DanceMoveIconSprite):
    def __init__(self, index):
        super().__init__(index, 'images/b-button.png')
        self.associated_button = BBUTTON
class Right(DanceMoveIconSprite):
    def __init__(self, index):
        super().__init__(index, 'images/a-button.png')
        self.associated_button = ABUTTON

class Jester(arcade.Sprite):
    def __init__(self, image='images/jester.png', visible=False):
        super().__init__(image, scale=2)
        self.center_x = PLAYERSTART_X
        self.center_y = PLAYERSTART_Y
        self.visible = visible
class UpJester(Jester):
    def __init__(self):
        super().__init__('images/dance-up.png')
class LeftJester(Jester):
    def __init__(self):
        super().__init__('images/dance-left.png')
class DownJester(Jester):
    def __init__(self):
        super().__init__('images/dance-down.png')
class RightJester(Jester):
    def __init__(self):
        super().__init__('images/dance-right.png')

class DanceView(BaseView):

    MOVES = (Up, Left, Down, Right)
    NUMMOVES = 8
    BACKLIGHTRADIUS = DanceMoveIconSprite.ICONRADIUS * 2
    error = arcade.load_sound('sounds/error.wav')

    def __init__(self):
        super().__init__()
        self.timer = 0
        self.is_won = False
        self.king = arcade.Sprite('images/king.png', 2)
        self.king.center_x = KING_X
        self.king.center_y = KING_Y
        self.scene.add_sprite('king', self.king)

        self.jesters = {
            'standing': Jester(visible=True),
            XBUTTON: UpJester(),
            YBUTTON: LeftJester(),
            BBUTTON: DownJester(),
            ABUTTON: RightJester()
        }
        self.current_jester = self.jesters['standing']
        for jester in self.jesters.items():
            self.scene.add_sprite('player', jester[1])

        self.scene.add_sprite_list('backlights')
        self.backlights = self.scene.get_sprite_list('backlights')
        self.scene.add_sprite_list('move_icons')
        self.move_icons = self.scene.get_sprite_list('move_icons')
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

    def on_update(self, dtime):
        self.timer += dtime

        if self.timer >= self.NUMMOVES + 1:
            self.window.next_view()
            return

        if self.timer > 1:
            self.current_move_index = int(self.timer // 1) - 1
            self.move_icons[self.current_move_index].visible = True
            self.backlights[self.current_move_index].visible = True
        if self.timer > 2:
            self.subtract_point_check()

    def subtract_point_check(self):
        last_move = self.move_icons[self.current_move_index - 1]
        if last_move.has_button_been_pressed or last_move.point_subtracted:
            return
        self.gameover = self.subtract_point()
        last_move.point_subtracted = True

    def on_draw(self):
        super().on_draw()

    def on_joybutton_press(self, joy, button):
        current_move = self.move_icons[self.current_move_index]
        if current_move.has_button_been_pressed:
            return
        current_move.has_button_been_pressed = True

        # update which jester is shown
        if button in (XBUTTON, YBUTTON, ABUTTON, BBUTTON):
            self.current_jester.visible = False
            self.current_jester = self.jesters[button]
            self.current_jester.visible = True

        if button == current_move.associated_button:
            current_move.pressed_correctly = True
            self.gameover = self.add_point()
            self.backlights[self.current_move_index].color = \
                arcade.color.GO_GREEN
            arcade.play_sound(random.choice(BELLS))
        else:
            self.gameover = self.subtract_point()
            self.gameover = self.subtract_point()
            self.backlights[self.current_move_index].color = \
                arcade.color.BOSTON_UNIVERSITY_RED
            arcade.play_sound(self.error)

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
