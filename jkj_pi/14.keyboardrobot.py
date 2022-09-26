import curses

import RPi.GPIO as GPIO

import time

import move

screen =curses.initscr()

curses.noecho()

curses.halfdelay(1)

screen.keypad(True)



def code():

	while True:

		char = screen.getch()

		if char  == curses.KEY_UP:

			move.forward(60)

			print ("up")

		elif char ==  curses.KEY_DOWN:

			move.reverse(60)

			print ("down")

		elif char == curses.KEY_LEFT:

			move.left(60)

			print ("left")

		elif char == curses.KEY_RIGHT:

			move.right(60)

			print ("right")

		else:

			move.stop()

if __name__=='__main__':

	try:

		code()

	except:

		screen.keypad(0)
		curses.echo()

		curses.endwin()

		GPIO.cleanup()
