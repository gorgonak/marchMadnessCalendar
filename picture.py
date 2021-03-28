from tkinter import *
from PIL import Image, ImageTk
import time


class Pic:
    def __init__(self, imgname, column, row):

        self.img = imgname
        self.col = column
        self.row = row

        self.image = self.img + ".png"
        self.alt_image = self.img + "_fact.png"
        self.img_src = Image.open("img\\" + self.image)
        self.alt_img_src = Image.open("img\\" + self.alt_image)
        self.pic = ImageTk.PhotoImage(self.img_src)
        self.alt_pic = ImageTk.PhotoImage(self.alt_img_src)

        self.Button = Button(image=self.pic, command=self.big_b)
        self.Button.grid(column=self.col, row=self.row)

    def big_b(self):
        self.Button.destroy()
        print(self.img + ".Button Destroyed")
        self.BigButton = Button(image=self.alt_pic, command=self.little_b)
        self.BigButton.grid(column=self.col, row=self.row)
        print(self.img + " clicked")

    def little_b(self):
        self.BigButton.destroy()
        print(self.img + ".BigButton Destroyed")
        self.Button = Button(image=self.pic, command=self.big_b)
        self.Button.grid(column=self.col, row=self.row)
        print(self.img + " clicked")
