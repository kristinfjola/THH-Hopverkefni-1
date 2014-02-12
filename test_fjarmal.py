import unittest
import sparnadur1b
import lan_v

class testMaxFunctions(unittest.TestCase):
	def test_raunvx(self):
		self.assertEqual(sparnadur1b.raunvx(0, 12), 0.046)
		self.assertEqual(sparnadur1b.raunvx(0, 18), 0.048)
		self.assertEqual(sparnadur1b.raunvx(1, 36), 0.0175)
		self.assertEqual(sparnadur1b.raunvx(1, 36), 0.0175)
	def test_sparivx(self):
		self.assertEqual(sparnadur1b.sparivx(0, 12), 0.046)
		self.assertEqual(sparnadur1b.sparivx(0, 24), 0.053)
		self.assertEqual(sparnadur1b.sparivx(1, 36), 0.0175)
		self.assertEqual(sparnadur1b.sparivx(1, 48), 0.0185)
	def test_hvad_er_best_ad_gera(self):
		self.assertEqual(sparnadur1b.hvad_er_best_ad_gera(12), 'Ad borga inn a Overdtryggdur 12')
		self.assertEqual(sparnadur1b.hvad_er_best_ad_gera(36), 'Ad borga inn a Verdtryggdur 36')	
	def test_overdAfborganirMan(self):
		self.assertEqual(lan_v.overdAfborganirMan(10000, 0, 5, 500, 'Lan 1'), [[], []])
		self.assertEqual(lan_v.overdAfborganirMan(500000, 0, 3, 25000, 'Lan 2'), [[], []])	
		
if __name__ == '__main__':
	unittest.main(verbosity=2, exit=False)