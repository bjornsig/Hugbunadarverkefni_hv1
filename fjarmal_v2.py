#!/usr/bin/env python
# encoding: utf-8

import Tkinter as tk
import tkMessageBox
import matplotlib as mpl
import ttk
import sparigui
mpl.use('TkAgg')
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

SPARI_VEXTIR = 1.035

class Graf(tk.LabelFrame):
    def __init__(self, parent, bg):
        tk.LabelFrame.__init__(self, parent, background=bg, text='Graf', padx=4, pady=4)

        f = Figure(figsize=(4,4), dpi=50)
        self.a = f.add_subplot(111)
        #t = arange(0.0,3.0,0.01)
        #s = sin(2*pi*t)


        self.canvas = FigureCanvasTkAgg(f, master=self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    def teikna_a_graf(self, x, y):
        self.a.plot(x,y)
        self.canvas.show()


class Sparispurn(tk.LabelFrame):
    def __init__(self, parent, teikna_a_graf, bg):
        tk.LabelFrame.__init__(self, parent, background=bg, text='Sparnaður', padx=4, pady=4)
        self.teikna_a_graf = teikna_a_graf


        self.spari1 = tk.Label(self, text='Ég get lagt fyrir')
        self.spari2 = tk.Label(self, text='kr. á mánuði.')
        self.hvad_a_eg = tk.Entry(self)
        self.spari1.grid(column=0,row=0,sticky=tk.E)
        self.hvad_a_eg.grid(column=1,row=0)
        self.spari2.grid(column=2,row=0,sticky=tk.W)


        self.kronur1 = tk.Label(self, text='Hvað tekur það mig langan tíma að safna')
        self.kronur2 = tk.Label(self, text='kr.?')
        self.safna1 = tk.Entry(self)
        self.kronur1.grid(column=0,row=1,sticky=tk.E)
        self.safna1.grid(column=1,row=1)
        self.kronur2.grid(column=2,row=1,sticky=tk.W)
        self.spari_takki1 = tk.Button(self, text='Reikna', command=self.reikna_spari).grid(column=3,row=1)


        self.kronur3 = tk.Label(self, text='Hvað mun ég eiga mikinn pening eftir')
        self.kronur4 = tk.Label(self, text='mánuði?')
        self.safna2 = tk.Entry(self)
        self.kronur3.grid(column=0,row=2,sticky=tk.E)
        self.safna2.grid(column=1,row=2)
        self.kronur4.grid(column=2,row=2,sticky=tk.W)
        self.spari_takki2 = tk.Button(self, text='Reikna', command=self.reikna_pening).grid(column=3,row=2)

    def teikna(self):
        x = range(0,5)
        y = []
        temp = float(self.hvad_a_eg.get())
        for i in x:
            temp = temp + temp*SPARI_VEXTIR
            y.append(temp)
        self.teikna_a_graf(x,y)

    def reikna_spari(self):
        eg_a = int(self.hvad_a_eg.get())
        eg_vil = int(self.safna1.get())
        svar = eg_vil / ( eg_a * SPARI_VEXTIR )
        tkMessageBox.showinfo('Sparnaður', 'Það tekur ' + str(int(round(svar))) + ' marga mánuði.')

    def reikna_pening(self):
        eg_a = int(self.hvad_a_eg.get())
        eftir_tima = int(self.safna2.get())
        svar = eg_a * SPARI_VEXTIR * eftir_tima
        tkMessageBox.showinfo('Sparnaður', 'Þú munt eiga ' + str(int(round(svar))) + ' kr.')


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
        self.heiti = tk.Entry(self, width=50)
        self.heiti.grid(row=0,column=1)
        self.timabil = tk.Entry(self, width=10)
        self.timabil.grid(row=0,column=3)
        self.vextir = tk.Entry(self, width=10)
        self.vextir.grid(row=0,column=2)

    def fa_vexti(self):
        return float(self.vextir.get())

    def fa_nafn(self):
        return self.heiti.get()


class Lanagluggi(tk.LabelFrame):
    def __init__(self, parent, bg):
        tk.LabelFrame.__init__(self, parent, background=bg, text='Lán', padx=4, pady=4)
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

    def fa_topp_vexti(self):
        toppur = self.lanasafn[0]
        for i in self.lanasafn:
            if i.fa_vexti() > toppur.fa_vexti():
                toppur = i
        if toppur.fa_vexti() > SPARI_VEXTIR:
            return toppur.fa_nafn()
        else:
            return 'Vaxtasproti'


class Takkar(tk.Frame):
    def __init__(self, parent, nytt_lan, taka_ut_lan, fa_topp_vexti, teikna_a_graf):
        tk.Frame.__init__(self, parent)
        self.fa_topp_vexti = fa_topp_vexti
        self.teikna_a_graf = teikna_a_graf
        self.meira = tk.Button(self, text='Bæta við láni', command=nytt_lan).pack(side=tk.LEFT, fill='both', expand='True')
        self.minna = tk.Button(self, text='Fjarlægja lán', command=taka_ut_lan).pack(side=tk.LEFT, fill='both', expand='True')
        self.teikna = tk.Button(self, text='Teikna', command=self.teikna).pack(side=tk.LEFT, fill='both', expand='True')

    def teikna(self):
        vextir = self.fa_topp_vexti()
        tkMessageBox.showinfo('Sparnaður', 'Hagstæðast er að borga í ' + vextir)
        self.teikna_a_graf()



class Grunnur(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.vidmot()

    def vidmot(self):
        self.graf = Graf(self,bg='lightgray')
        self.sparispurn = Sparispurn(self,
            self.graf.teikna_a_graf,
            bg='lightgray'
            )
        self.sparispurn.pack(side=tk.TOP,fill='both')
        self.lanagluggi = Lanagluggi(self, bg='lightgray')
        self.lanagluggi.pack(side=tk.TOP, fill='x', expand=True)
        Takkar(self,
            self.lanagluggi.nytt_lan,
            self.lanagluggi.taka_ut_lan,
            self.lanagluggi.fa_topp_vexti,
            self.sparispurn.teikna
            ).pack(side=tk.TOP, fill='both')
        self.graf.pack(side=tk.BOTTOM, fill='both', expand=True)


def main():
    root = tk.Tk()
    root.wm_title('Besta forrit í heimi!')
    app = Grunnur(root)
    app.pack(fill='both', expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
