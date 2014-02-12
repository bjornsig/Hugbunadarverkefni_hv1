#!/usr/bin/env python
# encoding: utf-8

import Tkinter as tk
import ttk

class Merki(tk.Frame):
    def __init__(self, parent, bg):
        tk.Frame.__init__(self, parent, background=bg)
        tk.Label(self, text='Verðtryggt').grid(row=0,column=0)
        tk.Label(self, text='Heiti lans').grid(row=0,column=1)
        tk.Label(self, text='Vextir').grid(row=0,column=2)
        tk.Label(self, text='Timabil').grid(row=0,column=3)
        self.columnconfigure(1,weight=3)
        self.columnconfigure(2,weight=1)

class Lan(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.form()

    def form(self):
        self.tryggt = tk.Checkbutton(self).grid(row=0,column=0)
        self.heiti = tk.Entry(self, width=50).grid(row=0,column=1)
        self.timabil = tk.Entry(self, width=10).grid(row=0,column=2)
        self.vextir = ttk.Combobox(self, state='readonly', width=10, values=['hallo','bless']).grid(row=0,column=3)

class Lanagluggi(tk.LabelFrame):
    def __init__(self, parent, bg):
        tk.LabelFrame.__init__(self, parent, background=bg, text='Fullt af lanum', padx=4, pady=4)
        Merki(self, bg='orange').pack(side=tk.TOP, fill='both')
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

class Spari(tk.LabelFrame):
    def __init__(self, parent, bg):
        tk.LabelFrame.__init__(self, parent, background=bg, text='Sparnadur', padx=4, pady=4)
        Merki(self, bg='orange').pack(side=tk.TOP, fill='both')
        self.form()

    def form(self):
        self.rammi = tk.Frame(self)
        self.rammi.pack(side=tk.TOP, fill='both')
        self.tryggt = tk.Checkbutton(self.rammi).grid(row=0,column=0)
        self.heiti = tk.Entry(self.rammi, width=50).grid(row=0,column=1)
        self.timabil = tk.Entry(self.rammi, width=10).grid(row=0,column=2)
        self.vextir = tk.Entry(self.rammi, width=10).grid(row=0,column=3)

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
        self.lanagluggi = Lanagluggi(self, bg='blue')
        self.lanagluggi.pack(side=tk.TOP, fill='x', expand=True)
        Spari(self, bg='green').pack(side=tk.TOP, fill='both')
        Takkar(self, self.lanagluggi.nytt_lan, self.lanagluggi.taka_ut_lan).pack(side=tk.TOP, fill='both')

def main():
    root = tk.Tk()
    app = Grunnur(root)
    app.pack(fill='both', expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
