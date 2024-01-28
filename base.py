import arcade
import random
from constants import *

class DevView(arcade.View):
    def on_mouse_press(self, x, y, button, mods):
        x_percent = int(x / SCREEN_WIDTH * 100)
        y_percent = int(y / SCREEN_HEIGHT * 100)
        print(f'{x}, {y} ({x_percent}%, {y_percent}%)')

class BaseView(DevView):
    def on_draw(self):
        self.window.clear()
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
    def __init__(self, x, y, title):
        super().__init__(x, y, title)
        self.controller = arcade.get_joysticks()[0]
        self.controller.open()
        self.controller.set_handler('on_joybutton_press', self.on_joybutton_press)
        self.controller.set_handler('on_joyaxis_motion', self.on_joyaxis_motion)
    def on_joybutton_press(self, controller, button):
        self.current_view.on_joybutton_press(controller, button)
    def on_joyaxis_motion(self, controller, axis, value):
        self.current_view.on_joyaxis_motion(controller, axis, value)

class BaseWindow(ControllerSupportWindow):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        self.views = [] # excludes title view
        # add "speed" variable
    def next_view(self):
        NextViewClass = random.choice([TestView1, TestView2, TestView3])
        _next_view = NextViewClass()
        self.views.append(_next_view)
        self.show_view(_next_view)
