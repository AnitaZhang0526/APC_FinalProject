from ExperimentalTechnique import ExperimentalTechnique

class FTIR(ExperimentalTechnique):

	def filter_baseline():
		# add Arjun's filter method
		pass

	def flip_input(self,a_or_t):
		if a_or_t == "transmittance":
			self.spectrum['x'] = 2-log(self.spectrum['x'])
