#!/usr/bin/env python3
import arcade
import pymunk
from base import BaseView, ControllerSupportWindow
import random
from constants import *

class Juggler(arcade.Sprite):

    SPEED = 200

    def __init__(self):
        self.window = arcade.get_window()
        super().__init__('images/juggle.png', 2)
        self.center_x = PLAYERSTART_X
        self.center_y = PLAYERSTART_Y
    def on_update(self, dtime):
        driftless_joy_x = self.window.controller.x
        sign = driftless_joy_x/abs(driftless_joy_x)
        driftless_joy_x -= abs(driftless_joy_x) % 0.1 * sign
        # add player left/right bounds
        new_x = self.center_x + dtime * self.SPEED * driftless_joy_x
        if new_x > MAXJUGGLE_X or new_x < MINJUGGLE_X:
            return
        else:
            self.center_x = new_x

class Ball(arcade.SpriteCircle):

    RADIUS = 10

    def __init__(self, colour):
        super().__init__(self.RADIUS, colour)
        self.center_x = random.randrange(MINJUGGLE_X, MAXJUGGLE_X)
        self.center_y = SCREEN_HEIGHT + PADDING

        # pymunk stuff - added from https://api.arcade.academy/en/latest/examples/pymunk_pegboard.html
        mass = 0.5
        radius = 15
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        self.body = pymunk.Body(mass, inertia)
        self.body.position = self.center_x, self.center_y
        self.shape = pymunk.Circle(self.body, self.RADIUS, pymunk.Vec2d(0, 0))
        self.shape.friction = 0.3

class JuggleView(BaseView):

    ball_colours = [
        arcade.color.AERO_BLUE,
        arcade.color.AFRICAN_VIOLET,
        arcade.color.BRASS
    ]

    def __init__(self):
        super().__init__()
        self.king = arcade.Sprite('images/king.png', 2)
        self.king.center_x, self.king.center_y = KING_X, KING_Y
        self.scene.add_sprite('king', self.king)
        self.player = Juggler()
        self.scene.add_sprite('player', self.player)

        self.timer = 0
        self.first_ball_time = 1
        self.second_ball_time = 4
        self.third_ball_time = 7
        self.balls_dropped = 0
        random.shuffle(self.ball_colours)
        self.scene.add_sprite_list('balls')

        # pymunk physics stuff
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)

        # body = pymunk.Body(body_type=pymunk.Body.STATIC)

        # self.physics_engine = arcade.PymunkPhysicsEngine(gravity=(0,-1))
        # self.physics_engine.add_sprite_list(self.scene.get_sprite_list('balls'))
    def on_update(self, dtime):
        self.timer += dtime
        self.scene.on_update(dtime)

        if self.timer > MAXTIME:
            self.window.next_view()
            return

        # pymunk stuff
        self.space.step(1 / 60.)
        for ball in self.scene.get_sprite_list('balls'):
            ball.center_x = ball.shape.body.position.x
            ball.center_y = ball.shape.body.position.y

        # drop 3 balls
        if self.balls_dropped == 3:
            return
        elif self.balls_dropped == 2:
            if self.timer > self.third_ball_time:
                new_ball = Ball(self.ball_colours[2])
                self.space.add(new_ball.body, new_ball.shape)
                self.scene.add_sprite('balls', new_ball)
                self.balls_dropped += 1
        elif self.balls_dropped == 1:
            if self.timer > self.second_ball_time:
                new_ball = Ball(self.ball_colours[1])
                self.space.add(new_ball.body, new_ball.shape)
                self.scene.add_sprite('balls', new_ball)
                self.balls_dropped += 1
        else:
            if self.timer > self.first_ball_time:
                new_ball = Ball(self.ball_colours[0])
                self.space.add(new_ball.body, new_ball.shape)
                self.scene.add_sprite('balls', new_ball)
                self.balls_dropped += 1
    def on_draw(self):
        super().on_draw()

def main():
    win = ControllerSupportWindow()
    win.show_view(JuggleView())
    arcade.run()

if __name__ == '__main__':
    main()
