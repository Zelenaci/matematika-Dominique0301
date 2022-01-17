#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Kalkulačka")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Konec", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.about)
        self.btn2.pack()
        self.btn3 = tk.Button(self, text="Kontrola", command=self.kontrola)


    def plus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,100-self.cisloA)#aby vysledek nebyl větší než 100
        self.vysledek = self.cisloA + self.cisloB
        self.lbl.config(text="+")


    def minus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,99)
        if self.cisloB > self.cisloB:
            self.cisloA, self.cisloB = self.cisloB, self.cisloA
        self.vysledek == self.cisloA - self.cisloB
        self.lbl.config(text="-")



    def krat(self):
        self.cisloA = random.randint(1,10)
        self.cisloB = random.randint(1,10)
        self.vysledek = self.cisloA * self.cisloB
        self.lbl.config(text="*")


    def deleno(self):
        self.vysledek = random.randint(1,9)
        self.cisloB = random.randint(1,9)
        self.cisloA = self.vysledek * self.cisloB
        self.lbl.config(text="/")

    def generuj(self):
        funkce = random.choice([self.plus,self.minus,self.krat,self.deleno])
        funkce()



    def kontrola(self):
        







    def about(self):
        self.generuj()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
