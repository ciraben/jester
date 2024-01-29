# jester

There are 3 mini games that will cycle through at random:

### Running Mini Game:
  - Your king demands a foot rub!
  - Alternate L/R buttons to run your way across the room
  - Gain points based on how fast you get to him
### Juggling Mini Game:
  - Balls will fall from the sky and it's your job to bounce them
  - Move the left joystick to put your hands under the balls
  - Gain a point every time you bounce a ball with your hand
  - Lose a point every time a ball hits the floor
### Dancing Mini Game:
  - Buttons will show up at the top of the screen
  - Push the button displayed to earn a point
  - Mess up and lose a point instead
  - Groove out

A total of 50 points is needed to win. Drop to zero and your king
will be very unimpressed.

## installation instructions

1. Python 3.9 is best for running `jester`. Python 3.12+ may not work.

2. `jester` requires `arcade` to run. Install it with: `$ pip install arcade`.

3. Connect your game controller.

4. `cd` into your unzipped `jester` folder and run `$ python3.9 game.py` to play!

### dev setup

```bash
python3.9 -m venv env
source env/bin/activate
pip install arcade
chmod +x game.py
./game.py
```
