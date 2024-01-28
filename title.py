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
    def on_draw(self):
        self.title.draw()
    def on_key_press(self, key, mods):
        if key == arcade.key.SPACE:
            self.window.next_view()
