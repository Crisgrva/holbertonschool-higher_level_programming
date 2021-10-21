# Imports each and every method and class
# of module tkinter and tkinter.ttk
from tkinter import *
from tkinter.ttk import *
class Shape:
	def __init__(self, master = None):
		self.master = master
		
		# Calls create method of class Shape
		self.create()
	
	def create(self):
		
		# Creates a object of class canvas
		# with the help of this we can create different shapes
		self.canvas = Canvas(self.master)

		# Creates a circle of diameter 80
		self.canvas.create_oval(10, 10, 80, 80,
							outline = "black", fill = "white",
							width = 2)
		self.canvas.pack(fill = BOTH, expand = 1)

if __name__ == "__main__":
	
	# object of class Tk, resposible for creating
	# a tkinter toplevel window
	master = Tk()
	shape = Shape(master)

	# Sets the title to Shapes
	master.title("Shapes")

	# Sets the geometry and position
	# of window on the screen
	master.geometry("330x220")

	# Infinite loop breaks only by interrupt
	mainloop()

