from tkinter import *
import CSS
#from PIL import Image, ImageTk

def About():
	AboutWindow = Tk()
	AboutWindow.config(background = CSS.BACKGROUND)
	AboutWindow.geometry("250x170")

	projectLabel = Label(AboutWindow, text = "Cube", font = "Arial, 30", background = CSS.BACKGROUND)
	projectLabel.pack()

	AmoghLabel = Label(AboutWindow, text = "Amogh Chauhan", font = "Arial, 10", background = CSS.BACKGROUND)
	AmoghLabel.pack()
	PrajaktaLabel = Label(AboutWindow, text = "Prajakta Dhumal", font = "Arial, 10", background = CSS.BACKGROUND)
	PrajaktaLabel.pack()
	YashLabel = Label(AboutWindow, text = "Yash Eksambekar", font = "Arial, 10", background = CSS.BACKGROUND)
	YashLabel.pack()
	KadambariLabel = Label(AboutWindow, text = "Kadambari Mane", font = "Arial, 10", background = CSS.BACKGROUND)
	KadambariLabel.pack()
	MohitLabel = Label(AboutWindow, text = "Mohit Sarode", font = "Arial, 10", background = CSS.BACKGROUND)
	MohitLabel.pack()

	AboutWindow.mainloop()
'''
def Notations():
	NotationWindow = Tk()
	NotationWindow.config(background = CSS.BACKGROUND)

	Single_Layer_Rotation_Image = Image.open("./images/Notations/Single_Layer_Rotation.png")
	Single_Layer_Rotation_Render = ImageTk.PhotoImage(Single_Layer_Rotation_Image)
	Single_Layer_Rotation_Label = Label(NotationWindow, image = Single_Layer_Rotation_Render)
	Single_Layer_Rotation_Label.pack()

	NotationWindow.mainloop()
'''