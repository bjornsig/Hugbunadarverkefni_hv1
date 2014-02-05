# -*- coding: utf-8 -*-
import lan
import spari

print('Hæ, hæ. Ég er fjármálalæsiforrit.')
lanasafn = []
hlaupa = True
sparnadur = spari.spari()

temp = raw_input('Ertu með lán? ja/nei\n')

if temp == 'nei':
    hlaupa = False

while hlaupa != False:
    lanasafn.append(lan.lan())
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

maxy = (0,'')
for i in lanasafn:
    if (i.get_vextir()[0]) > maxy[0]:
        maxy = i.get_vextir()
if sparnadur.get_vextir()[0] > maxy[0]:
    maxy = sparnadur.get_vextir()

print('Best er að borga inn á ' + maxy[1])
