import unittest
import fjarmal_v2

class test(unittest.TestCase):

	

	def test_reikna_pening(self):
		tilraunadyr = fjarmal_v2.tester()
		self.assertEqual(tilraunadyr.reikna_pening_test(100,120),12420)
		self.assertEqual(tilraunadyr.reikna_pening_test(0,120),0)
		self.assertEqual(tilraunadyr.reikna_pening_test(88,120),10930)
		self.assertEqual(tilraunadyr.reikna_pening_test(5765,88),525076)

	def test_reikna_spari(self):
		tilraunadyr = fjarmal_v2.tester()
		self.assertEqual(tilraunadyr.reikna_spari_test(100,200000),1932)
		self.assertEqual(tilraunadyr.reikna_spari_test(50,437222),8449)
		self.assertEqual(tilraunadyr.reikna_spari_test(1,100),97)
		self.assertEqual(tilraunadyr.reikna_spari_test(0,200000),0)
		self.assertEqual(tilraunadyr.reikna_spari_test(100000,2320000),22)

	def test_fa_topp_vexti(self):
		tilraunadyr = fjarmal_v2.tester()
		self.assertEqual(tilraunadyr.fa_topp_vexti([]),0)
		self.assertEqual(tilraunadyr.fa_topp_vexti([0.5,0.6,0.7,0.1]),0.7)
		self.assertEqual(tilraunadyr.fa_topp_vexti([1.7,8,7,4.3,99]),99)
		self.assertEqual(tilraunadyr.fa_topp_vexti([2,2,2,2,2,2,2,2]),2)
		self.assertEqual(tilraunadyr.fa_topp_vexti([1.03,1.003]),1.03)

		


if __name__ == '__main__':
	unittest.main(verbosity=2, exit=False)