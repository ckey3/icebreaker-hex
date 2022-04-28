import board
import time
import neopixel
npix = 38

pixels = neopixel.NeoPixel(board.D18, npix)

class hex:
	def __init__(self,n):
		self.i = n
		self.j = n+1
	def Top(self,color = (0,255,0)):
		pixels[self.i] = color
	def bot(self,color = (0,255,0)):
		pixels[self.j] = color
	def color(self,color = (255,255,0)):
		pixels[self.i] = color
		pixels[self.j] = color


class tileSet:
	def __init__(self):
		self.hexes = []
		for i in range(19):
			self.hexes.append(hex(i*2))

	def all(self,color = (0,0,255)):
		for h in self.hexes:
			h.color(color)

#	def one(self):
#		self.i =
