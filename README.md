Pong Game

This is a Python script that implements the classic game Pong using the turtle module. It provides a simple two-player game where players control paddles to hit a ball back and forth. The game keeps track of the score and ends when one player reaches a certain score limit.

Prerequisites

    Python 3.x
    turtle module

Installation

    Make sure you have Python 3.x installed on your system.
    No additional package installation is required.

Usage

    Save the script to a file with a .py extension (e.g., pong_game.py).
    Run the script using the following command:

    python pong_game.py

    The Pong game window will appear.
    Player 1 (right paddle) can control the paddle using the Up and Down arrow keys.
    Player 2 (left paddle) can control the paddle using the W and S keys.
    The game starts automatically, and players hit the ball back and forth.
    Each time the ball goes past a paddle and hits the wall behind it, the opposing player scores a point.
    The game continues until one player reaches the score limit.
    After the game ends, you can close the window by clicking on it.

Customization

You can customize the following aspects of the Pong game:

    Window Size: Modify the width and height parameters in the screen.setup() line to change the dimensions of the game window.
    Background Color: Change the screen.bgcolor() parameter to set the background color of the game window.
    Player Controls: Update the screen.onkey() lines to assign different keys for player controls.
    Score Limit: Modify the condition in the while loop to set a different score limit for ending the game.
