from o3seespy.command.uniaxial_material.base_material import UniaxialMaterialBase



class PySimple1(UniaxialMaterialBase):
    """
    The PySimple1 UniaxialMaterial Class
    
    This command is used to construct a PySimple1 uniaxial material object.
    """
    op_type = 'PySimple1'

    def __init__(self, osi, soil_type, pult, y50, cd, c=0.0):
        """
        Initial method for PySimple1

        Parameters
        ----------
        soil_type: int
            Soiltype = 1 backbone of p-y curve approximates matlock (1970) soft clay relation. soiltype = 2 backbone of
            p-y curve approximates api (1993) sand relation.
        pult: float
            Ultimate capacity of the p-y material. note that "p" or "pult" are distributed loads [force per length of
            pile] in common design equations, but are both loads for this uniaxialmaterial [i.e., distributed load times the
            tributary length of the pile].
        y50: float
            Displacement at which 50% of pult is mobilized in monotonic loading.
        cd: float
            Variable that sets the drag resistance within a fully-mobilized gap as cd*pult.
        c: float
            The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity).
            (optional default = 0.0). nonzero c values are used to represent radiation damping effects
        """
        self.soil_type = int(soil_type)
        self.pult = float(pult)
        self.y50 = float(y50)
        self.cd = float(cd)
        self.c = float(c)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.soil_type, self.pult, self.y50, self.cd, self.c]
        self.to_process(osi)


class TzSimple1(UniaxialMaterialBase):
    """
    The TzSimple1 UniaxialMaterial Class
    
    This command is used to construct a TzSimple1 uniaxial material object.
    """
    op_type = 'TzSimple1'

    def __init__(self, osi, soil_type, tult, z50, c=0.0):
        """
        Initial method for TzSimple1

        Parameters
        ----------
        soil_type: int
            Soiltype = 1 backbone of t-z curve approximates reese and o'neill (1987). soiltype = 2 backbone of t-z curve
            approximates mosher (1984) relation.
        tult: float
            Ultimate capacity of the t-z material. see note 1.
        z50: float
            Displacement at which 50% of tult is mobilized in monotonic loading.
        c: float
            The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity).
            (optional default = 0.0). see note 2.
        """
        self.soil_type = int(soil_type)
        self.tult = float(tult)
        self.z50 = float(z50)
        self.c = float(c)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.soil_type, self.tult, self.z50, self.c]
        self.to_process(osi)


class QzSimple1(UniaxialMaterialBase):
    """
    The QzSimple1 UniaxialMaterial Class
    
    This command is used to construct a QzSimple1 uniaxial material object.
    """
    op_type = 'QzSimple1'

    def __init__(self, osi, qz_type, qult, z50, suction=0.0, c=0.0):
        """
        Initial method for QzSimple1

        Parameters
        ----------
        qz_type: int
            Qztype = 1 backbone of q-z curve approximates reese and o'neill's (1987) relation for drilled shafts in
            clay. qztype = 2 backbone of q-z curve approximates vijayvergiya's (1977) relation for piles in sand.
        qult: float
            Ultimate capacity of the q-z material. see note 1.
        z50: float
            Displacement at which 50% of qult is mobilized in monotonic loading. see note 2.
        suction: float
            Uplift resistance is equal to suction*qult. default = 0.0. the value of suction must be 0.0 to 0.1.*
        c: float
            The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity).
            default = 0.0. nonzero c values are used to represent radiation damping effects.*
        """
        self.qz_type = int(qz_type)
        self.qult = float(qult)
        self.z50 = float(z50)
        self.suction = float(suction)
        self.c = float(c)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.qz_type, self.qult, self.z50, self.suction, self.c]
        self.to_process(osi)


class PyLiq1(UniaxialMaterialBase):
    """
    The PyLiq1 UniaxialMaterial Class
    
    
    """
    op_type = 'PyLiq1'

    def __init__(self, osi, soil_type, pult, y50, cd, c, p_res, ele1, ele2, time_series=None):
        """
        Initial method for PyLiq1

        Parameters
        ----------
        soil_type: int
            Soiltype = 1 backbone of p-y curve approximates matlock (1970) soft clay relation. soiltype = 2 backbone of
            p-y curve approximates api (1993) sand relation.
        pult: float
            Ultimate capacity of the p-y material. note that "p" or "pult" are distributed loads [force per length of
            pile] in common design equations, but are both loads for this uniaxialmaterial [i.e., distributed load times the
            tributary length of the pile].
        y50: float
            Displacement at which 50% of pult is mobilized in monotonic loading.
        cd: float
            Variable that sets the drag resistance within a fully-mobilized gap as cd*pult.
        c: float
            The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity).
            (optional default = 0.0). nonzero c values are used to represent radiation damping effects
        p_res: float
            Sets the minimum (or residual) peak resistance that the material retains as the adjacent solid soil elements
            liquefy
        ele1: float
            Are the eletag (element numbers) for the two solid elements from which pyliq1 will obtain mean effective
            stresses and excess pore pressures
        ele2: float
            Are the eletag (element numbers) for the two solid elements from which pyliq1 will obtain mean effective
            stresses and excess pore pressures
        time_series: obj
            Alternatively, mean effective stress can be supplied by a time series by specifying the text string
            ``'-timeseries'`` and the tag of the series    ``seriestag``.
        """
        self.soil_type = int(soil_type)
        self.pult = float(pult)
        self.y50 = float(y50)
        self.cd = float(cd)
        self.c = float(c)
        self.p_res = float(p_res)
        self.ele1 = float(ele1)
        self.ele2 = float(ele2)
        self.time_series = time_series
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.soil_type, self.pult, self.y50, self.cd, self.c, self.p_res, self.ele1, self.ele2]
        if getattr(self, 'time_series') is not None:
            self._parameters += ['-timeSeries', self.time_series.tag]
        self.to_process(osi)


class TzLiq1(UniaxialMaterialBase):
    """
    The TzLiq1 UniaxialMaterial Class
    
    
    """
    op_type = 'TzLiq1'

    def __init__(self, osi, tz_type, tult, z50, c, ele1, ele2, time_series=None):
        """
        Initial method for TzLiq1

        Parameters
        ----------
        tz_type: int
            Tztype = 1 backbone of t-z curve approximates reese and o'neill (1987). tztype = 2 backbone of t-z curve
            approximates mosher (1984) relation.
        tult: float
            Ultimate capacity of the t-z material. see note 1.
        z50: float
            Displacement at which 50% of tult is mobilized in monotonic loading.
        c: float
            The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity).
        ele1: float
            Are the eletag (element numbers) for the two solid elements from which pyliq1 will obtain mean effective
            stresses and excess pore pressures
        ele2: float
            Are the eletag (element numbers) for the two solid elements from which pyliq1 will obtain mean effective
            stresses and excess pore pressures
        time_series: obj
            Alternatively, mean effective stress can be supplied by a time series by specifying the text string
            ``'-timeseries'`` and the tag of the seriesm    ``seriestag``.
        """
        self.tz_type = int(tz_type)
        self.tult = float(tult)
        self.z50 = float(z50)
        self.c = float(c)
        self.ele1 = float(ele1)
        self.ele2 = float(ele2)
        self.time_series = time_series
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.tz_type, self.tult, self.z50, self.c, self.ele1, self.ele2]
        if getattr(self, 'time_series') is not None:
            self._parameters += ['-timeSeries', self.time_series.tag]
        self.to_process(osi)
