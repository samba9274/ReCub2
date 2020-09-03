from tkinter import *
from GUI_Accept_Data import *
from ReCub import *
import CFOP
import Common_GUI
import CSS
import Tooltip
import Help

def Solver():
	SolverWindow = Tk()
	SolverWindow.geometry("%dx%d"%(510 * CSS.SIZEMULTIPLIER, 290 * CSS.SIZEMULTIPLIER))
	SolverWindow.config(background =CSS.BACKGROUND)
	cube = ReCub()
	for i in range(0, 54, 1): cube.pos[i] = 'X'
	cube.pos[4:53:9] = ['W', 'R', 'B', 'O', 'G', 'Y']

	cubeDisplay(SolverWindow, cube.pos)

	def Solve(fun):
		methodDict = {"Cross":CFOP.Cross, "F2L":CFOP.F2L, "OLL":CFOP.OLL, "PLL":CFOP.PLL} 
		methodDict[fun](cube)
		cubeDisplay(SolverWindow, cube.pos)

	def update(fun):
		methodDict = {"Up":cube.Up, "UpInverted":cube.UpInverted, "Left":cube.Left, "LeftInverted":cube.LeftInverted, "Right":cube.Right, "RightInverted":cube.RightInverted, "Front":cube.Front, "FrontInverted":cube.FrontInverted, "Back":cube.Back, "BackInverted":cube.BackInverted, "Down":cube.Down, "DownInverted":cube.DownInverted, "Middle":cube.Middle, "MiddleInverted":cube.MiddleInverted, "Equatorial":cube.Equatorial, "EquatorialInverted":cube.EquatorialInverted, "Standing":cube.Standing, "StandingInverted":cube.StandingInverted, "X":cube.X, "XInverted":cube.XInverted, "Y":cube.Y, "YInverted":cube.YInverted, "Z":cube.Z, "ZInverted":cube.ZInverted}
		methodDict[fun]()
		cubeDisplay(SolverWindow, cube.pos)

	def solveReset(solved):
		if solved:
			cube.pos = ['W','W','W','W','W','W','W','W','W',
	        			'R','R','R','R','R','R','R','R','R',
	        			'B','B','B','B','B','B','B','B','B',
	        			'O','O','O','O','O','O','O','O','O',
	        			'G','G','G','G','G','G','G','G','G',
	        			'Y','Y','Y','Y','Y','Y','Y','Y','Y']
		else:
			for i in range(0, 54, 1): cube.pos[i] = 'X'
			cube.pos[4:53:9] = ['W', 'R', 'B', 'O', 'G', 'Y']
		cubeDisplay(SolverWindow, cube.pos)


	RotationFrame = LabelFrame(SolverWindow, text = "Rotations", background =CSS.BACKGROUND, font = CSS.FONT)
	RotationFrame.place(x=270 * CSS.SIZEMULTIPLIER, y=0 * CSS.SIZEMULTIPLIER, width=230 * CSS.SIZEMULTIPLIER, height=280 * CSS.SIZEMULTIPLIER)

	FaceRotationFrame = LabelFrame(SolverWindow, text = "Face", background =CSS.BACKGROUND, font = CSS.FONT)
	FaceRotationFrame.place(x=280 * CSS.SIZEMULTIPLIER, y=20 * CSS.SIZEMULTIPLIER, width=100 * CSS.SIZEMULTIPLIER, height=250 * CSS.SIZEMULTIPLIER)
	######################################################################################
	UpButton = Button(SolverWindow, text = "U", command = lambda: update("Up"), font = CSS.FONT)
	UpButton.place(x=300*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	UpToolTip = Tooltip.ToolTip(wdgt = UpButton, msg ="Rotates Top Face by 90° Clockwise")

	UpInvertedButton = Button(SolverWindow, text = "U'", command = lambda: update("UpInverted"), font = CSS.FONT)
	UpInvertedButton.place(x=340*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	UpInvertedToolTip = Tooltip.ToolTip(wdgt = UpInvertedButton, msg ="Rotates Top Face by 90° Counterclockwise")

	LeftButton = Button(SolverWindow, text = "L", command = lambda: update("Left"), font = CSS.FONT)
	LeftButton.place(x=300*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	LeftToolTip = Tooltip.ToolTip(wdgt = LeftButton, msg ="Rotates Left Face by 90° Clockwise")

	LeftInvertedButton = Button(SolverWindow, text = "L'", command = lambda: update("LeftInverted"), font = CSS.FONT)
	LeftInvertedButton.place(x=340*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	LeftInvertedToolTip = Tooltip.ToolTip(wdgt = LeftInvertedButton, msg ="Rotates Left Face by 90° Counterclockwise")

	RightButton = Button(SolverWindow, text = "R", command = lambda: update("Right"), font = CSS.FONT)
	RightButton.place(x=300*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	RightToolTip = Tooltip.ToolTip(wdgt = RightButton, msg ="Rotates Right Face by 90° Clockwise")

	RightInvertedButton = Button(SolverWindow, text = "R'", command = lambda: update("RightInverted"), font = CSS.FONT)
	RightInvertedButton.place(x=340*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	RightInvertedToolTip = Tooltip.ToolTip(wdgt = RightInvertedButton, msg ="Rotates Right Face by 90° Counterclockwise")

	FrontButton = Button(SolverWindow, text = "F", command = lambda: update("Front"), font = CSS.FONT)
	FrontButton.place(x=300*CSS.SIZEMULTIPLIER, y=160*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	FrontToolTip = Tooltip.ToolTip(wdgt = FrontButton, msg ="Rotates Front Face by 90° Clockwise")

	FrontInvertedButton = Button(SolverWindow, text = "F'", command = lambda: update("FrontInverted"), font = CSS.FONT)
	FrontInvertedButton.place(x=340*CSS.SIZEMULTIPLIER, y=160*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	FrontInvertedToolTip = Tooltip.ToolTip(wdgt = FrontInvertedButton, msg ="Rotates Front Face by 90° Counterclockwise")

	BackButton = Button(SolverWindow, text = "B", command = lambda: update("Back"), font = CSS.FONT)
	BackButton.place(x=300*CSS.SIZEMULTIPLIER, y=200*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	BackToolTip = Tooltip.ToolTip(wdgt = BackButton, msg ="Rotates Back Face by 90° Clockwise")

	BackInvertedButton = Button(SolverWindow, text = "B'", command = lambda: update("BackInverted"), font = CSS.FONT)
	BackInvertedButton.place(x=340*CSS.SIZEMULTIPLIER, y=200*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	BackInvertedToolTip = Tooltip.ToolTip(wdgt = BackInvertedButton, msg ="Rotates Back Face by 90° Counterclockwise")

	DownButton = Button(SolverWindow, text = "D", command = lambda: update("Down"), font = CSS.FONT)
	DownButton.place(x=300*CSS.SIZEMULTIPLIER, y=240*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	DownToolTip = Tooltip.ToolTip(wdgt = DownButton, msg ="Rotates Bottom Face by 90° Clockwise")

	DownInvertedButton = Button(SolverWindow, text = "D'", command = lambda: update("DownInverted"), font = CSS.FONT)
	DownInvertedButton.place(x=340*CSS.SIZEMULTIPLIER, y=240*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	DownInvertedToolTip = Tooltip.ToolTip(wdgt = DownInvertedButton, msg ="Rotates Bottom Face by 90° Counterclockwise")
	######################################################################################

	SliceRotationFrame = LabelFrame(SolverWindow, text = "Slice", background =CSS.BACKGROUND, font = CSS.FONT)
	SliceRotationFrame.place(x=390 * CSS.SIZEMULTIPLIER, y=20 * CSS.SIZEMULTIPLIER, width=100 * CSS.SIZEMULTIPLIER, height=125 * CSS.SIZEMULTIPLIER)
	######################################################################################
	MiddleButton = Button(SolverWindow, text = "M", command = lambda: update("Middle"), font = CSS.FONT)
	MiddleButton.place(x=410*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	MiddleToolTip = Tooltip.ToolTip(wdgt = MiddleButton, msg ="Middle Slice Rotation")

	MiddleInvertedButton = Button(SolverWindow, text = "M'", command = lambda: update("MiddleInverted"), font = CSS.FONT)
	MiddleInvertedButton.place(x=450*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	MiddleInvertedToolTip = Tooltip.ToolTip(wdgt = MiddleInvertedButton, msg ="MiddleInverted Slice Rotation")

	EquatorialButton = Button(SolverWindow, text = "E", command = lambda: update("Equatorial"), font = CSS.FONT)
	EquatorialButton.place(x=410*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	EquatorialToolTip = Tooltip.ToolTip(wdgt = EquatorialButton, msg ="Equatorial Slice Rotation")

	EquatorialInvertedButton = Button(SolverWindow, text = "E'", command = lambda: update("EquatorialInverted"), font = CSS.FONT)
	EquatorialInvertedButton.place(x=450*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	EquatorialInvertedToolTip = Tooltip.ToolTip(wdgt = EquatorialInvertedButton, msg ="EquatorialInverted Slice Rotation")

	StandingButton = Button(SolverWindow, text = "S", command = lambda: update("Standing"), font = CSS.FONT)
	StandingButton.place(x=410*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	StandingToolTip = Tooltip.ToolTip(wdgt = StandingButton, msg ="Standing Slice Rotation")

	StandingInvertedButton = Button(SolverWindow, text = "S'", command = lambda: update("StandingInverted"), font = CSS.FONT)
	StandingInvertedButton.place(x=450*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	StandingInvertedToolTip = Tooltip.ToolTip(wdgt = StandingInvertedButton, msg ="StandingInverted Slice Rotation")
	######################################################################################


	CubeRotationFrame = LabelFrame(SolverWindow, text = "Cube", background =CSS.BACKGROUND, font = CSS.FONT)
	CubeRotationFrame.place(x=390 * CSS.SIZEMULTIPLIER, y=140 * CSS.SIZEMULTIPLIER, width=100 * CSS.SIZEMULTIPLIER, height=130 * CSS.SIZEMULTIPLIER)
	######################################################################################
	XButton = Button(SolverWindow, text = "X", command = lambda: update("X"), font = CSS.FONT)
	XButton.place(x=410*CSS.SIZEMULTIPLIER, y=160*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	XToolTip = Tooltip.ToolTip(wdgt = XButton, msg ="X Cube Rotation")

	XInvertedButton = Button(SolverWindow, text = "X'", command = lambda: update("XInverted"), font = CSS.FONT)
	XInvertedButton.place(x=450*CSS.SIZEMULTIPLIER, y=160*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	XInvertedToolTip = Tooltip.ToolTip(wdgt = XInvertedButton, msg ="XInverted Cube Rotation")

	YButton = Button(SolverWindow, text = "Y", command = lambda: update("Y"), font = CSS.FONT)
	YButton.place(x=410*CSS.SIZEMULTIPLIER, y=200*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	YToolTip = Tooltip.ToolTip(wdgt = YButton, msg ="Y Cube Rotation")

	YInvertedButton = Button(SolverWindow, text = "Y'", command = lambda: update("YInverted"), font = CSS.FONT)
	YInvertedButton.place(x=450*CSS.SIZEMULTIPLIER, y=200*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	YInvertedToolTip = Tooltip.ToolTip(wdgt = YInvertedButton, msg ="YInverted Cube Rotation")

	ZButton = Button(SolverWindow, text = "Z", command = lambda: update("Z"), font = CSS.FONT)
	ZButton.place(x=410*CSS.SIZEMULTIPLIER, y=240*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ZToolTip = Tooltip.ToolTip(wdgt = ZButton, msg ="Z Cube Rotation")

	ZInvertedButton = Button(SolverWindow, text = "Z'", command = lambda: update("ZInverted"), font = CSS.FONT)
	ZInvertedButton.place(x=450*CSS.SIZEMULTIPLIER, y=240*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ZInvertedToolTip = Tooltip.ToolTip(wdgt = ZInvertedButton, msg ="ZInverted Cube Rotation")
	######################################################################################

	######################################################################################
	ClearButton = Button(SolverWindow, text = "Clear", command = lambda: solveReset(False), font = CSS.FONT)
	ClearButton.place(x=90*CSS.SIZEMULTIPLIER, y=210*CSS.SIZEMULTIPLIER, width=40*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ClearToolTip = Tooltip.ToolTip(wdgt = ClearButton, msg ="Clear")

	ResetButton = Button(SolverWindow, text = "Reset", command = lambda: solveReset(True), font = CSS.FONT)
	ResetButton.place(x=90*CSS.SIZEMULTIPLIER, y=250*CSS.SIZEMULTIPLIER, width=40*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ResetToolTip = Tooltip.ToolTip(wdgt = ResetButton, msg ="Reset")
	######################################################################################

	SolveFrame = LabelFrame(SolverWindow, text = "Cube", background =CSS.BACKGROUND, font = CSS.FONT)
	SolveFrame.place(x=140 * CSS.SIZEMULTIPLIER, y=190 * CSS.SIZEMULTIPLIER, width=130 * CSS.SIZEMULTIPLIER, height=90 * CSS.SIZEMULTIPLIER)
	######################################################################################
	CrossButton = Button(SolverWindow, text = "1.Cross", command = lambda: Solve("Cross"), font = CSS.FONT)
	CrossButton.place(x=150*CSS.SIZEMULTIPLIER, y=210*CSS.SIZEMULTIPLIER, width=50*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	CrossToolTip = Tooltip.ToolTip(wdgt = CrossButton, msg = "First step of Solving cube")

	F2LButton = Button(SolverWindow, text = "2.F2L", command = lambda: Solve("F2L"), font = CSS.FONT)
	F2LButton.place(x=210*CSS.SIZEMULTIPLIER, y=210*CSS.SIZEMULTIPLIER, width=50*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	F2LToolTip = Tooltip.ToolTip(wdgt = F2LButton, msg ="Second step of Solving cube")

	OLLButton = Button(SolverWindow, text = "3.OLL", command = lambda: Solve("OLL"), font = CSS.FONT)
	OLLButton.place(x=150*CSS.SIZEMULTIPLIER, y=250*CSS.SIZEMULTIPLIER, width=50*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	OLLToolTip = Tooltip.ToolTip(wdgt = OLLButton, msg ="Third step of Solving cube")

	PLLButton = Button(SolverWindow, text = "4.PLL", command = lambda: Solve("PLL"), font = CSS.FONT)
	PLLButton.place(x=210*CSS.SIZEMULTIPLIER, y=250*CSS.SIZEMULTIPLIER, width=50*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	PLLToolTip = Tooltip.ToolTip(wdgt = PLLButton, msg ="Fourth step of Solving cube")
	######################################################################################

	######################################################################################
	back = Button(SolverWindow, text="<-", command = lambda: Common_GUI.newWindow(SolverWindow, Common_GUI.Common_GUI), font = CSS.FONT)
	back.place(x=0*CSS.SIZEMULTIPLIER, y=0*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	######################################################################################

	menubar = Menu(SolverWindow)
	helpMenu = Menu(menubar ,tearoff = 0)
	#helpMenu.add_command(label = "Notations", command = lambda : Help.Notations())
	#helpMenu.add_command(label = "Solution")
	#helpMenu.add_separator()
	helpMenu.add_command(label = "About", command = lambda : Help.About())
	menubar.add_cascade(label = "Help", menu = helpMenu)

	cubeDisplay(SolverWindow, cube.pos)

	SolverWindow.config(menu=menubar)
	SolverWindow.mainloop()