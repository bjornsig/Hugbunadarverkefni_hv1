#!/usr/bin/env python
# encoding: utf-8

import Tkinter as tk
import tkMessageBox
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

SPARI_VEXTIR = 1.035
BACKGROUND = 'lightgray'

class Graf(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text='Graf', padx=4, pady=4)

        f = Figure(figsize=(4,4), dpi=50)
        self.a = f.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(f, master=self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    def teikna_a_graf(self, x, y):
        self.a.plot(x,y)
        self.canvas.show()


class Sparnadur(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text='Sparnaður', padx=4, pady=4)
        self.upphaed = tk.Entry(self)
        self.timabil = tk.Entry(self)
        self.timi_fyrir_peninga = tk.Entry(self)
        self.takki_timi = tk.Button(self, text='Reikna')
        self.takki_peningar = tk.Button(self, text='Reikna')

        self.vidmot_spari()
        self.vidmot_peningar()
        self.vidmot_timi()

    def vidmot_spari(self):
        tk.Label(self, text='Ég get lagt fyrir').grid(column=0,row=0,sticky=tk.E)
        self.upphaed.grid(column=1,row=0)
        tk.Label(self, text='kr. á mánuði').grid(column=2,row=0,sticky=tk.W)
        tk.Label(self, text='í').grid(column=0,row=1,sticky=tk.E)
        self.timabil.grid(column=1,row=1)
        tk.Label(self, text='mánuði.').grid(column=2,row=1,sticky=tk.W)

    def vidmot_peningar(self):
        tk.Label(self, text='Hvað mun ég eiga mikinn pening eftir þennan tíma?').grid(
                column=0,row=2, columnspan=3,sticky=tk.E)
        self.takki_peningar.grid(column=3,row=2)

    def vidmot_timi(self):
        tk.Label(self, text='Hvað tekur það mig langan tíma að safna').grid(
                column=0,row=3,sticky=tk.E)
        self.timi_fyrir_peninga.grid(column=1,row=3)
        tk.Label(self, text='kr.?').grid(column=2,row=3,sticky=tk.W)
        self.takki_timi.grid(column=3,row=3)


class Lan(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.tryggt = tk.Button(self, text='Nei')
        self.heiti = tk.Entry(self, width=50)
        self.upphaed = tk.Entry(self, width=20)
        self.vextir = tk.Entry(self, width=10)
        self.timabil = tk.Entry(self, width=10)

        self.vidmot()

    def vidmot(self):
        self.tryggt.grid(row=0,column=0)
        self.upphaed.grid(row=0,column=1)
        self.heiti.grid(row=0,column=2)
        self.vextir.grid(row=0,column=3)
        self.timabil.grid(row=0,column=4)

    def fa_vexti(self):
        return float(self.vextir.get())

    def fa_nafn(self):
        return self.heiti.get()

    def fa_upphaed(self):
        return int(self.upphaed.get())

    def fa_timabil(self):
        return int(self.timabil.get())


class Lanasafn(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text='Lán', padx=4, pady=4)
        self.vidmot().pack(side=tk.TOP, fill='both')
        self.bunki = []
        lan = Lan(self)
        lan.pack(side=tk.TOP)
        self.bunki.append(lan)

    def vidmot(self):
        merki = tk.Frame(self)
        tk.Label(merki, text='Verðtryggt').grid(row=0,column=0)
        tk.Label(merki, text='Upphæð').grid(row=0,column=1)
        tk.Label(merki, text='Heiti láns').grid(row=0,column=2)
        tk.Label(merki, text='Vextir').grid(row=0,column=3)
        tk.Label(merki, text='Tímabil').grid(row=0,column=4)
        merki.columnconfigure(1,weight=2)
        merki.columnconfigure(2,weight=3)
        merki.columnconfigure(3,weight=1)
        return merki

    def nytt_lan(self):
        if len(self.bunki) < 6:
            lan = Lan(self)
            lan.pack(side=tk.TOP)
            self.bunki.append(lan)

    def taka_ut_lan(self):
        if len(self.bunki) > 1:
            lan = self.bunki.pop()
            lan.pack_forget()
            lan.destroy()


class Takkar(tk.Frame):
    def __init__(self, foreldri):
        tk.Frame.__init__(self, foreldri)
        self.meira = tk.Button(self, text='Bæta við láni')
        self.minna = tk.Button(self, text='Fjarlægja lán')
        self.hvad = tk.Button(self, text='Hvað á ég að gera?')
        self.teikna = tk.Button(self, text='Teikna')
        self.vidmot()

    def vidmot(self):
        self.meira.pack(side=tk.LEFT, fill='both', expand='True')
        self.minna.pack(side=tk.LEFT, fill='both', expand='True')
        self.hvad.pack(side=tk.LEFT, fill='both', expand='True')
        self.teikna.pack(side=tk.LEFT, fill='both', expand='True')


class Reikningur:
    def __init__(self, graf, sparnadur, lanasafn, takkar):
        self.graf = graf
        self.sparnadur = sparnadur
        self.lanasafn = lanasafn
        self.takkar = takkar

        self.virkni_takkar()
        self.virkni_sparnadur()

    def virkni_takkar(self):
        self.takkar.meira.config(command=self.lanasafn.nytt_lan)
        self.takkar.minna.config(command=self.lanasafn.taka_ut_lan)
        self.takkar.hvad.config(command=self.bera_saman_vexti)
        self.takkar.teikna.config(command=self.teikna)

    def bera_saman_vexti(self):
        vextir = self.fa_topp_vexti(self.lanasafn.bunki)
        tkMessageBox.showinfo('Sparnaður', 'Hagstæðast er að borga í ' + vextir)

    def virkni_sparnadur(self):
        self.sparnadur.takki_timi.config(command=self.sparnadur_timi)
        self.sparnadur.takki_peningar.config(command=self.sparnadur_peningar)

    def sparnadur_timi(self):
        eg_a = int(self.sparnadur.upphaed.get())
        eg_vil = int(self.sparnadur.timi_fyrir_peninga.get())
        svar = eg_vil / ( eg_a * SPARI_VEXTIR )
        tkMessageBox.showinfo('Sparnaður', 'Það tekur ' + str(int(round(svar))) + ' marga mánuði að safna því ef þú notar Vaxtasprota.')

    def sparnadur_peningar(self):
        eg_a = int(self.sparnadur.upphaed.get())
        timi = int(self.sparnadur.timabil.get())
        svar = eg_a * SPARI_VEXTIR * timi
        tkMessageBox.showinfo('Sparnaður', 'Þú munt eiga ' + str(int(round(svar))) + ' kr.')

    def fa_topp_lan(self, bunki):
        toppur = bunki[0]
        for i in bunki:
            if i.fa_vexti() > toppur.fa_vexti():
                toppur = i
        return toppur

    def fa_topp_vexti(self, bunki):
        lan = self.fa_topp_lan(bunki)
        if lan[1] > SPARI_VEXTIR:
            return lan[0]
        else:
            return 'Vaxtasproti'

    def teikna(self):
        lan = self.fa_topp_lan(self.lanasafn.bunki)
        timi_lan = lan.fa_timabil()
        timi_spari = int(self.sparnadur.timabil.get())
        upphaed = lan.fa_upphaed() * (lan.fa_vexti() / 100 + 1)
        spari = int(self.sparnadur.upphaed.get())
        manadarleg_greidsla = upphaed / timi_lan
        x = range(0,timi_spari+1)
        y_lan = [upphaed]
        y_spari = [upphaed]
        for i in x[:-1]:
            y_lan.append(y_lan[i] - manadarleg_greidsla)
            y_spari.append(y_spari[i] - spari*SPARI_VEXTIR - manadarleg_greidsla)
        print(len(x),len(y_lan))
        self.graf.teikna_a_graf(x,y_lan)
        self.graf.teikna_a_graf(x,y_spari)


class Grunnur(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.graf = Graf(self)
        self.sparnadur = Sparnadur(self)
        self.lanasafn= Lanasafn(self)
        self.takkar = Takkar(self)
        self.reikningur = Reikningur(self.graf, self.sparnadur, self.lanasafn , self.takkar)

        self.vidmot()

    def vidmot(self):
        self.sparnadur.pack(side=tk.TOP,fill='both')
        self.lanasafn.pack(side=tk.TOP, fill='x', expand=True)
        self.takkar.pack(side=tk.TOP, fill='both')
        self.graf.pack(side=tk.BOTTOM, fill='both', expand=True)


def main():
    root = tk.Tk()
    root.wm_title('Besta forrit í heimi!')
    app = Grunnur(root)
    app.pack(fill='both', expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
