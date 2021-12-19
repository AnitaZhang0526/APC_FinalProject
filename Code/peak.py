class Peak:
    """
    This is the Peak class 
    
    FWHM: type double, given by param FWHM
    center: type double, given by param center
    intensity: type double, given by param intensity
    type: type string, given by param type
    """
    def __init__(self, FWHM,center,intensity,type):
        """
        Constructor method
        :param FWHM: full width half max of a peak
        :type FWHM: double
        :param center: center of a peak
        :type center: double
        :param intensity: height of a peak
        :type intensity: double
        :param type: peak type options: 'GaussianModel', 'LorentzianModel', 'VoightModel', or 'Polynomial'
        :type type: str
        :return: a Peak object
        """
        self.FWHM = FWHM # full width half max
        self.center = center # center
        self.intensity = intensity  # intensity
        self.type = type # peak type
    
    def as_dict(self):
        """
        :return: peaks in dictrionary format
        """
        return {
        	'FWHM': self.FWHM,  # full width half max
        	'center': self.center,  # center
        	'intensity': self.intensity, # intensity
        	'type': self.type # peak type
        }