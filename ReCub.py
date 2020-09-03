class ReCub:
    def __init__(self):
        self.pos = ['W','W','W','W','W','W','W','W','W',
        			'R','R','R','R','R','R','R','R','R',
        			'B','B','B','B','B','B','B','B','B',
        			'O','O','O','O','O','O','O','O','O',
        			'G','G','G','G','G','G','G','G','G',
        			'Y','Y','Y','Y','Y','Y','Y','Y','Y']

    #Normal Notations
    def Up(self):
        print("Up")
        temp=self.pos[0]
        self.pos[0]=self.pos[6]
        self.pos[6]=self.pos[8]
        self.pos[8]=self.pos[2]
        self.pos[2]=temp
        temp=self.pos[1]
        self.pos[1]=self.pos[3]
        self.pos[3]=self.pos[7]
        self.pos[7]=self.pos[5]
        self.pos[5]=temp
        temp=self.pos[9]
        self.pos[9]=self.pos[18]
        self.pos[18]=self.pos[27]
        self.pos[27]=self.pos[36]
        self.pos[36]=temp
        temp=self.pos[10]
        self.pos[10]=self.pos[19]
        self.pos[19]=self.pos[28]
        self.pos[28]=self.pos[37]
        self.pos[37]=temp
        temp=self.pos[11]
        self.pos[11]=self.pos[20]
        self.pos[20]=self.pos[29]
        self.pos[29]=self.pos[38]
        self.pos[38]=temp

    def UpInverted(self):
        print("UpInverted")
        temp=self.pos[0]
        self.pos[0]=self.pos[2]
        self.pos[2]=self.pos[8]
        self.pos[8]=self.pos[6]
        self.pos[6]=temp
        temp=self.pos[1]
        self.pos[1]=self.pos[5]
        self.pos[5]=self.pos[7]
        self.pos[7]=self.pos[3]
        self.pos[3]=temp
        temp=self.pos[9]
        self.pos[9]=self.pos[36]
        self.pos[36]=self.pos[27]
        self.pos[27]=self.pos[18]
        self.pos[18]=temp
        temp=self.pos[10]
        self.pos[10]=self.pos[37]
        self.pos[37]=self.pos[28]
        self.pos[28]=self.pos[19]
        self.pos[19]=temp
        temp=self.pos[11]
        self.pos[11]=self.pos[38]
        self.pos[38]=self.pos[29]
        self.pos[29]=self.pos[20]
        self.pos[20]=temp

    def Down(self):
        print("Down")
        temp=self.pos[45]
        self.pos[45]=self.pos[51]
        self.pos[51]=self.pos[53]
        self.pos[53]=self.pos[47]
        self.pos[47]=temp
        temp=self.pos[46]
        self.pos[46]=self.pos[48]
        self.pos[48]=self.pos[52]
        self.pos[52]=self.pos[50]
        self.pos[50]=temp
        temp=self.pos[15]
        self.pos[15]=self.pos[42]
        self.pos[42]=self.pos[33]
        self.pos[33]=self.pos[24]
        self.pos[24]=temp
        temp=self.pos[16]
        self.pos[16]=self.pos[43]
        self.pos[43]=self.pos[34]
        self.pos[34]=self.pos[25]
        self.pos[25]=temp
        temp=self.pos[17]
        self.pos[17]=self.pos[44]
        self.pos[44]=self.pos[35]
        self.pos[35]=self.pos[26]
        self.pos[26]=temp

    def DownInverted(self):
        print("DownInverted")
        temp=self.pos[45]
        self.pos[45]=self.pos[47]
        self.pos[47]=self.pos[53]
        self.pos[53]=self.pos[51]
        self.pos[51]=temp
        temp=self.pos[46]
        self.pos[46]=self.pos[50]
        self.pos[50]=self.pos[52]
        self.pos[52]=self.pos[48]
        self.pos[48]=temp
        temp=self.pos[15]
        self.pos[15]=self.pos[24]
        self.pos[24]=self.pos[33]
        self.pos[33]=self.pos[42]
        self.pos[42]=temp
        temp=self.pos[16]
        self.pos[16]=self.pos[25]
        self.pos[25]=self.pos[34]
        self.pos[34]=self.pos[43]
        self.pos[43]=temp
        temp=self.pos[17]
        self.pos[17]=self.pos[26]
        self.pos[26]=self.pos[35]
        self.pos[35]=self.pos[44]
        self.pos[44]=temp

    def Left(self):
        print("Left")
        temp=self.pos[9]
        self.pos[9]=self.pos[15]
        self.pos[15]=self.pos[17]
        self.pos[17]=self.pos[11]
        self.pos[11]=temp
        temp=self.pos[10]
        self.pos[10]=self.pos[12]
        self.pos[12]=self.pos[16]
        self.pos[16]=self.pos[14]
        self.pos[14]=temp
        temp=self.pos[0]
        self.pos[0]=self.pos[44]
        self.pos[44]=self.pos[45]
        self.pos[45]=self.pos[18]
        self.pos[18]=temp
        temp=self.pos[3]
        self.pos[3]=self.pos[41]
        self.pos[41]=self.pos[48]
        self.pos[48]=self.pos[21]
        self.pos[21]=temp
        temp=self.pos[6]
        self.pos[6]=self.pos[38]
        self.pos[38]=self.pos[51]
        self.pos[51]=self.pos[24]
        self.pos[24]=temp

    def LeftInverted(self):
        print("LeftInverted")
        temp=self.pos[9]
        self.pos[9]=self.pos[11]
        self.pos[11]=self.pos[17]
        self.pos[17]=self.pos[15]
        self.pos[15]=temp
        temp=self.pos[10]
        self.pos[10]=self.pos[14]
        self.pos[14]=self.pos[16]
        self.pos[16]=self.pos[12]
        self.pos[12]=temp
        temp=self.pos[0]
        self.pos[0]=self.pos[18]
        self.pos[18]=self.pos[45]
        self.pos[45]=self.pos[44]
        self.pos[44]=temp
        temp=self.pos[3]
        self.pos[3]=self.pos[21]
        self.pos[21]=self.pos[48]
        self.pos[48]=self.pos[41]
        self.pos[41]=temp
        temp=self.pos[6]
        self.pos[6]=self.pos[24]
        self.pos[24]=self.pos[51]
        self.pos[51]=self.pos[38]
        self.pos[38]=temp

    def Right(self):
        print("Right")
        temp=self.pos[27]
        self.pos[27]=self.pos[33]
        self.pos[33]=self.pos[35]
        self.pos[35]=self.pos[29]
        self.pos[29]=temp
        temp=self.pos[28]
        self.pos[28]=self.pos[30]
        self.pos[30]=self.pos[34]
        self.pos[34]=self.pos[32]
        self.pos[32]=temp
        temp=self.pos[2]
        self.pos[2]=self.pos[20]
        self.pos[20]=self.pos[47]
        self.pos[47]=self.pos[42]
        self.pos[42]=temp
        temp=self.pos[5]
        self.pos[5]=self.pos[23]
        self.pos[23]=self.pos[50]
        self.pos[50]=self.pos[39]
        self.pos[39]=temp
        temp=self.pos[8]
        self.pos[8]=self.pos[26]
        self.pos[26]=self.pos[53]
        self.pos[53]=self.pos[36]
        self.pos[36]=temp

    def RightInverted(self):
        print("RightInverted")
        temp=self.pos[27]
        self.pos[27]=self.pos[29]
        self.pos[29]=self.pos[35]
        self.pos[35]=self.pos[33]
        self.pos[33]=temp
        temp=self.pos[28]
        self.pos[28]=self.pos[32]
        self.pos[32]=self.pos[34]
        self.pos[34]=self.pos[30]
        self.pos[30]=temp
        temp=self.pos[2]
        self.pos[2]=self.pos[42]
        self.pos[42]=self.pos[47]
        self.pos[47]=self.pos[20]
        self.pos[20]=temp
        temp=self.pos[5]
        self.pos[5]=self.pos[39]
        self.pos[39]=self.pos[50]
        self.pos[50]=self.pos[23]
        self.pos[23]=temp
        temp=self.pos[8]
        self.pos[8]=self.pos[36]
        self.pos[36]=self.pos[53]
        self.pos[53]=self.pos[26]
        self.pos[26]=temp

    def Front(self):
        print("Front")
        temp=self.pos[18]
        self.pos[18]=self.pos[24]
        self.pos[24]=self.pos[26]
        self.pos[26]=self.pos[20]
        self.pos[20]=temp
        temp=self.pos[19]
        self.pos[19]=self.pos[21]
        self.pos[21]=self.pos[25]
        self.pos[25]=self.pos[23]
        self.pos[23]=temp
        temp=self.pos[6]
        self.pos[6]=self.pos[17]
        self.pos[17]=self.pos[47]
        self.pos[47]=self.pos[27]
        self.pos[27]=temp
        temp=self.pos[7]
        self.pos[7]=self.pos[14]
        self.pos[14]=self.pos[46]
        self.pos[46]=self.pos[30]
        self.pos[30]=temp
        temp=self.pos[8]
        self.pos[8]=self.pos[11]
        self.pos[11]=self.pos[45]
        self.pos[45]=self.pos[33]
        self.pos[33]=temp

    def FrontInverted(self):
        print("FrontInverted")
        temp=self.pos[18]
        self.pos[18]=self.pos[20]
        self.pos[20]=self.pos[26]
        self.pos[26]=self.pos[24]
        self.pos[24]=temp
        temp=self.pos[19]
        self.pos[19]=self.pos[23]
        self.pos[23]=self.pos[25]
        self.pos[25]=self.pos[21]
        self.pos[21]=temp
        temp=self.pos[6]
        self.pos[6]=self.pos[27]
        self.pos[27]=self.pos[47]
        self.pos[47]=self.pos[17]
        self.pos[17]=temp
        temp=self.pos[7]
        self.pos[7]=self.pos[30]
        self.pos[30]=self.pos[46]
        self.pos[46]=self.pos[14]
        self.pos[14]=temp
        temp=self.pos[8]
        self.pos[8]=self.pos[33]
        self.pos[33]=self.pos[45]
        self.pos[45]=self.pos[11]
        self.pos[11]=temp

    def Back(self):
        print("Back")
        temp=self.pos[36]
        self.pos[36]=self.pos[42]
        self.pos[42]=self.pos[44]
        self.pos[44]=self.pos[38]
        self.pos[38]=temp
        temp=self.pos[37]
        self.pos[37]=self.pos[39]
        self.pos[39]=self.pos[43]
        self.pos[43]=self.pos[41]
        self.pos[41]=temp
        temp=self.pos[0]
        self.pos[0]=self.pos[29]
        self.pos[29]=self.pos[53]
        self.pos[53]=self.pos[15]
        self.pos[15]=temp
        temp=self.pos[1]
        self.pos[1]=self.pos[32]
        self.pos[32]=self.pos[52]
        self.pos[52]=self.pos[12]
        self.pos[12]=temp
        temp=self.pos[2]
        self.pos[2]=self.pos[35]
        self.pos[35]=self.pos[51]
        self.pos[51]=self.pos[9]
        self.pos[9]=temp

    def BackInverted(self):
        print("BackInverted")
        temp=self.pos[36]
        self.pos[36]=self.pos[38]
        self.pos[38]=self.pos[44]
        self.pos[44]=self.pos[42]
        self.pos[42]=temp
        temp=self.pos[37]
        self.pos[37]=self.pos[41]
        self.pos[41]=self.pos[43]
        self.pos[43]=self.pos[39]
        self.pos[39]=temp
        temp=self.pos[0]
        self.pos[0]=self.pos[15]
        self.pos[15]=self.pos[53]
        self.pos[53]=self.pos[29]
        self.pos[29]=temp
        temp=self.pos[1]
        self.pos[1]=self.pos[12]
        self.pos[12]=self.pos[52]
        self.pos[52]=self.pos[32]
        self.pos[32]=temp
        temp=self.pos[2]
        self.pos[2]=self.pos[9]
        self.pos[9]=self.pos[51]
        self.pos[51]=self.pos[35]
        self.pos[35]=temp

    #Slice Notations
    def Middle(self):
        print("Middle")
        temp=self.pos[1]
        self.pos[1]=self.pos[43]
        self.pos[43]=self.pos[46]
        self.pos[46]=self.pos[19]
        self.pos[19]=temp
        temp=self.pos[4]
        self.pos[4]=self.pos[40]
        self.pos[40]=self.pos[49]
        self.pos[49]=self.pos[22]
        self.pos[22]=temp
        temp=self.pos[7]
        self.pos[7]=self.pos[37]
        self.pos[37]=self.pos[52]
        self.pos[52]=self.pos[25]
        self.pos[25]=temp

    def MiddleInverted(self):
        print("MiddleInverted")
        temp=self.pos[1]
        self.pos[1]=self.pos[19]
        self.pos[19]=self.pos[46]
        self.pos[46]=self.pos[43]
        self.pos[43]=temp
        temp=self.pos[4]
        self.pos[4]=self.pos[22]
        self.pos[22]=self.pos[49]
        self.pos[49]=self.pos[40]
        self.pos[40]=temp
        temp=self.pos[7]
        self.pos[7]=self.pos[25]
        self.pos[25]=self.pos[52]
        self.pos[52]=self.pos[37]
        self.pos[37]=temp

    def Equatorial(self):
        print("Equatorial")
        temp=self.pos[12]
        self.pos[12]=self.pos[39]
        self.pos[39]=self.pos[30]
        self.pos[30]=self.pos[21]
        self.pos[21]=temp
        temp=self.pos[13]
        self.pos[13]=self.pos[40]
        self.pos[40]=self.pos[31]
        self.pos[31]=self.pos[22]
        self.pos[22]=temp
        temp=self.pos[14]
        self.pos[14]=self.pos[41]
        self.pos[41]=self.pos[32]
        self.pos[32]=self.pos[23]
        self.pos[23]=temp

    def EquatorialInverted(self):
        print("EquatorialInverted")
        temp=self.pos[12]
        self.pos[12]=self.pos[21]
        self.pos[21]=self.pos[30]
        self.pos[30]=self.pos[39]
        self.pos[39]=temp
        temp=self.pos[13]
        self.pos[13]=self.pos[22]
        self.pos[22]=self.pos[31]
        self.pos[31]=self.pos[40]
        self.pos[40]=temp
        temp=self.pos[14]
        self.pos[14]=self.pos[23]
        self.pos[23]=self.pos[32]
        self.pos[32]=self.pos[41]
        self.pos[41]=temp

    def Standing(self):
        print("Standing")
        temp=self.pos[3]
        self.pos[3]=self.pos[16]
        self.pos[16]=self.pos[50]
        self.pos[50]=self.pos[28]
        self.pos[28]=temp
        temp=self.pos[4]
        self.pos[4]=self.pos[13]
        self.pos[13]=self.pos[49]
        self.pos[49]=self.pos[31]
        self.pos[31]=temp
        temp=self.pos[5]
        self.pos[5]=self.pos[10]
        self.pos[10]=self.pos[48]
        self.pos[48]=self.pos[34]
        self.pos[34]=temp

    def StandingInverted(self):
        print("StandingInverted")
        temp=self.pos[3]
        self.pos[3]=self.pos[28]
        self.pos[28]=self.pos[50]
        self.pos[50]=self.pos[16]
        self.pos[16]=temp
        temp=self.pos[4]
        self.pos[4]=self.pos[31]
        self.pos[31]=self.pos[49]
        self.pos[49]=self.pos[13]
        self.pos[13]=temp
        temp=self.pos[5]
        self.pos[5]=self.pos[34]
        self.pos[34]=self.pos[48]
        self.pos[48]=self.pos[10]
        self.pos[10]=temp


    #Entire Cube Rotation Notations
    def X(self):
        self.Right()
        self.MiddleInverted()
        self.LeftInverted()

    def XInverted(self):
        self.RightInverted()
        self.Middle()
        self.Left()

    def Y(self):
        self.Up()
        self.EquatorialInverted()
        self.DownInverted()

    def YInverted(self):
        self.UpInverted()
        self.Equatorial()
        self.Down()

    def Z(self):
        self.Front()
        self.Standing()
        self.BackInverted()

    def ZInverted(self):
        self.FrontInverted()
        self.StandingInverted()
        self.Back()

    def print(self):
        for square in self.pos:
        	print(square, end="")
        print()

    def checkSolve(self):
        return self.pos == ['W','W','W','W','W','W','W','W','W',
                            'R','R','R','R','R','R','R','R','R',
                            'B','B','B','B','B','B','B','B','B',
                            'O','O','O','O','O','O','O','O','O',
                            'G','G','G','G','G','G','G','G','G',
                            'Y','Y','Y','Y','Y','Y','Y','Y','Y']