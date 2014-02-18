#!/usr/bin/env python
# encoding: utf-8

import Tkinter as tk
import tkMessageBox
import verdbolga
#import matplotlib as mpl
#mpl.use('TkAgg')
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re

SPARI_VEXTIR = 1.035
BACKGROUND = 'lightgray'

#class Graf(tk.LabelFrame):
#    def __init__(self, parent):
#        tk.LabelFrame.__init__(self, parent, text='Graf', padx=4, pady=4)

#        f = Figure(figsize=(4,4), dpi=50)
#        self.a = f.add_subplot(111)

#        self.canvas = FigureCanvasTkAgg(f, master=self)
#        self.canvas.show()
#        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

#        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

#    def teikna_a_graf(self, x, y):
#        self.a.plot(x,y)
#        self.canvas.show()


class Sparnadur(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text='Sparnaður', padx=4, pady=4)
        self.upphaed = tk.Entry(self)
        self.timi_fyrir_peninga = tk.Entry(self)
        self.takki_timi = tk.Button(self, text='Reikna')
        self.peningar_eftir_tima = tk.Entry(self)
        self.takki_peningar = tk.Button(self, text='Reikna')

        self.vidmot_spari()
        self.vidmot_timi()
        self.vidmot_peningar()

    def vidmot_spari(self):
        tk.Label(self, text='Ég get lagt fyrir').grid(column=0,row=0,sticky=tk.E)
        self.upphaed.grid(column=1,row=0)
        tk.Label(self, text='kr. á mánuði.').grid(column=2,row=0,sticky=tk.W)

    def vidmot_timi(self):
        tk.Label(self, text='Hvað tekur það mig langan tíma að safna').grid(
                column=0,row=1,sticky=tk.E)
        self.timi_fyrir_peninga.grid(column=1,row=1)
        tk.Label(self, text='kr.?').grid(column=2,row=1,sticky=tk.W)
        self.takki_timi.grid(column=3,row=1)

    def vidmot_peningar(self):
        tk.Label(self, text='Hvað mun ég eiga mikinn pening eftir').grid(
                column=0,row=2,sticky=tk.E)
        self.peningar_eftir_tima.grid(column=1,row=2)
        tk.Label(self, text='mánuði?').grid(column=2,row=2,sticky=tk.W)
        self.takki_peningar.grid(column=3,row=2)


class Lan(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.tryggt = tk.Checkbutton(self)
        self.heiti = tk.Entry(self, width=50)
        self.vextir = tk.Entry(self, width=10)
        self.timabil = tk.Entry(self, width=10)

        self.vidmot()

    def vidmot(self):
        self.tryggt.grid(row=0,column=0)
        self.heiti.grid(row=0,column=1)
        self.vextir.grid(row=0,column=2)
        self.timabil.grid(row=0,column=3)

    def fa_vexti(self):
        vextir = self.vextir.get()
        athugun = re.compile('[A-Za-z]')
        if athugun.search(vextir):
            tkMessageBox.showinfo('villa','Það er bókstafur í vaxtarálknum hjá ' + self.heiti.get())
        elif len(vextir)==0:
            tkMessageBox.showinfo('villa','gleymdir að fylla út vaxtadálkinn fyrir ' + self.heiti.get())
        else:
            return float(vextir)

    def fa_nafn(self):
        return self.heiti.get()


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
        tk.Label(merki, text='Heiti láns').grid(row=0,column=1)
        tk.Label(merki, text='Vextir').grid(row=0,column=2)
        tk.Label(merki, text='Tímabil').grid(row=0,column=3)
        merki.columnconfigure(1,weight=3)
        merki.columnconfigure(2,weight=1)
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
    def __init__(self, sparnadur, lanasafn, takkar):
        #self.graf = graf
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
        eg_a = self.sparnadur.upphaed.get()
        eg_vil = self.sparnadur.timi_fyrir_peninga.get()
        athugun = re.compile('\D+')
        if athugun.search(eg_a) or athugun.search(eg_vil):
            tkMessageBox.showinfo('villa', 'Þá verður að slá inn tölu ekki bókstaf! \nmundu að við notum bara heilar tölur')
        elif len(eg_a)==0 or len(eg_vil)==0:
            tkMessageBox.showinfo('villa', 'verður að fylla út báða reiti! \nmundu að við notum bara heilar tölur')
        elif int(eg_a)<=0:
            tkMessageBox.showinfo('villa', 'Þú verður að leggja eitthvað fyrir! \nmundu að við notum bara heilar tölur')
        else:    
            svar = int(eg_vil) / ( int(eg_a) * SPARI_VEXTIR )
            tkMessageBox.showinfo('Sparnaður', 'Það tekur ' + str(int(round(svar))) + ' marga mánuði.')

    def sparnadur_peningar(self):
        eg_a = self.sparnadur.upphaed.get()
        timi = self.sparnadur.peningar_eftir_tima.get()
        athugun = re.compile('\D+')
        if athugun.search(eg_a) or athugun.search(timi):
            tkMessageBox.showinfo('villa', 'Þú verður að slá inn tölu ekki bókstaf! \nmundu að við notum bara heilar tölur')
        elif len(eg_a)==0 or len(timi)==0:
            tkMessageBox.showinfo('villa', 'verður að fylla út báða reiti! \nmundu að við notum bara heilar tölur')
        else:
            svar = int(eg_a) * SPARI_VEXTIR * int(timi)
            tkMessageBox.showinfo('Sparnaður', 'Þú munt eiga ' + str(int(round(svar))) + ' kr.')


    def fa_topp_vexti(self, bunki):
        toppur = bunki[0]
        for i in bunki:
            if i.fa_vexti() > toppur.fa_vexti():
                toppur = i
        if toppur.fa_vexti() > SPARI_VEXTIR:
            return toppur.fa_nafn()
        else:
            return 'Vaxtasproti'

    def teikna(self):
        x = range(0,5)
        y = []
        temp = 0
        for i in x:
            temp += float(self.sparnadur.upphaed.get())*SPARI_VEXTIR
            y.append(temp)
        #self.graf.teikna_a_graf(x,y)


class Grunnur(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        #self.graf = Graf(self)
        self.sparnadur = Sparnadur(self)
        self.lanasafn= Lanasafn(self)
        self.takkar = Takkar(self)
        self.reikningur = Reikningur(self.sparnadur, self.lanasafn , self.takkar)

        self.vidmot()

    def vidmot(self):
        self.sparnadur.pack(side=tk.TOP,fill='both')
        self.lanasafn.pack(side=tk.TOP, fill='x', expand=True)
        self.takkar.pack(side=tk.TOP, fill='both')
        #self.graf.pack(side=tk.BOTTOM, fill='both', expand=True)


def main():
    root = tk.Tk()
    root.wm_title('Besta forrit í heimi!')
    app = Grunnur(root)
    app.pack(fill='both', expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
