#!/usr/bin/env python3
import arcade
from game import BaseWindow, BaseView

class MassageView(BaseView):
    def __init__(self):



def main():
    win = BaseWindow()
    win.show_view(MassageView())
    arcade.run()

if __name__ == '__main__':
    main()
