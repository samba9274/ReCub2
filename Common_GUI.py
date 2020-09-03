from tkinter import *
import Stopwatch
import Solver
import CSS

def newWindow(currentWindow, func):
	currentWindow.destroy()
	func()

def Common_GUI():
	#Window
	Common_GUI = Tk()
	Common_GUI.geometry("%dx%d"%(260 * CSS.SIZEMULTIPLIER, 120 * CSS.SIZEMULTIPLIER))
	Common_GUI.config(background = CSS.BACKGROUND)

	#Button to Solver Window
	SolverButton = Button(Common_GUI, text="Solver", command = lambda: newWindow(Common_GUI, Solver.Solver))
	SolverButton.place(x=20*CSS.SIZEMULTIPLIER, y=20*CSS.SIZEMULTIPLIER, width=100*CSS.SIZEMULTIPLIER, height=30*CSS.SIZEMULTIPLIER)

	#Button to Stopwatch Window
	StopwatchButton = Button(Common_GUI, text="Stopwatch", command = lambda: newWindow(Common_GUI, Stopwatch.Stopwatch))	
	StopwatchButton.place(x=140*CSS.SIZEMULTIPLIER, y=20*CSS.SIZEMULTIPLIER, width=100*CSS.SIZEMULTIPLIER, height=30*CSS.SIZEMULTIPLIER)

	#Button to Quit Window
	QuitButton = Button(Common_GUI, text="Quit", command = lambda: Common_GUI.destroy())
	QuitButton.place(x=105*CSS.SIZEMULTIPLIER, y=70*CSS.SIZEMULTIPLIER, width=50*CSS.SIZEMULTIPLIER, height=30*CSS.SIZEMULTIPLIER)

	Common_GUI.mainloop()