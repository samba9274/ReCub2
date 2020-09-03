from ReCub import *

def Cross(cube):
	"""
	First step to solve the 3x3x3 Rubik's cube. After execution, returns a cube with white cross.
	"""
	print("################################\nCross:\n")

	while(True):
		if(cube.pos[1] == 'W' and cube.pos[3] == 'W' and cube.pos[5] == 'W' and cube.pos[7] == 'W'):break

		for i in range(0, 4, 1):
			if(cube.pos[46] == 'W'):
				while(cube.pos[7] == 'W'):
					cube.Up()
				cube.Front()
				cube.Front()
			cube.Y()

		for i in range(0, 4, 1):
			if(cube.pos[16] == 'W'):
				while(cube.pos[7] == 'W'):
					cube.Up()
				cube.LeftInverted()
				cube.Front()
				cube.Left()
				count = 0
			cube.Y()

		for i in range(0, 4, 1):
			if(cube.pos[12]=='W'):	
				while(cube.pos[1] == 'W'):
					cube.Up()
				cube.BackInverted()
			cube.Y()

		for i in range(0, 4, 1):
			if(cube.pos[14]=='W'):
				while(cube.pos[7] == 'W'):
					cube.Up()
				cube.Front()
			cube.Y()

		for i in range(0, 4, 1):
			if(cube.pos[10]=='W'):
				cube.Left()
				cube.UpInverted()
				cube.Front()
				cube.Up()
			cube.Y()

	cube.Middle()
	cube.Middle()
	cube.Standing()
	cube.Standing()


	for i in range(0, 4, 1):
		while(True):
			if(cube.pos[22]==cube.pos[25]):break
			cube.Down()
		cube.Front()
		cube.Front()
		cube.Y()

	cube.Y()
	cube.Y()

def F2L(cube):
	"""
	Second step of Rubik's cube sloution. Ends with First 2 Layers solved in the cube.
	"""
	print("################################\nF2L:\n")
	for i in range(0, 4, 1):
		while(True):
			if (cube.pos[8] != 'W' and cube.pos[20] != 'W' and cube.pos[27] != 'W'): break
			if(cube.pos[26] != 'W' and cube.pos[33] != 'W' and cube.pos[47] != 'W'):
				cube.RightInverted()
				cube.DownInverted()
				cube.Right()
				cube.Down()
				break
			cube.Down()
		cube.Up()


	for i in range(0, 4, 1):
		while(True):
			if((cube.pos[26] == cube.pos[22] or cube.pos[33] == cube.pos[22] or cube.pos[47] == cube.pos[22]) and (cube.pos[26] == cube.pos[31] or cube.pos[33] == cube.pos[31] or cube.pos[47] == cube.pos[31]) and (cube.pos[26] == 'W' or cube.pos[33] == 'W' or cube.pos[47] == 'W')):
				while(True):
					if(cube.pos[8] == 'W'): break
					cube.RightInverted()
					cube.DownInverted()
					cube.Right()
					cube.Down()
				break
			cube.Down()
		cube.Y()

	for i in range(0, 4, 1):
		if(cube.pos[23] != 'Y' and cube.pos[30] != 'Y'):
			while(True):
				if(cube.pos[25] != 'Y' and cube.pos[46] != 'Y'):
					cube.Down()
				else:
					cube.DownInverted()
					cube.RightInverted()
					cube.Down()
					cube.Right()
					cube.Down()
					cube.Front()
					cube.DownInverted()
					cube.FrontInverted()
					break
		cube.Y()

	for i in range(0, 16, 1):
		count = 0
		while(count<4):
			count += 1
			if(cube.pos[22] == cube.pos[25]): break
			cube.Down()
		if(cube.pos[46] == cube.pos[31]):
			cube.DownInverted()
			cube.RightInverted()
			cube.Down()
			cube.Right()
			cube.Down()
			cube.Front()
			cube.DownInverted()
			cube.FrontInverted()
		elif(cube.pos[46] == cube.pos[13]):
			cube.Down()
			cube.Left()
			cube.DownInverted()
			cube.LeftInverted()
			cube.DownInverted()
			cube.FrontInverted()
			cube.Down()
			cube.Front()
		cube.Y()



