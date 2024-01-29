import arcade
from constants import *

class DevView(arcade.View):
    def on_mouse_press(self, x, y, button, mods):
        x_percent = int(x / SCREEN_WIDTH * 100)
        y_percent = int(y / SCREEN_HEIGHT * 100)
        print(f'{x}, {y} ({x_percent}%, {y_percent}%)')

class BaseView(arcade.View): # subclass DevView when testing
    def __init__(self):
        super().__init__()
        self.points = self.window.points
        self.gameover = 0
        self.scene = arcade.Scene()
        self.scene.add_sprite('wall', arcade.Sprite(
            'images/wall.png',
            scale = 1,
            center_x = SCREEN_WIDTH * .5,
            center_y = SCREEN_HEIGHT * .5)
        )
        self.scene.add_sprite('window', arcade.Sprite(
            'images/window.png',
            scale = .9,
            center_x = SCREEN_WIDTH * .75,
            center_y = SCREEN_HEIGHT * .58)
        )
        self.scene.add_sprite('window', arcade.Sprite(
            'images/window.png',
            scale = .9,
            center_x = SCREEN_WIDTH * .25,
            center_y = SCREEN_HEIGHT * .58)
        )
        self.scene.add_sprite('floor', arcade.Sprite(
            'images/floor.png',
            scale = 1,
            center_x = SCREEN_WIDTH * .5,
            center_y = SCREEN_HEIGHT * .5)
        )
        self.scene.add_sprite('meter', arcade.Sprite(
            'images/meter.png',
            scale = 1,
            center_x = SCREEN_WIDTH * .5,
            center_y = SCREEN_HEIGHT * .5)
        )
        self.scene.add_sprite_list_before('points', 'meter')
        self.point_sprites = self.scene.get_sprite_list('points')
        for i in range(POINT_GOAL):
            self.add_point_sprite(i)

    def add_point_sprite(self, index):
        POINT_SPRITE_WIDTH = 21
        POINT_SPRITE_HEIGHT = 5
        point_sprite = arcade.SpriteSolidColor(
            POINT_SPRITE_WIDTH,
            POINT_SPRITE_HEIGHT,
            arcade.color.BABY_BLUE
        )
        point_sprite.center_x = SCREEN_WIDTH * .9375 + 1
        point_sprite.center_y = SCREEN_HEIGHT * .12 + \
            POINT_SPRITE_HEIGHT * index + POINT_SPRITE_HEIGHT * 1.5
        if index > self.points:
            point_sprite.visible = False
        self.scene.add_sprite('points', point_sprite)
    def add_point(self):
        self.points += 1
        if self.points >= POINT_GOAL:
            return 1 # go to win view
        self.point_sprites[self.points - 1].visible = True
        return 0 # continue game
    def subtract_point(self):
        self.points -= 1
        if self.points <= 0:
            return -1 # go to lose view
        self.point_sprites[self.points + 1].visible = False # bugfix
        self.point_sprites[self.points].visible = False
        return 0 # continue game
    def on_draw(self):
        self.window.clear()
        self.scene.draw()
        # arcade.draw_text(self.points, PADDING, PADDING)
    def on_key_press(self, key, mods):
        if key == arcade.key.SPACE:
            self.window.next_view()
    def on_joybutton_press(self, controller, button):
        pass
    def on_joyaxis_motion(self, controller, axis, value):
        pass

class TestView1(BaseView):
    def on_show(self):
        arcade.set_background_color(arcade.color.CHERRY_BLOSSOM_PINK)

class TestView2(BaseView):
    def on_show(self):
        arcade.set_background_color(arcade.color.CHROME_YELLOW)

class TestView3(BaseView):
    def on_show(self):
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

class ControllerSupportWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, fullscreen=FULLSCREEN)
        self.points = STARTING_POINTS
        self.controller = arcade.get_joysticks()[0]
        self.controller.open()
        self.controller.set_handler('on_joybutton_press', self.on_joybutton_press)
        self.controller.set_handler('on_joyaxis_motion', self.on_joyaxis_motion)
        # self.controller.set_handler('on_dpad_motion', self.on_dpad_motion)
    def on_joybutton_press(self, controller, button):
        self.current_view.on_joybutton_press(controller, button)
    def on_joyaxis_motion(self, controller, axis, value):
        self.current_view.on_joyaxis_motion(controller, axis, value)
    # def on_dpad_motion(self, controller, dpl, dpr, dpu, dpd):
    #     self.current_view.on_dpad_motion(controller, dpl, dpr, dpu, dpd)
