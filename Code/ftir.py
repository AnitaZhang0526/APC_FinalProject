from Code.ExperimentalTechnique import ExperimentalTechnique

class FTIR(ExperimentalTechnique):

	def filter_baseline():
		# add Arjun's filter method
		pass

	def flip_input(self,a_or_t,spectrum):
		if a_or_t == "transmittance":
			spectrum['x'] = 2-log(spectrum['x'])
