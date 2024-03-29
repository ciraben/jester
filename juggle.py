#!/usr/bin/env python3
import arcade
import pymunk
from base import BaseView, ControllerSupportWindow
import random
from constants import *

class Juggler(arcade.Sprite):
    def __init__(self):
        self.window = arcade.get_window()
        super().__init__('images/juggle.png', 2 * SCREEN_WIDTH / 640)
        self.center_x = PLAYERSTART_X
        self.center_y = PLAYERSTART_Y

        # pymunk left hand
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.pymunk_lefty = pymunk.Segment(body, [0, 0], [0, 0], 10.0)
        self.set_lefty_posn()
        self.pymunk_lefty.collision_type = 2 # hand ID
        self.pymunk_lefty.friction = 1
        self.pymunk_lefty.elasticity = STATIC_ELASTICITY

        # pymunk right hand
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.pymunk_righty = pymunk.Segment(body, [0, 0], [0, 0], 10.0)
        self.set_righty_posn()
        self.pymunk_righty.collision_type = 2 # hand ID
        self.pymunk_righty.friction = 1
        self.pymunk_righty.elasticity = STATIC_ELASTICITY

    def set_lefty_posn(self):
        self.pymunk_lefty.unsafe_set_endpoints(
            [int(self.center_x - 60 * SCREEN_WIDTH/640), int(96 * SCREEN_WIDTH/640 + HANDANGLE)],
            [int(self.center_x - 40 * SCREEN_WIDTH/640), int(96 * SCREEN_WIDTH/640)]
        )
    def set_righty_posn(self):
        self.pymunk_righty.unsafe_set_endpoints(
            [int(self.center_x + 40 * SCREEN_WIDTH/640), int(96 * SCREEN_WIDTH/640)],
            [int(self.center_x + 60 * SCREEN_WIDTH/640), int(96 * SCREEN_WIDTH/640 + HANDANGLE)]
        )

    def on_update(self, dtime):
        driftless_joy_x = self.window.controller.x
        sign = driftless_joy_x/abs(driftless_joy_x)
        driftless_joy_x -= abs(driftless_joy_x) % 0.1 * sign
        # add player left/right bounds
        new_x = self.center_x + dtime * STRAFESPEED * driftless_joy_x
        if new_x < MAXJUGGLE_X and new_x > MINJUGGLE_X:
            self.center_x = new_x

        # move pymunk hands
        self.pymunk_lefty.unsafe_set_endpoints(
            [int(self.center_x - 60 * SCREEN_WIDTH/640), int(96 * SCREEN_WIDTH/640)],
            [int(self.center_x - 40 * SCREEN_WIDTH/640), int(96 * SCREEN_WIDTH/640)]
        )
        self.pymunk_righty.unsafe_set_endpoints(
            [int(self.center_x + 40 * SCREEN_WIDTH/640), int(96 * SCREEN_WIDTH/640)],
            [int(self.center_x + 60 * SCREEN_WIDTH/640), int(96 * SCREEN_WIDTH/640)]
        )

class Ball(arcade.SpriteCircle):

    RADIUS = int(10 * SCREEN_WIDTH/640)

    def __init__(self, colour):
        super().__init__(self.RADIUS, colour)
        self.center_x = random.randrange(MINBALL_X, MAXBALL_X)
        self.center_y = SCREEN_HEIGHT + PADDING

        # pymunk stuff - added from https://api.arcade.academy/en/latest/examples/pymunk_pegboard.html
        mass = 5
        radius = 15
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        self.body = pymunk.Body(mass, inertia)
        self.body.position = self.center_x, self.center_y
        self.pymunk_shape = pymunk.Circle(
            self.body,
            self.RADIUS,
            pymunk.Vec2d(0, 0))
        self.pymunk_shape.collision_type = 0 # ball ID
        self.pymunk_shape.elasticity = .9
        self.pymunk_shape.friction = .3

class JuggleView(BaseView):

    ball_colours = [
        arcade.color.ORANGE,
        arcade.color.BALL_BLUE,
        arcade.color.FANDANGO_PINK
    ]

    def __init__(self):
        super().__init__()
        self.king = arcade.Sprite('images/king.png', int(2 * SCREEN_WIDTH/640))
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
        self.space.gravity = (0, GRAVITY)

        # make pymunk floor
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(
            body,
            [-Ball.RADIUS, SCREEN_HEIGHT * .03],
            [SCREEN_WIDTH + Ball.RADIUS, SCREEN_HEIGHT * .03],
            10.0)
        shape.collision_type = 1 # floor ID
        shape.friction = 1
        shape.elasticity = STATIC_ELASTICITY
        self.space.add(shape, body)

        # add juggler hands to pymunk
        self.space.add(self.player.pymunk_righty, self.player.pymunk_righty.body)
        self.space.add(self.player.pymunk_lefty, self.player.pymunk_lefty.body)

        # pymunk - track collisions between balls and floor/hands
        # 0 = balls
        # 1 = floor
        # 2 = hands
        floor_handler = self.space.add_collision_handler(0, 1)
        def on_collide_floor(*args):
            # print('bam floor')
            self.gameover = self.subtract_point()
            return True
        floor_handler.begin = on_collide_floor
        hand_handler = self.space.add_collision_handler(0, 2)
        def on_collide_hand(*args):
            # print('bam hand')
            self.gameover = self.add_point()
            arcade.play_sound(random.choice(BELLS), volume=BELL_VOLUME)
            return True
        hand_handler.begin = on_collide_hand

    def on_update(self, dtime):
        if self.gameover:
            if self.gameover > 0:
                self.window.go_to_win_view()
            elif self.gameover < 0:
                self.window.go_to_lose_view()

        self.timer += dtime
        self.scene.on_update(dtime)

        if self.timer > MAXTIME:
            self.window.next_view()
            return

        # pymunk stuff
        self.space.step(1 / 60.)
        for ball in self.scene.get_sprite_list('balls'):
            ball.center_x = ball.pymunk_shape.body.position.x
            ball.center_y = ball.pymunk_shape.body.position.y

        # drop 3 balls
        if self.balls_dropped == 3:
            return
        elif self.balls_dropped == 2:
            if self.timer > self.third_ball_time:
                self.generate_ball(self.ball_colours[2])
        elif self.balls_dropped == 1:
            if self.timer > self.second_ball_time:
                self.generate_ball(self.ball_colours[1])
        else:
            if self.timer > self.first_ball_time:
                self.generate_ball(self.ball_colours[0])
    def on_draw(self):
        super().on_draw()
    def generate_ball(self, colour):
        new_ball = Ball(colour)
        self.space.add(new_ball.body, new_ball.pymunk_shape)
        self.scene.add_sprite('balls', new_ball)
        self.balls_dropped += 1

def main():
    win = ControllerSupportWindow()
    win.show_view(JuggleView())
    arcade.run()

if __name__ == '__main__':
    main()