def OLL(cube):
	"""
	Third step in solveing cube. Orients Last Layer of cube. Solid yellow face.
	"""
	print("################################\nOLL:\n")
	while(True):
		if(cube.pos[46] == cube.pos[48] == cube.pos[50] == cube.pos[52] == 'Y'): break

		#Dot
		if(cube.pos[46] != 'Y' and cube.pos[48] != 'Y' and cube.pos[50] != 'Y' and cube.pos[52] != 'Y'):
			cube.X()
			cube.X()
			cube.Front()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.FrontInverted()
			cube.Front()
			cube.Standing()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.FrontInverted()
			cube.StandingInverted()
			cube.XInverted()
			cube.XInverted()
			break


		#L
		elif(cube.pos[46] == 'Y' and cube.pos[48] == 'Y' and cube.pos[50] != 'Y' and cube.pos[52] != 'Y'):
			cube.X()
			cube.X()
			cube.Front()
			cube.Up()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.FrontInverted()
			cube.XInverted()
			cube.XInverted()
			break
		
		#Dash	
		elif(cube.pos[46] != 'Y' and cube.pos[48] == 'Y' and cube.pos[50] == 'Y' and cube.pos[52] != 'Y'):
			cube.X()
			cube.X()
			cube.Front()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.FrontInverted()
			cube.XInverted()
			cube.XInverted()
			break

		cube.Down()

	while(True):
		if(cube.pos[45] == cube.pos[46] == cube.pos[47] == cube.pos[48] == cube.pos[49] == cube.pos[50] == cube.pos[51] == cube.pos[52] == cube.pos[53] == 'Y'): break

		#21
		elif(cube.pos[52] == cube.pos[46] == cube.pos[50] == cube.pos[48] == cube.pos[24] == cube.pos[44] == cube.pos[42] == cube.pos[26] == 'Y'):
			cube.X()
			cube.X()
			cube.Right()
			cube.Up()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.XInverted()
			cube.XInverted()
			break
	    #22
		elif(cube.pos[48] == cube.pos[50] == cube.pos[46] == cube.pos[52] == cube.pos[26] == cube.pos[42] == cube.pos[17] == cube.pos[15] == 'Y'):
			cube.X()
			cube.X()
			cube.Right()
			cube.UpInverted()
			cube.UpInverted()
			cube.Right()
			cube.Right()
			cube.UpInverted()
			cube.Right()
			cube.Right()
			cube.UpInverted()
			cube.Right()
			cube.Right()
			cube.UpInverted()
			cube.UpInverted()
			cube.Right()
			cube.XInverted()
			cube.XInverted()
			break

		#23
		elif(cube.pos[48] == cube.pos[45] == cube.pos[46] == cube.pos[47] == cube.pos[50] == cube.pos[42] == cube.pos[52] == cube.pos[44] == 'Y'):
			cube.X()
			cube.X()
			cube.Right()
			cube.Right()
			cube.Down()
			cube.RightInverted()
			cube.Up()
			cube.Up()
			cube.Right()
			cube.DownInverted()
			cube.RightInverted()
			cube.Up()
			cube.Up()
			cube.RightInverted()
			cube.XInverted()
			cube.XInverted()
			break

		#24
		elif(cube.pos[51] == cube.pos[48] == cube.pos[45] == cube.pos[46] == cube.pos[26] == cube.pos[50] == cube.pos[42] == cube.pos[52] == 'Y'):
			cube.X()
			cube.X()
			cube.LeftInverted()
			cube.MiddleInverted()
			cube.UpInverted()
			cube.Left()
			cube.Up()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.Middle()
			cube.Front()
			cube.XInverted()
			cube.XInverted()
			break

		#25
		elif(cube.pos[48] == cube.pos[45] == cube.pos[46] == cube.pos[33] == cube.pos[50] == cube.pos[53] == cube.pos[52] == cube.pos[44] == 'Y'):
			cube.X()
			cube.X()
			cube.RightInverted()
			cube.Front()
			cube.Right()
			cube.BackInverted()
			cube.RightInverted()
			cube.FrontInverted()
			cube.Right()
			cube.Back()
			cube.XInverted()
			cube.XInverted()
			break

		#26
		elif(cube.pos[45] == cube.pos[46] == cube.pos[26] == cube.pos[48] == cube.pos[50] == cube.pos[44] == cube.pos[52] == cube.pos[35] == 'Y'):
			cube.X()
			cube.X()
			cube.RightInverted()
			cube.UpInverted()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.Up()
			cube.Up()
			cube.Right()
			cube.XInverted()
			cube.XInverted()
			break

		#27
		elif(cube.pos[24] == cube.pos[46] == cube.pos[47] == cube.pos[48] == cube.pos[50] == cube.pos[15] == cube.pos[52] == cube.pos[42] == 'Y'):
			cube.X()
			cube.X()
			cube.Left()
			cube.Up()
			cube.LeftInverted()
			cube.Up()
			cube.Left()
			cube.Up()
			cube.Up()
			cube.LeftInverted()
			cube.XInverted()
			cube.XInverted()
			break

		cube.Down()
	



