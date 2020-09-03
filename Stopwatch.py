from tkinter import *
import random
import Common_GUI
import CSS
  
running = False
counter = 0

def Stopwatch():
	def scramble():
		scramble = ''
		for i in range(0, 18, 1):
			scramble += random.choice(["U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'", "M", "M'"]) + ' '
		return scramble

	def Reset(label): 
	    global counter 
	    counter=0
	    if running==False:       
	        reset['state']='disabled'
	        label['text']='0.00'
	        scrambleLabel['text'] = scramble()
	    else:                
	        label['text']='0.00'

	def Toggle(x):
		global running 
		if running:
			reset['state']='normal'
			running = False
		else:
			running=True
			def count(): 
				if running: 
					global counter 
					display="%.2f"%counter 
					label['text']=display
					label.after(10, count)  
					counter += 0.01
			count()     
			reset['state']='normal'
	  
	StopwatchWindow = Tk() 
	StopwatchWindow.title("Stopwatch") 
	StopwatchWindow.config(background = CSS.BACKGROUND)
	StopwatchWindow.geometry("%dx%d"%(350 * CSS.SIZEMULTIPLIER, 100 * CSS.SIZEMULTIPLIER)) 
	scrambleLabel = Label(StopwatchWindow, text = scramble(), background = "#808080", font = CSS.FONT)
	scrambleLabel.place(x=10*CSS.SIZEMULTIPLIER, y=10*CSS.SIZEMULTIPLIER, width=330*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	label = Label(StopwatchWindow, text="0.00", fg="black", font="Arial %d bold"%(30 * CSS.SIZEMULTIPLIER), background = "#808080") 
	label.place(x=125*CSS.SIZEMULTIPLIER, y=30*CSS.SIZEMULTIPLIER, width=100*CSS.SIZEMULTIPLIER)
	StopwatchWindow.bind("<space>", Toggle)
	reset = Button(StopwatchWindow, text="Reset", state='disabled', command=lambda:Reset(label), background = "#808080") 
	reset.place(x=250*CSS.SIZEMULTIPLIER, y=45*CSS.SIZEMULTIPLIER, width=50*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	back = Button(StopwatchWindow, text="<-", command = lambda: Common_GUI.newWindow(StopwatchWindow, Common_GUI.Common_GUI))
	back.place(x=0*CSS.SIZEMULTIPLIER, y=0*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	StopwatchWindow.mainloop() 