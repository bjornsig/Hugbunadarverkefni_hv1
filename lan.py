# -*- coding: utf-8 -*-

class lan:
    def __init__(self):
        self.heiti = ''
        self.upphaed = 0
        self.timibil = 0
        self.vextir = 0
        self.tryggt = ''

        self.byrja()

    def byrja(self):
        self.nytt_lan()


    def nytt_lan(self):
        self.heiti = raw_input('Hvað heitir lánið sem þú ert að hugsa um?\n')
        self.upphaed = raw_input('Hver er lánsupphæðin?\n')
        self.timabil = raw_input('Hve margir mánuðir eru eftir af láninu?\n')
        self.vextir = raw_input('Hve háir eru vextirnir?\n')
        self.tryggt = raw_input('Er lánið verðtryggt? ja/nei\n')

    def print_lan(self):
        print('Nafn láns: ' + self.heiti)
        print('Upphæð láns: ' + self.upphaed)
        print('Tímabil láns: ' + self.timabil)
        print('Vextir láns: ' + self.vextir)
        print('Verðtryggt: ' + self.tryggt)
        print('')

    def get_vextir(self):
        return self.vextir

print('Hæ, hæ. Ég er fjármálalæsiforrit.')
lanasafn = []
hlaupa = True
while hlaupa != False:
    lanasafn.append(lan())
    got_it = False
    while got_it != True:
        meir = raw_input('Ertu með fleiri lán? ja/nei\n')
        if meir == 'nei':
            got_it = True
            hlaupa = False
        elif meir == 'ja':
            got_it = True
        else:
            print('HA?!?')

for i in lanasafn:
    i.print_lan()
