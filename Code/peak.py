class Peak:
    """
    :This is the Peak class 
    
    :FWHM: type double, given by param FWHM
    :center: type double, given by param center
    :intensity: type double, given by param intensity
    :type: type string, given by param type
    """
    def __init__(self, FWHM,center,intensity,type):
        """
        :Constructor method
        :param FWHM: type double, full width half max of a peak
        :param center: type double, center of a peak
        :param intensity: type double, height of a peak
        :param type: type string, peak type options: 'GaussianModel', 'LorentzianModel', 'VoightModel', or 'Polynomial'
        """
        self.FWHM = FWHM # full width half max
        self.center = center # center
        self.intensity = intensity  # intensity
        self.type = type # peak type
    
    def as_dict(self):
        """
        :returns peaks in dictrionary format
        """
        return {
        	'FWHM': self.FWHM,  # full width half max
        	'center': self.center,  # center
        	'intensity': self.intensity, # intensity
        	'type': self.type # peak type
        }