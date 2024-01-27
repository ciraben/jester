#!/usr/bin/env python3
import arcade
import random


SCREEN_WIDTH, SCREEN_HEIGHT, TITLE = 640, 360, 'jester'
FONTSIZE = 24
FONTNAME = 'monaco'

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

class TitleView(BaseView):
    def __init__(self):
        super().__init__()
        self.title = arcade.Text(
            TITLE,
            SCREEN_WIDTH * .5,
            SCREEN_HEIGHT * .5,
            font_name=FONTNAME,
            font_size=FONTSIZE,
            anchor_x='center'
        )
    def on_draw(self):
        self.title.draw()
    def on_key_press(self, key, mods):
        if key == arcade.key.SPACE:
            self.window.next_view()

class TestView1(BaseView):
    def on_show(self):
        arcade.set_background_color(arcade.color.CHERRY_BLOSSOM_PINK)

class TestView2(BaseView):
    def on_show(self):
        arcade.set_background_color(arcade.color.CHROME_YELLOW)

class TestView3(BaseView):
    def on_show(self):
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

class BaseWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        self.views = [] # excludes title
        # add "speed" variable
    def next_view(self):
        NextViewClass = random.choice([TestView1, TestView2, TestView3])
        _next_view = NextViewClass()
        self.views.append(_next_view)
        print(len(self.views))
        self.show_view(_next_view)


def main():
    win = BaseWindow()
    win.show_view(TitleView())
    arcade.run()

if __name__ == '__main__':
    main()
