# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

class sparnadur(tk.LabelFrame):

	def __init__(self, foreldri, bg):

		tk.LabelFrame.__init__(self, foreldri, background=bg, text='Sparnadur', padx=4, pady=4)
		self.sparileidir = [('Vaxtasproti',0.036,0), ('Vaxtathrep',0.043,1)]
		self.form()


	def form(self):

		rammi = tk.Frame(self)

		spari = tk.Label(rammi, text='Sparnaður')
		spari.grid(column=0, row=0)

		self.sparnadur = tk.Entry(rammi)
		self.sparnadur.grid(column=0, row=1)

		timi = tk.Label(rammi, text='Tímabil')
		timi.grid(column=1, row=0)

		self.lengd = tk.Entry(rammi)
		self.lengd.grid(column=1, row=1)

		moguleikar = ttk.Combobox(rammi, state='readonly')
		moguleikar['values'] = (self.sparileidir[0][0],self.sparileidir[1][0])

		moguleikar.grid(column=2,row=1)

                self.kronur1 = tk.Label(rammi, text='Hvað tekur það mig langan tíma að safna')
                self.kronur2 = tk.Label(rammi, text='kr.')
                self.safna = tk.Entry(rammi)
                self.kronur1.grid(column=0,row=2,columnspan=1,sticky=tk.E)
                self.safna.grid(column=1,row=2)
                self.kronur2.grid(column=2,row=2,sticky=tk.W)

                rammi.pack(side=tk.TOP)