def PLL(cube):
	"""
	Permutation of Last Layer. Solves entire cube.
	"""
	print("################################\nPLL:\n")

	while(True):
		if(cube.checkSolve()): break

		#Ua
		elif((cube.pos[24] == cube.pos[25] == cube.pos[26]) and (cube.pos[15] == cube.pos[34] == cube.pos[17]) and (cube.pos[42] == cube.pos[16] == cube.pos[44]) and (cube.pos[33] == cube.pos[43] == cube.pos[35])):
			cube.X()
			cube.X()
			cube.Right()
			cube.UpInverted()
			cube.Right()
			cube.Up()
			cube.Right()
			cube.Up()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.UpInverted()
			cube.Right()
			cube.Right()
			cube.XInverted()
			cube.XInverted()
			break

		#Ub
		elif((cube.pos[24] == cube.pos[25] == cube.pos[26]) and (cube.pos[15] == cube.pos[43] == cube.pos[17]) and (cube.pos[42] == cube.pos[34] == cube.pos[44]) and (cube.pos[33] == cube.pos[16] == cube.pos[35])):
			cube.X()
			cube.X()
			cube.Right()
			cube.Right()
			cube.Up()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.RightInverted()
			cube.UpInverted()
			cube.RightInverted()
			cube.Up()
			cube.RightInverted()
			cube.XInverted()
			cube.XInverted()
			break

		#Z
		elif((cube.pos[24] == cube.pos[34] == cube.pos[26]) and (cube.pos[15] == cube.pos[43] == cube.pos[17]) and (cube.pos[42] == cube.pos[16] == cube.pos[44]) and (cube.pos[33] == cube.pos[25] == cube.pos[35])):
			cube.X()
			cube.X()
			cube.Middle()
			cube.Middle()
			cube.Up()
			cube.Middle()
			cube.Middle()
			cube.Up()
			cube.MiddleInverted()
			cube.Up()
			cube.Up()
			cube.Middle()
			cube.Middle()
			cube.Up()
			cube.Up()
			cube.MiddleInverted()
			cube.Up()
			cube.Up()
			cube.XInverted()
			cube.XInverted()
			break

		#H
		elif((cube.pos[24] == cube.pos[43] == cube.pos[26]) and (cube.pos[15] == cube.pos[34] == cube.pos[17]) and (cube.pos[42] == cube.pos[25] == cube.pos[44]) and (cube.pos[33] == cube.pos[16] == cube.pos[35])):
			cube.X()
			cube.X()
			cube.Middle()
			cube.Middle()
			cube.Up()
			cube.Middle()
			cube.Middle()
			cube.Up()
			cube.Up()
			cube.Middle()
			cube.Middle()
			cube.Up()
			cube.Middle()
			cube.Middle()
			cube.XInverted()
			cube.XInverted()
			break

		#Aa
		elif((cube.pos[42] == cube.pos[25] == cube.pos[17]) and (cube.pos[15] == cube.pos[16] == cube.pos[35]) and (cube.pos[44] == cube.pos[43] == cube.pos[33]) and (cube.pos[24] == cube.pos[34] == cube.pos[26])):
			cube.X()
			cube.X()
			cube.LeftInverted()
			cube.MiddleInverted()
			cube.Up()
			cube.RightInverted()
			cube.Down()
			cube.Down()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.Down()
			cube.Down()
			cube.Right()
			cube.Right()
			cube.XInverted()
			cube.XInverted()
			break

		#Ab
		elif((cube.pos[33] == cube.pos[16] == cube.pos[17]) and (cube.pos[24] == cube.pos[25] == cube.pos[35]) and (cube.pos[42] == cube.pos[34] == cube.pos[44]) and (cube.pos[15] == cube.pos[43] == cube.pos[26])):
			cube.X()
			cube.X()
			cube.Left()
			cube.Middle()
			cube.UpInverted()
			cube.Right()
			cube.Down()
			cube.Down()
			cube.RightInverted()
			cube.Up()
			cube.Right()
			cube.Down()
			cube.Down()
			cube.Right()
			cube.Right()
			cube.XInverted()
			cube.XInverted()
			break

		#E
		elif((cube.pos[24] == cube.pos[16] == cube.pos[44]) and (cube.pos[15] == cube.pos[25] == cube.pos[35]) and (cube.pos[26] == cube.pos[34] == cube.pos[42]) and (cube.pos[33] == cube.pos[43] == cube.pos[17])):
			cube.X()
			cube.X()
			cube.XInverted()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.Down()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.DownInverted()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.Down()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.DownInverted()
			cube.X()
			cube.XInverted()
			cube.XInverted()
			break

		#T
		elif((cube.pos[15] == cube.pos[34] == cube.pos[17]) and (cube.pos[24] == cube.pos[25] == cube.pos[35]) and (cube.pos[43] == cube.pos[44] == cube.pos[33]) and (cube.pos[42] == cube.pos[43] == cube.pos[33])):
			cube.X()
			cube.X()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.RightInverted()
			cube.Front()
			cube.Right()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.UpInverted()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.FrontInverted()
			cube.XInverted()
			cube.XInverted()
			break

		#F
		elif((cube.pos[42] == cube.pos[43] == cube.pos[44]) and (cube.pos[15] == cube.pos[34] == cube.pos[26]) and (cube.pos[17] == cube.pos[25] == cube.pos[33]) and (cube.pos[35] == cube.pos[16] == cube.pos[24])):
			cube.X()
			cube.X()
			cube.RightInverted()
			cube.Up()
			cube.Right()
			cube.UpInverted()
			cube.Right()
			cube.Right()
			cube.YInverted()
			cube.RightInverted()
			cube.UpInverted()
			cube.Right()
			cube.Up()
			cube.Y()
			cube.X()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.Right()
			cube.Right()
			cube.X()
			cube.UpInverted()

		#Ja
		elif((cube.pos[42] == cube.pos[43] == cube.pos[44]) and (cube.pos[24] == cube.pos[34] == cube.pos[35]) and (cube.pos[16] == cube.pos[17] == cube.pos[33]) and (cube.pos[15] == cube.pos[25] == cube.pos[26])):
			cube.X()
			cube.X()
			cube.RightInverted()
			cube.Up()
			cube.LeftInverted()
			cube.Up()
			cube.Up()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.Up()
			cube.Up()
			cube.Left()
			cube.Right()
			cube.UpInverted()
			cube.XInverted()
			cube.XInverted()

	    #Jb
		elif((cube.pos[33] == cube.pos[43] == cube.pos[35]) and (cube.pos[34] == cube.pos[42] == cube.pos[44]) and (cube.pos[15] == cube.pos[16] == cube.pos[17]) and (cube.pos[24] == cube.pos[25] == cube.pos[44])):
			cube.X()
			cube.X()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.FrontInverted()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.RightInverted()
			cube.Front()
			cube.Right()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.UpInverted()
			cube.XInverted()
			cube.XInverted()
			break

	    #Ra
		elif((cube.pos[15] == cube.pos[43] == cube.pos[26]) and (cube.pos[24] == cube.pos[25] == cube.pos[26]) and (cube.pos[24] == cube.pos[34] == cube.pos[35]) and (cube.pos[15] == cube.pos[16] == cube.pos[42])):
			cube.X()
			cube.X()
			cube.Left()
			cube.UpInverted()
			cube.UpInverted()
			cube.LeftInverted()
			cube.UpInverted()
			cube.UpInverted()
			cube.Left()
			cube.FrontInverted()
			cube.LeftInverted()
			cube.UpInverted()
			cube.Left()
			cube.Up()
			cube.Left()
			cube.Front()
			cube.LeftInverted()
			cube.LeftInverted()
			cube.Up()
			cube.XInverted()
			cube.XInverted()
			break

		#Rb
		elif((cube.pos[15] == cube.pos[16] == cube.pos[26]) and (cube.pos[17] == cube.pos[25] == cube.pos[33]) and (cube.pos[24] == cube.pos[43] == cube.pos[35]) and (cube.pos[42] == cube.pos[34] == cube.pos[44])):
			cube.X()
			cube.X()
			cube.RightInverted()
			cube.Up()
			cube.Up()
			cube.Right()
			cube.Up()
			cube.Up()
			cube.RightInverted()
			cube.Front()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.RightInverted()
			cube.FrontInverted()
			cube.Right()
			cube.Right()
			cube.UpInverted()
			cube.XInverted()
			cube.XInverted()

		#V
		elif((cube.pos[15] == cube.pos[16] == cube.pos[35]) and (cube.pos[42] == cube.pos[34] == cube.pos[26]) and (cube.pos[33] == cube.pos[25] == cube.pos[17]) and (cube.pos[23] == cube.pos[43] == cube.pos[44])):
			cube.X()
			cube.X()
			cube.RightInverted()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.X()
			cube.X()
			cube.YInverted()
			cube.RightInverted()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.Left()
			cube.Middle()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.Up()
			cube.Right()
			cube.Up()
			cube.Y()
			break

		#Y
		elif((cube.pos[15] == cube.pos[25] == cube.pos[35]) and (cube.pos[42] == cube.pos[16] == cube.pos[26]) and (cube.pos[33] == cube.pos[34] == cube.pos[17]) and (cube.pos[24] == cube.pos[43] == cube.pos[44])):
			cube.X()
			cube.X()
			cube.Front()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.UpInverted()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.FrontInverted()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.RightInverted()
			cube.Front()
			cube.Right()
			cube.FrontInverted()
			cube.XInverted()
			cube.XInverted()
			break

		#Na
		elif((cube.pos[15] == cube.pos[16] == cube.pos[35]) and (cube.pos[42] == cube.pos[43] == cube.pos[26]) and (cube.pos[33] == cube.pos[34] == cube.pos[17]) and (cube.pos[24] == cube.pos[25] == cube.pos[44])):
			cube.X()
			cube.X()
			cube.Left()
			cube.UpInverted()
			cube.Right()
			cube.Up()
			cube.Up()
			cube.LeftInverted()
			cube.Up()
			cube.RightInverted()
			cube.Left()
			cube.UpInverted()
			cube.Right()
			cube.Up()
			cube.Up()
			cube.LeftInverted()
			cube.Up()
			cube.RightInverted()
			cube.Up()
			cube.XInverted()
			cube.XInverted()

		#Nb
		elif((cube.pos[33] == cube.pos[16] == cube.pos[17]) and (cube.pos[24] == cube.pos[43] == cube.pos[44]) and (cube.pos[15] == cube.pos[34] == cube.pos[35]) and (cube.pos[42] == cube.pos[25] == cube.pos[26])):
			cube.X()
			cube.X()
			cube.RightInverted()
			cube.Up()
			cube.LeftInverted()
			cube.Up()
			cube.Up()
			cube.Right()
			cube.UpInverted()
			cube.Left()
			cube.RightInverted()
			cube.Up()
			cube.LeftInverted()
			cube.Up()
			cube.Up()
			cube.Right()
			cube.UpInverted()
			cube.Left()
			cube.UpInverted()
			cube.XInverted()
			cube.XInverted()

		#Ga
		elif((cube.pos[42] == cube.pos[43] == cube.pos[26]) and (cube.pos[35] == cube.pos[16] == cube.pos[24]) and (cube.pos[15] == cube.pos[34] == cube.pos[17]) and (cube.pos[33] == cube.pos[25] == cube.pos[44])):
			cube.X()
			cube.X()
			cube.Right()
			cube.Right()
			cube.Up()
			cube.EquatorialInverted()
			cube.RightInverted()
			cube.Up()
			cube.RightInverted()
			cube.UpInverted()
			cube.Right()
			cube.UpInverted()
			cube.Equatorial()
			cube.Right()
			cube.Right()
			cube.YInverted()
			cube.RightInverted()
			cube.Up()
			cube.Right()
			cube.Y()
			cube.XInverted()
			cube.XInverted()
			break
			
		#Gb
		elif((cube.pos[15] == cube.pos[16] == cube.pos[26]) and (cube.pos[33] == cube.pos[43] == cube.pos[35]) and (cube.pos[42] == cube.pos[25] == cube.pos[17]) and (cube.pos[24] == cube.pos[34] == cube.pos[44])):
			cube.X()
			cube.X()
			cube.LeftInverted()
			cube.UpInverted()
			cube.Left()
			cube.YInverted()
			cube.Right()
			cube.Right()
			cube.Up()
			cube.EquatorialInverted()
			cube.RightInverted()
			cube.Up()
			cube.Right()
			cube.UpInverted()
			cube.Right()
			cube.UpInverted()
			cube.Equatorial()
			cube.Right()
			cube.Right()
			cube.Y()
			cube.XInverted()
			cube.XInverted()

		#Gc
		elif((cube.pos[25] == cube.pos[26] == cube.pos[42]) and (cube.pos[16] == cube.pos[33] == cube.pos[44]) and (cube.pos[34] == cube.pos[15] == cube.pos[17]) and (cube.pos[43] == cube.pos[35] == cube.pos[24])):
			cube.X()
			cube.X()
			cube.Right()
			cube.Right()
			cube.UpInverted()
			cube.Equatorial()
			cube.Right()
			cube.UpInverted()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.Up()
			cube.EquatorialInverted()
			cube.Right()
			cube.Right()
			cube.Y()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.YInverted()
			cube.XInverted()
			cube.XInverted()

		#Gd
		elif((cube.pos[33] == cube.pos[25] == cube.pos[44]) and (cube.pos[15] == cube.pos[43] == cube.pos[17]) and (cube.pos[24] == cube.pos[34] == cube.pos[35]) and (cube.pos[42] == cube.pos[16] == cube.pos[26])):
			cube.X()
			cube.X()
			cube.Right()
			cube.Up()
			cube.RightInverted()
			cube.YInverted()
			cube.Right()
			cube.Right()
			cube.UpInverted()
			cube.Equatorial()
			cube.Right()
			cube.UpInverted()
			cube.RightInverted()
			cube.Up()
			cube.RightInverted()
			cube.Up()
			cube.EquatorialInverted()
			cube.Right()
			cube.Right()
			cube.Y()
			cube.XInverted()
			cube.XInverted()

		else:
			cube.Down()
	c = 0
	while(c<4):
		c+=1
		if(cube.checkSolve()):break
		cube.Down()