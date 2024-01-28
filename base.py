import arcade
from constants import *

class DevView(arcade.View):
    def on_mouse_press(self, x, y, button, mods):
        x_percent = int(x / SCREEN_WIDTH * 100)
        y_percent = int(y / SCREEN_HEIGHT * 100)
        print(f'{x}, {y} ({x_percent}%, {y_percent}%)')

class BaseView(DevView):
    def __init__(self):
        super().__init__()
        self.points = self.window.points
        self.scene = arcade.Scene()
        self.scene.add_sprite('wall', arcade.Sprite(
            'images/wall.png',
            scale = 1,
            center_x = SCREEN_WIDTH * .5,
            center_y = SCREEN_HEIGHT * .5)
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

    def on_draw(self):
        self.window.clear()
        self.scene.draw()
        arcade.draw_text(self.points, PADDING, PADDING)
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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
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
