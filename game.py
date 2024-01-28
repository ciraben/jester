#!/usr/bin/env python3
import arcade
from base import BaseWindow
from title import TitleView

def main():
    win = BaseWindow()
    win.show_view(TitleView())
    arcade.run()

if __name__ == '__main__':
    main()
