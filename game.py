#!/usr/bin/env python3
import arcade
import random
from base import ControllerSupportWindow
from title import TitleView
from massage import MassageView
from juggle import JuggleView
from dance import DanceView
from constants import *

class BaseWindow(ControllerSupportWindow):
    def __init__(self):
        super().__init__()
        self.views = [] # excludes title view
        # add "speed" variable
    def next_view(self):
        NextViewClass = random.choice([MassageView, JuggleView, DanceView])
        _next_view = NextViewClass()
        self.views.append(_next_view)
        self.show_view(_next_view)

def main():
    win = BaseWindow()
    win.show_view(TitleView())
    arcade.run()

if __name__ == '__main__':
    main()
