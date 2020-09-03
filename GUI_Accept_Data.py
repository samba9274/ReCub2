from tkinter import *
from ReCub import *
import CSS
import Tooltip


cursorState = 'X'
colorDict = {'W':"white", 'R':"red", 'B':"blue", 'O':"orange", 'G':"green", 'Y':"yellow", 'X':"#cca5e3"}

def cursorStateUpdate(color):
	global cursorState
	cursorState = color

def update(window, cube, pos):
	cube[pos] = cursorState
	cubeDisplay(window, cube)

def cubeDisplay(window, cube):
	#######################################
	ttl = Label(window, text = cube[0], background = colorDict[cube[0]], font = CSS.FONT)
	ttl.place(x=80*CSS.SIZEMULTIPLIER, y=20*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ttl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 0))

	ttc = Label(window, text = cube[1], background = colorDict[cube[1]], font = CSS.FONT)
	ttc.place(x=100*CSS.SIZEMULTIPLIER, y=20*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ttc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 1))

	ttr = Label(window, text = cube[2], background = colorDict[cube[2]], font = CSS.FONT)
	ttr.place(x=120*CSS.SIZEMULTIPLIER, y=20*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ttr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 2))

	tcl = Label(window, text = cube[3], background = colorDict[cube[3]], font = CSS.FONT)
	tcl.place(x=80*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	tcl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 3))

	tcc = Label(window, text = cube[4], background = colorDict[cube[4]], font = CSS.FONT)
	tcc.place(x=100*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	tcc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 4))

	tcr = Label(window, text = cube[5], background = colorDict[cube[5]], font = CSS.FONT)
	tcr.place(x=120*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	tcr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 5))

	tbl = Label(window, text = cube[6], background = colorDict[cube[6]], font = CSS.FONT)
	tbl.place(x=80*CSS.SIZEMULTIPLIER, y=60*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	tbl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 6))

	tbc = Label(window, text = cube[7], background = colorDict[cube[7]], font = CSS.FONT)
	tbc.place(x=100*CSS.SIZEMULTIPLIER, y=60*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	tbc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 7))

	tbr = Label(window, text = cube[8], background = colorDict[cube[8]], font = CSS.FONT)
	tbr.place(x=120*CSS.SIZEMULTIPLIER, y=60*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	tbr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 8))
	#######################################
	#######################################
	ltl = Label(window, text = cube[9], background = colorDict[cube[9]], font = CSS.FONT)
	ltl.place(x=20*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ltl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 9))

	ltc = Label(window, text = cube[10], background = colorDict[cube[10]], font = CSS.FONT)
	ltc.place(x=40*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ltc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 10))

	ltr = Label(window, text = cube[11], background = colorDict[cube[11]], font = CSS.FONT)
	ltr.place(x=60*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ltr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 11))

	lcl = Label(window, text = cube[12], background = colorDict[cube[12]], font = CSS.FONT)
	lcl.place(x=20*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	lcl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 12))

	lcc = Label(window, text = cube[13], background = colorDict[cube[13]], font = CSS.FONT)
	lcc.place(x=40*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	lcc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 13))

	lcr = Label(window, text = cube[14], background = colorDict[cube[14]], font = CSS.FONT)
	lcr.place(x=60*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	lcr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 14))

	lbl = Label(window, text = cube[15], background = colorDict[cube[15]], font = CSS.FONT)
	lbl.place(x=20*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	lbl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 15))

	lbc = Label(window, text = cube[16], background = colorDict[cube[16]], font = CSS.FONT)
	lbc.place(x=40*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	lbc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 16))

	lbr = Label(window, text = cube[17], background = colorDict[cube[17]], font = CSS.FONT)
	lbr.place(x=60*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	lbr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 17))
	#######################################
	#######################################
	ftl = Label(window, text = cube[18], background = colorDict[cube[18]], font = CSS.FONT)
	ftl.place(x=80*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ftl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 18))

	ftc = Label(window, text = cube[19], background = colorDict[cube[19]], font = CSS.FONT)
	ftc.place(x=100*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ftc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 19))

	ftr = Label(window, text = cube[20], background = colorDict[cube[20]], font = CSS.FONT)
	ftr.place(x=120*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	ftr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 20))

	fcl = Label(window, text = cube[21], background = colorDict[cube[21]], font = CSS.FONT)
	fcl.place(x=80*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	fcl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 21))

	fcc = Label(window, text = cube[22], background = colorDict[cube[22]], font = CSS.FONT)
	fcc.place(x=100*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	fcc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 22))

	fcr = Label(window, text = cube[23], background = colorDict[cube[23]], font = CSS.FONT)
	fcr.place(x=120*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	fcr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 23))

	fbl = Label(window, text = cube[24], background = colorDict[cube[24]], font = CSS.FONT)
	fbl.place(x=80*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	fbl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 24))

	fbc = Label(window, text = cube[25], background = colorDict[cube[25]], font = CSS.FONT)
	fbc.place(x=100*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	fbc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 25))

	fbr = Label(window, text = cube[26], background = colorDict[cube[26]], font = CSS.FONT)
	fbr.place(x=120*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	fbr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 26))
	#######################################
	#######################################
	rtl = Label(window, text = cube[27], background = colorDict[cube[27]], font = CSS.FONT)
	rtl.place(x=140*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	rtl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 27))

	rtc = Label(window, text = cube[28], background = colorDict[cube[28]], font = CSS.FONT)
	rtc.place(x=160*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	rtc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 28))

	rtr = Label(window, text = cube[29], background = colorDict[cube[29]], font = CSS.FONT)
	rtr.place(x=180*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	rtr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 29))

	rcl = Label(window, text = cube[30], background = colorDict[cube[30]], font = CSS.FONT)
	rcl.place(x=140*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	rcl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 30))

	rcc = Label(window, text = cube[31], background = colorDict[cube[31]], font = CSS.FONT)
	rcc.place(x=160*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	rcc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 31))

	rcr = Label(window, text = cube[32], background = colorDict[cube[32]], font = CSS.FONT)
	rcr.place(x=180*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	rcr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 32))

	rbl = Label(window, text = cube[33], background = colorDict[cube[33]], font = CSS.FONT)
	rbl.place(x=140*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	rbl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 33))

	rbc = Label(window, text = cube[34], background = colorDict[cube[34]], font = CSS.FONT)
	rbc.place(x=160*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	rbc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 34))

	rbr = Label(window, text = cube[35], background = colorDict[cube[35]], font = CSS.FONT)
	rbr.place(x=180*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	rbr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 35))
	#######################################
	#######################################
	btl = Label(window, text = cube[36], background = colorDict[cube[36]], font = CSS.FONT)
	btl.place(x=200*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	btl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 36))

	btc = Label(window, text = cube[37], background = colorDict[cube[37]], font = CSS.FONT)
	btc.place(x=220*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	btc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 37))

	btr = Label(window, text = cube[38], background = colorDict[cube[38]], font = CSS.FONT)
	btr.place(x=240*CSS.SIZEMULTIPLIER, y=80*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	btr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 38))

	bcl = Label(window, text = cube[39], background = colorDict[cube[39]], font = CSS.FONT)
	bcl.place(x=200*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	bcl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 39))

	bcc = Label(window, text = cube[40], background = colorDict[cube[40]], font = CSS.FONT)
	bcc.place(x=220*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	bcc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 40))

	bcr = Label(window, text = cube[41], background = colorDict[cube[41]], font = CSS.FONT)
	bcr.place(x=240*CSS.SIZEMULTIPLIER, y=100*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	bcr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 41))

	bbl = Label(window, text = cube[42], background = colorDict[cube[42]], font = CSS.FONT)
	bbl.place(x=200*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	bbl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 42))

	bbc = Label(window, text = cube[43], background = colorDict[cube[43]], font = CSS.FONT)
	bbc.place(x=220*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	bbc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 43))

	bbr = Label(window, text = cube[44], background = colorDict[cube[44]], font = CSS.FONT)
	bbr.place(x=240*CSS.SIZEMULTIPLIER, y=120*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	bbr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 44))
	#######################################
	#######################################
	dtl = Label(window, text = cube[45], background = colorDict[cube[45]], font = CSS.FONT)
	dtl.place(x=80*CSS.SIZEMULTIPLIER, y=140*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	dtl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 45))

	dtc = Label(window, text = cube[46], background = colorDict[cube[46]], font = CSS.FONT)
	dtc.place(x=100*CSS.SIZEMULTIPLIER, y=140*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	dtc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 46))

	dtr = Label(window, text = cube[47], background = colorDict[cube[47]], font = CSS.FONT)
	dtr.place(x=120*CSS.SIZEMULTIPLIER, y=140*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	dtr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 47))

	dcl = Label(window, text = cube[48], background = colorDict[cube[48]], font = CSS.FONT)
	dcl.place(x=80*CSS.SIZEMULTIPLIER, y=160*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	dcl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 48))

	dcc = Label(window, text = cube[49], background = colorDict[cube[49]], font = CSS.FONT)
	dcc.place(x=100*CSS.SIZEMULTIPLIER, y=160*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	dcc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 49))

	dcr = Label(window, text = cube[50], background = colorDict[cube[50]], font = CSS.FONT)
	dcr.place(x=120*CSS.SIZEMULTIPLIER, y=160*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	dcr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 50))

	dbl = Label(window, text = cube[51], background = colorDict[cube[51]], font = CSS.FONT)
	dbl.place(x=80*CSS.SIZEMULTIPLIER, y=180*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	dbl.bind("<Button-1>", lambda X = 'X' : update(window, cube, 51))

	dbc = Label(window, text = cube[52], background = colorDict[cube[52]], font = CSS.FONT)
	dbc.place(x=100*CSS.SIZEMULTIPLIER, y=180*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	dbc.bind("<Button-1>", lambda X = 'X' : update(window, cube, 52))

	dbr = Label(window, text = cube[53], background = colorDict[cube[53]], font = CSS.FONT)
	dbr.place(x=120*CSS.SIZEMULTIPLIER, y=180*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	dbr.bind("<Button-1>", lambda X = 'X' : update(window, cube, 53))
	#######################################

	ColorPaletteFrame = LabelFrame(window, text = "Palette", font = CSS.FONT ,background = CSS.BACKGROUND)
	ColorPaletteFrame.place(x=190*CSS.SIZEMULTIPLIER, y=0*CSS.SIZEMULTIPLIER, width=80*CSS.SIZEMULTIPLIER, height=70*CSS.SIZEMULTIPLIER)
	ColorPaletteToolTip = Tooltip.ToolTip(wdgt = ColorPaletteFrame, msg = "Select color from Palette to fill in the cube.")
	#######################################
	colorPaletteWhite = Label(window, text = 'W', background = colorDict['W'], font = CSS.FONT)
	colorPaletteWhite.place(x=200*CSS.SIZEMULTIPLIER, y=20*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	colorPaletteWhite.bind("<Button-1>",lambda X = 'X' : cursorStateUpdate('W'))
	colorPaletteWhiteToolTip = Tooltip.ToolTip(wdgt = colorPaletteWhite, msg = "Select color from Palette to fill in the cube.")

	colorPaletteRed = Label(window, text = 'R', background = colorDict['R'], font = CSS.FONT)
	colorPaletteRed.place(x=220*CSS.SIZEMULTIPLIER, y=20*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	colorPaletteRed.bind("<Button-1>",lambda X = 'X' : cursorStateUpdate('R'))
	colorPaletteRedToolTip = Tooltip.ToolTip(wdgt = colorPaletteRed, msg = "Select color from Palette to fill in the cube.")

	colorPaletteBlue = Label(window, text = 'B', background = colorDict['B'], font = CSS.FONT)
	colorPaletteBlue.place(x=240*CSS.SIZEMULTIPLIER, y=20*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	colorPaletteBlue.bind("<Button-1>",lambda X = 'X' : cursorStateUpdate('B'))
	colorPaletteBlueToolTip = Tooltip.ToolTip(wdgt = colorPaletteBlue, msg = "Select color from Palette to fill in the cube.")

	colorPaletteOrange = Label(window, text = 'O', background = colorDict['O'], font = CSS.FONT)
	colorPaletteOrange.place(x=200*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	colorPaletteOrange.bind("<Button-1>",lambda X = 'X' : cursorStateUpdate('O'))
	colorPaletteOrangeToolTip = Tooltip.ToolTip(wdgt = colorPaletteOrange, msg = "Select color from Palette to fill in the cube.")

	colorPaletteGreen = Label(window, text = 'G', background = colorDict['G'], font = CSS.FONT)
	colorPaletteGreen.place(x=220*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	colorPaletteGreen.bind("<Button-1>",lambda X = 'X' : cursorStateUpdate('G'))
	colorPaletteGreenToolTip = Tooltip.ToolTip(wdgt = colorPaletteGreen, msg = "Select color from Palette to fill in the cube.")

	colorPaletteYellow = Label(window, text = 'Y', background = colorDict['Y'], font = CSS.FONT)
	colorPaletteYellow.place(x=240*CSS.SIZEMULTIPLIER, y=40*CSS.SIZEMULTIPLIER, width=20*CSS.SIZEMULTIPLIER, height=20*CSS.SIZEMULTIPLIER)
	colorPaletteYellow.bind("<Button-1>",lambda X = 'X' : cursorStateUpdate('Y'))
	colorPaletteYellowToolTip = Tooltip.ToolTip(wdgt = colorPaletteYellow, msg = "Select color from Palette to fill in the cube.")
	#######################################