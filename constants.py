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
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 360
# SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
TITLE = 'jester'
FONTSIZE = 24
FONTNAME = 'monaco'
FULLSCREEN=False

# PLAYERSTART_X, PLAYERSTART_Y = 100, 100
PLAYERSTART_X, PLAYERSTART_Y = SCREEN_WIDTH * .15625, SCREEN_HEIGHT * .278
KING_X, KING_Y = SCREEN_WIDTH * .75, PLAYERSTART_Y
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
# SPRITEWIDTH, SPRITEHEIGHT = 40, 90
SPRITEWIDTH, SPRITEHEIGHT = SCREEN_WIDTH * .0625, SCREEN_HEIGHT * .25
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
# STRAFESPEED = 200
STRAFESPEED = SCREEN_WIDTH * .3125
