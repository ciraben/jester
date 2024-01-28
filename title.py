import arcade
from base import BaseView
from constants import *

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
        self.subtitle = arcade.Text(
            'press A to start',
            SCREEN_WIDTH * .5,
            SCREEN_HEIGHT * .3,
            color=arcade.color.SLATE_GRAY,
            font_name=FONTNAME,
            font_size=FONTSIZE * .5,
            anchor_x='center'
        )
    def on_draw(self):
        self.window.clear()
        self.title.draw()
        self.subtitle.draw()
    # def on_key_press(self, key, mods):
    #     if key == arcade.key.SPACE:
    #         self.window.next_view()
    def on_joybutton_press(self, joy, button):
        if button == ABUTTON:
            self.window.next_view()
