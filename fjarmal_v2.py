#!/usr/bin/env python
# encoding: utf-8

import Tkinter as tk
import ttk
import tkMessageBox
import verdbolga
import re
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

SPARI_VEXTIR = 1.035

class Graf(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text='Graf', padx=4, pady=4)
        self.f = Figure(figsize=(4,4), dpi=50)
        self.a = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    def teikna_a_graf(self, x, y, nafn, titill):
        self.a.plot(x,y,label=nafn)
        self.a.legend(title=titill)
        self.canvas.show()

    def hreinsa_graf(self):
        self.a.cla()


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


class Verdtrygging(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.wm_title('Verðtrygging')
        self.stada = tk.IntVar()
        self.fyrra_ar = ttk.Combobox(self, state='readonly', width=10, values=verdbolga.artal)
        self.seinna_ar = ttk.Combobox(self, state='readonly', width=10, values=verdbolga.artal)
        self.i_dag = tk.Button(self, text='Verðbólga í dag')
        self.skra = tk.Button(self, text='Skrá')
        self.vidmot()

    def vidmot(self):
        tk.Label(self, text='Veldu tímabil verðbólgu?').pack()
        self.i_dag.pack()
        tk.Label(self, text='Einnig er hægt að velja verðbólgu á tímabili.').pack()
        tk.Label(self, text='Frá:').pack()
        self.fyrra_ar.pack()
        tk.Label(self, text='Til:').pack()
        self.seinna_ar.pack()
        self.skra.pack()


class Lan(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.verdtrygging = Verdtrygging()
        self.verdtrygging.wm_withdraw()
        self.verdtrygging.skra.config(command=self.skra_tryggingu)
        self.verdtrygging.i_dag.config(command=self.skra_tryggingu_i_dag)
        self.verdtrygging.protocol('WM_DELETE_WINDOW', self.skra_tryggingu)
        self.i_dag = 0
        self.tryggt = tk.Checkbutton(self, variable=self.verdtrygging.stada, width=8, command=self.tryggja)
        self.heiti = tk.Entry(self, width=28)
        self.upphaed = tk.Entry(self, width=13)
        self.vextir = tk.Entry(self, width=9)
        self.timabil = tk.Entry(self, width=9)

        self.vidmot()

    def skra_tryggingu_i_dag(self):
        vt = 'Í dag'
        self.tryggt.config(text=vt)
        self.verdtrygging.wm_withdraw()
        self.i_dag = 1

    def skra_tryggingu(self):
        f = self.verdtrygging.fyrra_ar.get()
        s = self.verdtrygging.seinna_ar.get()
        if f == '' and s == '':
            self.tryggt.config(text='')
            self.tryggt.deselect()
        elif s != '' and f == '':
            self.tryggt.config(text=s)
        elif f != '' and s == '':
            self.tryggt.config(text=f)
        else:
            vt = min(f,s) + '-' + max(f,s)
            self.tryggt.config(text=vt)
        self.verdtrygging.wm_withdraw()
        self.i_dag = 0

    def vidmot(self):
        self.tryggt.grid(row=0,column=0)
        self.upphaed.grid(row=0,column=1)
        self.heiti.grid(row=0,column=2)
        self.vextir.grid(row=0,column=3)
        self.timabil.grid(row=0,column=4)

    def tryggja(self):
        if self.verdtrygging.stada.get():
            self.verdtrygging.wm_deiconify()
        else:
            self.tryggt.config(text='')
            self.i_dag = 0

    def fa_medal_bolgu(self):
        f = self.verdtrygging.fyrra_ar.get()
        s = self.verdtrygging.seinna_ar.get()
        if self.i_dag:
            return verdbolga.stodlud_verdbolga
        elif f == '' and s == '':
            self.tryggt.config(text='')
            self.tryggt.deselect()
            self.i_dag = 0
            return 0
        elif s != '' and f == '':
            s = verdbolga.artal.index(int(self.verdtrygging.seinna_ar.get()))
            return verdbolga.verdbolga[s]
        elif f != '' and s == '':
            f = verdbolga.artal.index(int(self.verdtrygging.fyrra_ar.get()))
            return verdbolga.verdbolga[f]
        else:
            f = verdbolga.artal.index(int(self.verdtrygging.fyrra_ar.get()))
            s = verdbolga.artal.index(int(self.verdtrygging.seinna_ar.get()))
            if f == s:
                return verdbolga.verdbolga[f]
            else:
                tot = 0
                for i in verdbolga.verdbolga[f:s+1]:
                    tot += float(i)
                return tot/abs(s-f+1)

    def fa_vexti(self):
        vextir = self.vextir.get()
        athugun = re.compile('[A-Za-z]')
        if athugun.search(vextir):
            tkMessageBox.showinfo('villa','Það er bókstafur í vaxtarálknum hjá ' + self.heiti.get())
        elif len(vextir)==0:
            tkMessageBox.showinfo('villa','gleymdir að fylla út vaxtadálkinn fyrir ' + self.heiti.get())
        elif self.verdtrygging.stada.get():
            return float(vextir) + self.fa_medal_bolgu()
        else:
            return float(vextir)

    def fa_nafn(self):
        heiti = self.heiti.get()
        athugun = re.compile('\s')
        if len(heiti)==0:
            tkMessageBox.showinfo('villa','gleymdir að fylla út lánsheiti fyrir lánið þitt')
        if athugun.match(heiti):
            tkMessageBox.showinfo('villa','þú verður að slá inn bókstafi, ekki byrja á bili')
        return heiti

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
        self.takkar.hvad.config(command=self.prof(self.bera_saman_vexti))
        self.takkar.teikna.config(command=self.prof(self.teikna))

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
            tkMessageBox.showinfo('Sparnaður', 'Það tekur ' + str(int(round(svar))) + ' mánuð/i.')

    def sparnadur_peningar(self):
        eg_a = self.sparnadur.upphaed.get()
        timi = self.sparnadur.timabil.get()
        athugun = re.compile('\D+')
        if athugun.search(eg_a) or athugun.search(timi):
            tkMessageBox.showinfo('villa', 'Þú verður að slá inn tölu ekki bókstaf! \nmundu að við notum bara heilar tölur')
        elif len(eg_a)==0 or len(timi)==0:
            tkMessageBox.showinfo('villa', 'verður að fylla út báða reiti! \nmundu að við notum bara heilar tölur')
        else:
            svar = int(eg_a) * SPARI_VEXTIR * int(timi)
            tkMessageBox.showinfo('Sparnaður', 'Þú munt eiga ' + str(int(round(svar))) + ' kr.')

    def fa_topp_lan(self, bunki):
        toppur = bunki[0]
        for i in bunki:
            if i.fa_vexti() > float(toppur.fa_vexti()):
                toppur = i
        return toppur

    def fa_topp_vexti(self, bunki):
        lan = self.fa_topp_lan(bunki)
        if lan.fa_vexti() > SPARI_VEXTIR:
            return lan.fa_nafn()
        else:
            return 'Vaxtasproti'

    def prof(self):
        for i in self.lanasafn.bunki:
            if i.fa_nafn() == '' or i.fa_vexti() == '' or i.fa_timabil() == '' or i.fa_upphaed() == '':
                tkMessageBox.showinfo('Sparnaður', 'þú verður að fylla allt út eða fjarlægja óútfyllt lán.')
                return False
        return True



    def teikna(self):
        lan = self.fa_topp_lan(self.lanasafn.bunki)
        nafn = lan.fa_nafn()
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
        self.graf.hreinsa_graf()
        self.graf.teikna_a_graf(x,y_lan,'Ekki borga inn',nafn)
        self.graf.teikna_a_graf(x,y_spari,'Borga inn',nafn)


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
