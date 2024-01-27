#!/usr/bin/env python3
import arcade

SCREEN_WIDTH, SCREEN_HEIGHT, TITLE = 350, 350, 'jester'
FONTSIZE = 24
FONTNAME = 'monaco'

class BaseView(arcade.View):
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

def main():
    win = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    win.show_view(BaseView())
    arcade.run()

if __name__ == '__main__':
    main()
