import arcade

# controller button keys
controller = arcade.get_joysticks()[0]
if controller.device.name == 'Faceoff Deluxe+ Audio Wired Controller for Nintendo Switch':
    ABUTTON = 2
    BBUTTON = 1
    XBUTTON = 3
    YBUTTON = 0
    # print('Faceoff Deluxe+')
elif controller.device.name == 'Pro Controller':
    ABUTTON = 1
    BBUTTON = 0
    XBUTTON = 3
    YBUTTON = 2
    # print('Pro Controller')
LBUTTON = 4
RBUTTON = 5

# general
SCREEN_WIDTH, SCREEN_HEIGHT, TITLE = 640, 360, 'jester'
FONTSIZE = 24
FONTNAME = 'monaco'

PLAYERSTART_X, PLAYERSTART_Y = 100, 100
KING_X, KING_Y = SCREEN_WIDTH * .75, 100
MAXTIME = 10
STARTING_POINTS = 10
POINT_GOAL = 50

BELLS = (
    arcade.load_sound('sounds/bell1.wav'),
    arcade.load_sound('sounds/bell2.wav'),
    arcade.load_sound('sounds/bell3.wav')
)

BACKGROUNDMUSIC = arcade.load_sound('sounds/background.wav')

# massage.py
PLAYERANGLE = 10 # depend this on game progress later
SPRITEWIDTH, SPRITEHEIGHT = 40, 90
PADDING = 20
PLAYERFINISHX = SCREEN_WIDTH * .7
TOTALSTEPSREQUIRED = 36

# juggle.py
MINJUGGLE_X = SCREEN_WIDTH * .1
MAXJUGGLE_X = SCREEN_WIDTH * .6
MINBALL_X = SCREEN_WIDTH * .25
MAXBALL_X = SCREEN_WIDTH * .45
HANDANGLE = 5
STATIC_ELASTICITY = .9
GRAVITY = -900
STRAFESPEED = 200
