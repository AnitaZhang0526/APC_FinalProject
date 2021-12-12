from ExperimentalTechnique import ExperimentalTechnique
import Code.baseline as baseline

class FTIR(ExperimentalTechnique):

	def filter_baseline(self):
		baseline_removed = baseline.baseline_removal(self.spectrum['y'])
		return baseline_removed
		

	def flip_input(self,a_or_t):
		if a_or_t == "transmittance":
			self.spectrum['x'] = 2-log(self.spectrum['x'])
