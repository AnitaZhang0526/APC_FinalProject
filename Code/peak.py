class Peak:
    """
    : peak class 
    : a peak is defined by its full width half max, center, intensity, and type
    """
    def __init__(self, FWHM,center,intensity,type):
        self.FWHM = FWHM
        self.center = center
        self.intensity = intensity
        self.type = type