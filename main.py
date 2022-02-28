from os.path import basename, splitext
import tkinter as tk
import random
from tkinter.constants import END

# from typing_extensions import IntVar
from xml.dom.minidom import Entity

# from tkinter import ttk
# Dominik Šlehofer


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Matematická Hra"
    # tk.geometry(150*200)

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="")
        self.generuj()
        self.vysledek_vstup = tk.Entry(self)
        self.vysledek_vstup.grid(row=3, column=1)
        self.lbl_hodnoceni = tk.Label(self, text="")
        self.lbl_hodnoceni.grid(row=4, column=1)
        self.btn3 = tk.Button(self, text="Kontrola", command=self.kontrola)
        self.btn3.grid(row=5, column=1)

    def plus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(
            1, 100 - self.cisloA
        )  # aby vysledek nebyl větší než 100
        self.vysledek = self.cisloA + self.cisloB
        return str(self.cisloA) + "+" + str(self.cisloB)

    def minus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, self.cisloA)
        self.vysledek = self.cisloA - self.cisloB
        return str(self.cisloA) + "-" + str(self.cisloB)

    def krat(self):
        self.cisloA = random.randint(1, 10)
        self.cisloB = random.randint(1, 10)
        self.vysledek = self.cisloA * self.cisloB
        return str(self.cisloA) + "*" + str(self.cisloB)

    def deleno(self):
        self.vysledek = random.randint(1, 10)
        self.cisloB = random.randint(1, 10)
        self.cisloA = self.vysledek * self.cisloB
        return str(self.cisloA) + "/" + str(self.cisloB)

    def generuj(self):
        self.funkce = random.choice([self.plus, self.minus, self.krat, self.deleno])
        self.priklad = self.funkce()
        self.lbl.config(text=self.priklad)
        self.lbl.grid(row=1, column=1)

    def kontrola(self):
        try:
            vysledek = int(self.vysledek_vstup.get())
        except ValueError:
            vysledek = None
            return

        if vysledek == int(self.vysledek):
            self.lbl_hodnoceni.config(text="SPRÁVNĚ")
        else:
            self.lbl_hodnoceni.config(text="ŠPATNĚ")
        self.generuj()
        self.vysledek_vstup.delete(0, END)


app = Application()
app.mainloop()
