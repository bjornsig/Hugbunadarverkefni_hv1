# -*- coding: utf-8 -*-

class spari:
	def __init__(self):
		self.sparnadur = 0
		self.sparileid = [('Vaxtasproti',0.036,0), ('Vaxtaþrep',0.043,1)]
		self.val = 0

		self.byrja()



	def byrja(self):
		self.sparnadur = raw_input('hvað ertu tilbúinn að leggja til á mánuði')
		c = 1
		print('Eftirfarandi sparnaðarleiðir eru í boði: ')
		for i in self.sparileid:
			print(c + '. ' + i[0] + '- vextirnir eru: ' + str(i[1]*100) + '- bundið í ' + str(i[2]) + ' mánuði')
		got_it = False
		while got_it == False
			temp = raw_input('hvaða leið má bjóða þér ?\n')
			if temp == "1" || temp == "2":
				print('þú valdir ' + self.sparileid[int(temp)-1][0])
				self.val = int(temp)
				got_it = True
			else
				print('veldu númer sparileiðanna')

	def get_vextir(self):
		return self.sparileid[self.val][1]