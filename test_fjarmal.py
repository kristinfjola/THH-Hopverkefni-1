import unittest
import sparnadur1b
import sparitimi
import lan_v

class testMaxFunctions(unittest.TestCase):
	def test_raunvx(self):
		self.assertEqual(sparnadur1b.raunvx(0, 12), 0.046)
		self.assertEqual(sparnadur1b.raunvx(1, 36), 0.0175)
	def test_sparivx(self):
		self.assertEqual(sparnadur1b.sparivx(0, 24), 0.053)
		self.assertEqual(sparnadur1b.sparivx(1, 48), 0.0185)
	def test_hvad_er_best_ad_gera(self):
		self.assertEqual(sparnadur1b.hvad_er_best_ad_gera(12), 'Ad borga inn a Overdtryggdur 12')
		self.assertEqual(sparnadur1b.hvad_er_best_ad_gera(36), 'Ad borga inn a Verdtryggdur 36')	
	def test_overdAfborganirMan(self):
		self.assertEqual(lan_v.overdAfborganirMan(10000, 0, 5, 500, 'lan1', 0), [[], []])
		self.assertEqual(lan_v.overdAfborganirMan(500000, 0, 3, 25000, 'lan2', 0), [[], []])	
	def test_eingreidslaSparInnlogn(self):
		self.assertEqual(sparitimi.eingreidslaSparInnlogn(12, 0.05, 1000000), 'Thu tharft ad leggja inn 952381.0 i upphafi til thess ad na uppi 1000000')
		self.assertEqual(sparitimi.eingreidslaSparInnlogn(36, 0.10, 2000000), 'Thu tharft ad leggja inn 1502630.0 i upphafi til thess ad na uppi 2000000')
	def test_manadalegurSparTimi(self):
		self.assertEqual(sparitimi.manadalegurSparTimi(10000, 0.08, 0.06, 150000), 'Thu tarft ad spara i 15 manudi til thess ad na uppi 150000')
		self.assertEqual(sparitimi.manadalegurSparTimi(10, 0.08, 0.06, 500), 'Thu tarft ad spara i 42 manudi til thess ad na uppi 500')
	def test_eingreidslaSparTimi(self):
		self.assertEqual(sparitimi.eingreidslaSparTimi(89000, 0.08, 0.04, 250000), 'Thu tharft ad spara i 134 manudi til thess ad na uppi 250000')
		self.assertEqual(sparitimi.eingreidslaSparTimi(1000000, 0.03, 0.07, 1500000), 'Thu tharft ad spara i 62 manudi til thess ad na uppi 1500000')

if __name__ == '__main__':
	unittest.main(verbosity=2, exit=False)