#!/usr/bin/env python
# encoding: utf-8

import Tkinter as tk
import matplotlib as mpl
import ttk
import sparigui
mpl.use('TkAgg')
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

class Graf(tk.LabelFrame):
    def __init__(self, parent, bg):
        tk.LabelFrame.__init__(self, parent, background=bg, text='Graf', padx=4, pady=4)

        f = Figure(figsize=(4,4), dpi=50)
        a = f.add_subplot(111)
        t = arange(0.0,3.0,0.01)
        s = sin(2*pi*t)

        a.plot(t,s)

        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)


class Merki(tk.Frame):
    def __init__(self, parent, bg):
        tk.Frame.__init__(self, parent, background=bg)
        tk.Label(self, text='Verðtryggt').grid(row=0,column=0)
        tk.Label(self, text='Heiti láns').grid(row=0,column=1)
        tk.Label(self, text='Vextir').grid(row=0,column=2)
        tk.Label(self, text='Tímabil').grid(row=0,column=3)
        self.columnconfigure(1,weight=3)
        self.columnconfigure(2,weight=1)

class Lan(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.form()

    def form(self):
        self.tryggt = tk.Checkbutton(self)
        self.tryggt.grid(row=0,column=0)
        self.heiti = tk.Entry(self, width=50).grid(row=0,column=1)
        self.timabil = tk.Entry(self, width=10).grid(row=0,column=2)
        self.vextir = ttk.Combobox(self, state='readonly', width=10, values=['hallo','bless']).grid(row=0,column=3)

    def fa_vexti(self):
        return self.vextir

    
class Lanagluggi(tk.LabelFrame):
    def __init__(self, parent, bg):
        tk.LabelFrame.__init__(self, parent, background=bg, text='Fullt af lanum', padx=4, pady=4)
        Merki(self, bg='lightgray').pack(side=tk.TOP, fill='both')
        self.lanasafn = []
        lan = Lan(self)
        lan.pack(side=tk.TOP)
        self.lanasafn.append(lan)

    def nytt_lan(self):
        if len(self.lanasafn) < 6:
            lan = Lan(self)
            lan.pack(side=tk.TOP)
            self.lanasafn.append(lan)

    def taka_ut_lan(self):
        if len(self.lanasafn) > 1:
            lan = self.lanasafn.pop()
            lan.pack_forget()
            lan.destroy()

class Takkar(tk.Frame):
    def __init__(self, parent, nytt_lan, taka_ut_lan):
        tk.Frame.__init__(self, parent)
        self.meira = tk.Button(self, text='+', command=nytt_lan).pack(side=tk.LEFT, fill='both', expand='True')
        self.minna = tk.Button(self, text='-', command=taka_ut_lan).pack(side=tk.LEFT, fill='both', expand='True')
        self.teikna = tk.Button(self, text='Teikna').pack(side=tk.LEFT, fill='both', expand='True')

class Grunnur(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.vidmot()

    def vidmot(self):
        self.lanagluggi = Lanagluggi(self, bg='lightgray')
        self.lanagluggi.pack(side=tk.TOP, fill='x', expand=True)
        sparigui.sparnadur(self,bg='lightgray').pack(side=tk.TOP, fill='both')
        Takkar(self, self.lanagluggi.nytt_lan, self.lanagluggi.taka_ut_lan).pack(side=tk.TOP, fill='both')
        Graf(self,bg='lightgray').pack(side=tk.BOTTOM, fill='both', expand=True)

def main():
    root = tk.Tk()
    root.wm_title('Besta forrit í heimi!')
    app = Grunnur(root)
    app.pack(fill='both', expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
