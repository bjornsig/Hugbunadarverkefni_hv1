# -*- coding: utf-8 -*-

class lan:
    def __init__(self):
        self.heiti = ''
        self.upphaed = 0
        self.timibil = 0
        self.vextir = 0

        self.byrja()

    def byrja(self):
        self.nytt_lan()


    def nytt_lan(self):
        self.heiti = raw_input('Hvað heitir lánið sem þú ert með?\n')
        self.upphaed = raw_input('Hver er lánsupphæðin?\n')
        self.timabil = raw_input('Hve margir mánuðir eru eftir af láninu?\n')
        self.vextir = float(raw_input('Hve háir eru vextirnir?\n'))

    def print_lan(self):
        print('Nafn láns: ' + self.heiti)
        print('Upphæð láns: ' + self.upphaed)
        print('Tímabil láns: ' + self.timabil)
        print('Vextir láns: ' + self.vextir)
        print('Verðtryggt: ' + self.tryggt)
        print('')

    def get_vextir(self):
        return (self.vextir,self.heiti)

