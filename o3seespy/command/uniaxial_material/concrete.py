from o3seespy.command.uniaxial_material.base_material import UniaxialMaterialBase



class Concrete01(UniaxialMaterialBase):
    """
    The Concrete01 UniaxialMaterial Class
    
    This command is used to construct a uniaxial Kent-Scott-Park concrete material object with degraded linear
    unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. (REF: Fedeas).
    """
    op_type = 'Concrete01'

    def __init__(self, osi, fpc, epsc0, fpcu, eps_u):
        """
        Initial method for Concrete01

        Parameters
        ----------
        fpc: float
            Concrete compressive strength at 28 days (compression is negative)
        epsc0: float
            Concrete strain at maximum strength
        fpcu: float
            Concrete crushing strength
        eps_u: float
            Concrete strain at crushing strength
        """
        self.fpc = float(fpc)
        self.epsc0 = float(epsc0)
        self.fpcu = float(fpcu)
        self.eps_u = float(eps_u)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fpc, self.epsc0, self.fpcu, self.eps_u]
        self.to_process(osi)


class Concrete02(UniaxialMaterialBase):
    """
    The Concrete02 UniaxialMaterial Class
    
    This command is used to construct a uniaxial Kent-Scott-Park concrete material object with degraded linear
    unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. (REF: Fedeas).
    """
    op_type = 'Concrete02'

    def __init__(self, osi, fpc, epsc0, fpcu, eps_u, lamb, ft, ets):
        """
        Initial method for Concrete02

        Parameters
        ----------
        fpc: float
            Concrete compressive strength at 28 days (compression is negative)
        epsc0: float
            Concrete strain at maximum strength
        fpcu: float
            Concrete crushing strength
        eps_u: float
            Concrete strain at crushing strength
        lamb: float
            Ratio between unloading slope at $epscu and initial slope
        ft: float
            Tensile strength
        ets: float
            Tension softening stiffness (absolute value) (slope of the linear tension softening branch)
        """
        self.fpc = float(fpc)
        self.epsc0 = float(epsc0)
        self.fpcu = float(fpcu)
        self.eps_u = float(eps_u)
        self.lamb = float(lamb)
        self.ft = float(ft)
        self.ets = float(ets)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fpc, self.epsc0, self.fpcu, self.eps_u, self.lamb, self.ft, self.ets]
        self.to_process(osi)


class Concrete04(UniaxialMaterialBase):
    """
    The Concrete04 UniaxialMaterial Class
    
    This command is used to construct a uniaxial Popovics concrete material object with degraded linear
    unloading/reloading stiffness according to the work of Karsan-Jirsa and tensile strength with exponential decay.
    """
    op_type = 'Concrete04'

    def __init__(self, osi, fc, epsc, epscu, ec, fct, et, beta):
        """
        Initial method for Concrete04

        Parameters
        ----------
        fc: float
            Floating point values defining concrete compressive strength at 28 days (compression is negative)
        epsc: float
            Floating point values defining concrete strain at maximum strength
        epscu: float
            Floating point values defining concrete strain at crushing strength
        ec: float
            Floating point values defining initial stiffness
        fct: float
            Floating point value defining the maximum tensile strength of concrete (optional)
        et: float
            Floating point value defining ultimate tensile strain of concrete (optional)
        beta: float
            Loating point value defining the exponential curve parameter to define the residual stress (as a factor of
            ft) at etu
        """
        self.fc = float(fc)
        self.epsc = float(epsc)
        self.epscu = float(epscu)
        self.ec = float(ec)
        self.fct = float(fct)
        self.et = float(et)
        self.beta = float(beta)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc, self.epsc, self.epscu, self.ec, self.fct, self.et, self.beta]
        self.to_process(osi)


class Concrete06(UniaxialMaterialBase):
    """
    The Concrete06 UniaxialMaterial Class
    
    This command is used to construct a uniaxial concrete material object with tensile strength, nonlinear tension
    stiffening and compressive behavior based on Thorenfeldt curve.
    """
    op_type = 'Concrete06'

    def __init__(self, osi, fc, e0, n, k, alpha1, fcr, ecr, b, alpha2):
        """
        Initial method for Concrete06

        Parameters
        ----------
        fc: float
            Concrete compressive strength (compression is negative)
        e0: float
            Strain  at compressive strength
        n: float
            Compressive shape factor
        k: float
            Post-peak compressive shape factor
        alpha1: float
            :math:`\alpha_1` parameter for compressive plastic strain definition
        fcr: float
            Tensile strength
        ecr: float
            Tensile strain at peak stress (fcr)
        b: float
            Exponent of the tension stiffening curve
        alpha2: float
            :math:`\alpha_2` parameter for tensile plastic strain definition
        """
        self.fc = float(fc)
        self.e0 = float(e0)
        self.n = float(n)
        self.k = float(k)
        self.alpha1 = float(alpha1)
        self.fcr = float(fcr)
        self.ecr = float(ecr)
        self.b = float(b)
        self.alpha2 = float(alpha2)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc, self.e0, self.n, self.k, self.alpha1, self.fcr, self.ecr, self.b, self.alpha2]
        self.to_process(osi)


class Concrete07(UniaxialMaterialBase):
    """
    The Concrete07 UniaxialMaterial Class
    
    Concrete07 is an implementation of Chang & Mander's 1994 concrete model with simplified unloading and reloading
    curves. Additionally the tension envelope shift with respect to the origin proposed by Chang and Mander has been
    removed. The model requires eight input parameters to define the monotonic envelope of confined and unconfined
    concrete in the following form:
    """
    op_type = 'Concrete07'

    def __init__(self, osi, fc, epsc, ec, ft, et, xp, xn, r):
        """
        Initial method for Concrete07

        Parameters
        ----------
        fc: float
            Concrete compressive strength (compression is negative)
        epsc: float
            Concrete strain at maximum compressive strength
        ec: float
            Initial elastic modulus of the concrete
        ft: float
            Tensile strength of concrete (tension is positive)
        et: float
            Tensile strain at max tensile strength of concrete
        xp: float
            Non-dimensional term that defines the strain at which the straight line descent begins in tension
        xn: float
            Non-dimensional term that defines the strain at which the straight line descent begins in compression
        r: float
            Parameter that controls the nonlinear descending branch
        """
        self.fc = float(fc)
        self.epsc = float(epsc)
        self.ec = float(ec)
        self.ft = float(ft)
        self.et = float(et)
        self.xp = float(xp)
        self.xn = float(xn)
        self.r = float(r)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc, self.epsc, self.ec, self.ft, self.et, self.xp, self.xn, self.r]
        self.to_process(osi)


class Concrete01WithSITC(UniaxialMaterialBase):
    """
    The Concrete01WithSITC UniaxialMaterial Class
    
    This command is used to construct a modified uniaxial Kent-Scott-Park concrete material object with degraded linear
    unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. The modification is to
    model the effect of Stuff In The Cracks (SITC).
    """
    op_type = 'Concrete01WithSITC'

    def __init__(self, osi, fpc, epsc0, fpcu, eps_u, end_strain_sitc=0.01):
        """
        Initial method for Concrete01WithSITC

        Parameters
        ----------
        fpc: float
            Concrete compressive strength at 28 days (compression is negative)
        epsc0: float
            Concrete strain at maximum strength
        fpcu: float
            Concrete crushing strength
        eps_u: float
            Concrete strain at crushing strength
        end_strain_sitc: float
            Optional, default = 0.03
        """
        self.fpc = float(fpc)
        self.epsc0 = float(epsc0)
        self.fpcu = float(fpcu)
        self.eps_u = float(eps_u)
        self.end_strain_sitc = float(end_strain_sitc)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fpc, self.epsc0, self.fpcu, self.eps_u, self.end_strain_sitc]
        self.to_process(osi)


class ConfinedConcrete01(UniaxialMaterialBase):
    """
    The ConfinedConcrete01 UniaxialMaterial Class
    
    
    """
    op_type = 'ConfinedConcrete01'

    def __init__(self, osi, sec_type, fpc, ec, epscu_type, epscu_val, nu, l1, l2, l3, phis, big_s, fyh, es0, ha_ratio, mu, phi_lon, internal_args: list=None, wrap_args: list=None, gravel=False, silica=False, tol: float=None, max_num_iter: int=None, epscu_limit: float=None, st_ratio=None):
        """
        Initial method for ConfinedConcrete01

        Parameters
        ----------
        sec_type: str
            Tag for the transverse reinforcement configuration. see image below. * ``'s1'`` square section with s1 type
            of transverse reinforcement with or without external frp wrapping * ``'s2'`` square section with s2 type of transverse
            reinforcement with or without external frp wrapping * ``'s3'`` square section with s3 type of transverse
            reinforcement with or without external frp wrapping * ``'s4a'`` square section with s4a type of
            transverse reinforcement with or without external frp wrapping * ``'s4b'`` square section with
            s4b type of transverse reinforcement with or without external frp wrapping * ``'s5'`` square
            section with s5 type of transverse reinforcement with or without external frp wrapping *
            ``'c'`` circular section with or without external frp wrapping * ``'r'`` rectangular
            section with or without external frp wrapping.
        fpc: float
            Unconfined cylindrical strength of concrete specimen.
        ec: float
            Initial elastic modulus of unconfined concrete.
        epscu_type: str
            Method to define confined concrete ultimate strain * ``-epscu`` then value is confined concrete ultimate
            strain, * ``-gamma`` then value is the ratio of the strength corresponding to ultimate strain to the peak strength
            of the confined concrete in the range [0, epsculimit] then epsculimit (optional, default: 0.05) will be assumed
            as ultimate strain.
        epscu_val: float
            Value for the definition of the concrete ultimate strain
        nu: str or list
            Definition for poisson's ratio. * ``*['-nu', <value of poisson's ratio>]`` * ``'-varub'`` poisson's ratio is
            defined as a function of axial strain by means of the expression proposed by braga et al. (2006) with the upper bound
            equal to 0.5 *``'-varnoub'`` poisson's ratio is defined as a function of axial strain by means of the expression
            proposed by braga et al. (2006) without any upper bound.
        l1: float
            Length/diameter of square/circular core section measured respect to the hoop center line.
        l2: float
            Additional dimensions when multiple hoops are being used.
        l3: float
            Additional dimensions when multiple hoops are being used.
        phis: float
            Hoop diameter. if section arrangement has multiple hoops it refers to the external hoop.
        big_s: float
            Hoop spacing.
        fyh: float
            Yielding strength of the hoop steel.
        es0: float
            Elastic modulus of the hoop steel.
        ha_ratio: float
            Hardening ratio of the hoop steel.
        mu: float
            Ductility factor of the hoop steel.
        phi_lon: float
            Diameter of longitudinal bars.
        internal_args: list
            ``internalargs= [phisi, si, fyhi, es0i, haratioi, mui]`` optional parameters for defining the internal
            transverse reinforcement. if they are not specified they will be assumed equal to the external ones
        wrap_args: list
            ``wrapargs=[cover, am, sw, ful, es0w]`` optional parameters required when section is strengthened with frp
            wraps. * ``cover`` cover thickness measured from the outer line of hoop. * ``am`` total area of frp wraps (number of
            layers x wrap thickness x wrap width). * ``sw`` spacing of frp wraps (if continuous wraps are used the spacing is
            equal to the wrap width). * ``ful`` ultimate strength of frp wraps. * ``es0w`` elastic modulus of frp wraps.
        gravel: str
            Unknown
        silica: str
            Unknown
        tol: float
            Unknown
        max_num_iter: int
            Unknown
        epscu_limit: float
            Unknown
        st_ratio: unk
            Unknown
        """
        self.sec_type = sec_type
        self.fpc = float(fpc)
        self.ec = float(ec)
        self.epscu_type = epscu_type
        self.epscu_val = float(epscu_val)
        self.nu = nu
        self.l1 = float(l1)
        self.l2 = float(l2)
        self.l3 = float(l3)
        self.phis = float(phis)
        self.big_s = float(big_s)
        self.fyh = float(fyh)
        self.es0 = float(es0)
        self.ha_ratio = float(ha_ratio)
        self.mu = float(mu)
        self.phi_lon = float(phi_lon)
        self.internal_args = internal_args
        self.wrap_args = wrap_args
        self.gravel = gravel
        self.silica = silica
        if tol is None:
            self.tol = None
        else:
            self.tol = float(tol)
        if max_num_iter is None:
            self.max_num_iter = None
        else:
            self.max_num_iter = int(max_num_iter)
        if epscu_limit is None:
            self.epscu_limit = None
        else:
            self.epscu_limit = float(epscu_limit)
        self.st_ratio = st_ratio
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.sec_type, self.fpc, self.ec, self.epscu_type, self.epscu_val, self.nu, self.l1, self.l2, self.l3, self.phis, self.big_s, self.fyh, self.es0, self.ha_ratio, self.mu, self.phi_lon]
        if getattr(self, 'internal_args') is not None:
            self._parameters += ['-internal', *self.internal_args]
        if getattr(self, 'wrap_args') is not None:
            self._parameters += ['-wrap', *self.wrap_args]
        if getattr(self, 'gravel'):
            self._parameters += ['-gravel']
        if getattr(self, 'silica'):
            self._parameters += ['-silica']
        if getattr(self, 'tol') is not None:
            self._parameters += ['-tol', self.tol]
        if getattr(self, 'max_num_iter') is not None:
            self._parameters += ['-maxNumIter', self.max_num_iter]
        if getattr(self, 'epscu_limit') is not None:
            self._parameters += ['-epscuLimit', self.epscu_limit]
        if getattr(self, 'st_ratio') is not None:
            self._parameters += ['-stRatio', self.st_ratio]
        self.to_process(osi)


class ConcreteD(UniaxialMaterialBase):
    """
    The ConcreteD UniaxialMaterial Class
    
    This command is used to construct a concrete material based on the Chinese design code.
    """
    op_type = 'ConcreteD'

    def __init__(self, osi, fc, epsc, ft, epst, ec, alphac, alphat, cesp=0.25, etap=1.15):
        """
        Initial method for ConcreteD

        Parameters
        ----------
        fc: float
            Concrete compressive strength
        epsc: float
            Concrete strain at corresponding to compressive strength
        ft: float
            Concrete tensile strength
        epst: float
            Concrete strain at corresponding to tensile strength
        ec: float
            Concrete initial elastic modulus
        alphac: float
            Compressive descending parameter
        alphat: float
            Tensile descending parameter
        cesp: float
            Plastic parameter, recommended values: 0.2~0.3
        etap: float
            Plastic parameter, recommended values: 1.0~1.3
        """
        self.fc = float(fc)
        self.epsc = float(epsc)
        self.ft = float(ft)
        self.epst = float(epst)
        self.ec = float(ec)
        self.alphac = float(alphac)
        self.alphat = float(alphat)
        self.cesp = float(cesp)
        self.etap = float(etap)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc, self.epsc, self.ft, self.epst, self.ec, self.alphac, self.alphat, self.cesp, self.etap]
        self.to_process(osi)


class FRPConfinedConcrete(UniaxialMaterialBase):
    """
    The FRPConfinedConcrete UniaxialMaterial Class
    
    This command is used to construct a uniaxial Megalooikonomou-Monti-Santini concrete material object with degraded
    linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength.
    """
    op_type = 'FRPConfinedConcrete'

    def __init__(self, osi, fpc1, fpc2, epsc0, big_d, c, ej, sj, tj, eju, big_s, fyl, fyh, dlong, dtrans, es, nu0, k, use_buck):
        """
        Initial method for FRPConfinedConcrete

        Parameters
        ----------
        fpc1: float
            Concrete core compressive strength.
        fpc2: float
            Concrete cover compressive strength.
        epsc0: float
            Strain corresponding to unconfined concrete strength.
        big_d: float
            Diameter of the circular section.
        c: float
            Dimension of concrete cover (until the outer edge of steel stirrups)
        ej: float
            Elastic modulus of the fiber reinforced polymer (frp) jacket.
        sj: float
            Clear spacing of the frp strips - zero if frp jacket is continuous.
        tj: float
            Total thickness of the frp jacket.
        eju: float
            Rupture strain of the frp jacket from tensile coupons.
        big_s: float
            Spacing of the steel spiral/stirrups.
        fyl: float
            Yielding strength of longitudinal steel bars.
        fyh: float
            Yielding strength of the steel spiral/stirrups.
        dlong: float
            Diameter of the longitudinal bars of the circular section.
        dtrans: float
            Diameter of the steel spiral/stirrups.
        es: float
            Elastic modulus of steel.
        nu0: float
            Initial poisson's coefficient for concrete.
        k: float
            Reduction factor for the rupture strain of the frp jacket, recommended values 0.5-0.8.
        use_buck: float
            Frp jacket failure criterion due to buckling of longitudinal compressive steel bars (0 = not                
                                       include it, 1= to include it).
        """
        self.fpc1 = float(fpc1)
        self.fpc2 = float(fpc2)
        self.epsc0 = float(epsc0)
        self.big_d = float(big_d)
        self.c = float(c)
        self.ej = float(ej)
        self.sj = float(sj)
        self.tj = float(tj)
        self.eju = float(eju)
        self.big_s = float(big_s)
        self.fyl = float(fyl)
        self.fyh = float(fyh)
        self.dlong = float(dlong)
        self.dtrans = float(dtrans)
        self.es = float(es)
        self.nu0 = float(nu0)
        self.k = float(k)
        self.use_buck = float(use_buck)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fpc1, self.fpc2, self.epsc0, self.big_d, self.c, self.ej, self.sj, self.tj, self.eju, self.big_s, self.fyl, self.fyh, self.dlong, self.dtrans, self.es, self.nu0, self.k, self.use_buck]
        self.to_process(osi)


class FRPConfinedConcrete02JacketC(UniaxialMaterialBase):
    """
    The FRPConfinedConcrete02JacketC UniaxialMaterial Class
    
    | DEVELOPED AND IMPLEMENTED BY:| Jin-Yu LU, Southeast University, Nanjing, China| Guan LIN (guanlin@polyu.edu.hk),
    Hong Kong Polytechnic University, Hong Kong, China.

    Figure 1 Hysteretic Stress-Strain Relation.. image::
    /_static/FRPConfinedConcrete02/Figure1.pngThis command is used to construct a uniaxial hysteretic
    stress-strain model for fiber-reinforced polymer (FRP)-confined concrete. The envelope
    compressive stress-strain response is described by a parabolic first portion and a
    linear second portion with smooth connection between them (Figure 1). The
    hysteretic rules of compression are based on Lam and Teng’s (2009)
    model. The cyclic linear tension model of Yassin (1994) for
    unconfined concrete (as adopted in Concrete02) is used
    with slight modifications to describe the tensile behavior of FRP-confined concrete (Teng et al. 2015).
    """
    op_type = 'FRPConfinedConcrete02'

    def __init__(self, osi, fc0, ec, ec0, tfrp, efrp, erup, big_r):
        """
        Initial method for FRPConfinedConcrete02JacketC

        Parameters
        ----------
        fc0: float
            Compressive strength of unconfined concrete (compression is negative)
        ec: float
            Elastic modulus of unconfined concrete (=4730√(-$fc0(mpa)))
        ec0: float
            Axial strain corresponding to unconfined concrete strength (≈ 0.002)
        tfrp: float
            Thickness of an frp jacket
        efrp: float
            Tensile elastic modulus of an frp jacket
        erup: float
            Hoop rupture strain of an frp jacket
        big_r: float
            Radius of circular column section
        """
        self.fc0 = float(fc0)
        self.ec = float(ec)
        self.ec0 = float(ec0)
        self.tfrp = float(tfrp)
        self.efrp = float(efrp)
        self.erup = float(erup)
        self.big_r = float(big_r)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc0, self.ec, self.ec0, '-JacketC', self.tfrp, self.efrp, self.erup, self.big_r]
        self.to_process(osi)

class FRPConfinedConcrete02Ultimate(UniaxialMaterialBase):
    """
    The FRPConfinedConcrete02Ultimate UniaxialMaterial Class
    
    | DEVELOPED AND IMPLEMENTED BY:| Jin-Yu LU, Southeast University, Nanjing, China| Guan LIN (guanlin@polyu.edu.hk),
    Hong Kong Polytechnic University, Hong Kong, China.

    Figure 1 Hysteretic Stress-Strain Relation.. image::
    /_static/FRPConfinedConcrete02/Figure1.pngThis command is used to construct a uniaxial hysteretic
    stress-strain model for fiber-reinforced polymer (FRP)-confined concrete. The envelope
    compressive stress-strain response is described by a parabolic first portion and a
    linear second portion with smooth connection between them (Figure 1). The
    hysteretic rules of compression are based on Lam and Teng’s (2009)
    model. The cyclic linear tension model of Yassin (1994) for
    unconfined concrete (as adopted in Concrete02) is used
    with slight modifications to describe the tensile behavior of FRP-confined concrete (Teng et al. 2015).
    """
    op_type = 'FRPConfinedConcrete02'

    def __init__(self, osi, fc0, ec, ec0, fcu, ecu, ft, ets, unit):
        """
        Initial method for FRPConfinedConcrete02Ultimate

        Parameters
        ----------
        fc0: float
            Compressive strength of unconfined concrete (compression is negative)
        ec: float
            Elastic modulus of unconfined concrete (=4730√(-$fc0(mpa)))
        ec0: float
            Axial strain corresponding to unconfined concrete strength (≈ 0.002)
        fcu: float
            Ultimate stress of frp-confined concrete ($fcu ≥ $fc0)
        ecu: float
            Ultimate strain of frp-confined concrete
        ft: float
            Tensile strength of unconfined concrete (=0.632√(-$fc0(mpa)))
        ets: float
            Stiffness of tensile softening (≈ 0.05 ec)
        unit: float
            Unit indicator, unit = 1 for si metric units; unit = 0 for us customary units
        """
        self.fc0 = float(fc0)
        self.ec = float(ec)
        self.ec0 = float(ec0)
        self.fcu = float(fcu)
        self.ecu = float(ecu)
        self.ft = float(ft)
        self.ets = float(ets)
        self.unit = float(unit)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc0, self.ec, self.ec0, '-Ultimate', self.fcu, self.ecu, self.ft, self.ets, self.unit]
        self.to_process(osi)


class ConcreteCM(UniaxialMaterialBase):
    """
    The ConcreteCM UniaxialMaterial Class
    
    This command is used to construct a uniaxialMaterial ConcreteCM (Kolozvari et al., 2015), which is a uniaxial
    hysteretic constitutive model for concrete developed by Chang and Mander (1994).
    """
    op_type = 'ConcreteCM'

    def __init__(self, osi, fpcc, epcc, ec, rc, xcrn, ft, et, rt, xcrp, gap_close: float=None):
        """
        Initial method for ConcreteCM

        Parameters
        ----------
        fpcc: float
            Compressive strength (:math:`f'_c`)
        epcc: float
            Strain at compressive strength (:math:`\\epsilon'_c`)
        ec: float
            Initial tangent modulus (:math:`e_c`)
        rc: float
            Shape parameter in tsai's equation defined for compression (:math:`r_c`)
        xcrn: float
            Non-dimensional critical strain on compression envelope (:math:`\\epsilon^{-}_{cr}`, where the envelope
            curve starts following a straight line)
        ft: float
            Tensile strength (:math:`f_t`)
        et: float
            Strain at tensile strength (:math:`\\epsilon_t`)
        rt: float
            Shape parameter in tsai's equation defined for tension (:math:`r_t`)
        xcrp: float
            Non-dimensional critical strain on tension envelope (:math:`\\epsilon^{+}_{cr}`, where the envelope curve
            starts following a straight line - large value [e.g., 10000] recommended when tension stiffening is considered)
        gap_close: float
            Gapclose = 0, less gradual gap closure (default); gapclose = 1, more gradual gap closure
        """
        self.fpcc = float(fpcc)
        self.epcc = float(epcc)
        self.ec = float(ec)
        self.rc = float(rc)
        self.xcrn = float(xcrn)
        self.ft = float(ft)
        self.et = float(et)
        self.rt = float(rt)
        self.xcrp = float(xcrp)
        if gap_close is None:
            self.gap_close = None
        else:
            self.gap_close = float(gap_close)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fpcc, self.epcc, self.ec, self.rc, self.xcrn, self.ft, self.et, self.rt, self.xcrp]
        if getattr(self, 'gap_close') is not None:
            self._parameters += ['-GapClose', self.gap_close]
        self.to_process(osi)


class TDConcrete(UniaxialMaterialBase):
    """
    The TDConcrete UniaxialMaterial Class
    
    This command is used to construct a uniaxial time-dependent concrete material object with linear behavior in
    compression, nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to ACI 209R-92.
    """
    op_type = 'TDConcrete'

    def __init__(self, osi, fc, fct, ec, beta, t_d, epsshu, psish, tcr, phiu, psicr1, psicr2, tcast):
        """
        Initial method for TDConcrete

        Parameters
        ----------
        fc: float
            Concrete compressive strength (compression is negative)
        fct: float
            Concrete tensile strength (tension is positive)
        ec: float
            Concrete modulus of elasticity
        beta: float
            Tension softening parameter (tension softening exponent)
        t_d: float
            Analysis time at initiation of drying (in days)
        epsshu: float
            Ultimate shrinkage strain as per aci 209r-92 (shrinkage is negative)
        psish: float
            Fitting parameter of the shrinkage time evolution function as per aci 209r-92
        tcr: float
            Creep model age (in days)
        phiu: float
            Ultimate creep coefficient as per aci 209r-92
        psicr1: float
            Fitting parameter of the creep time evolution function as per aci 209r-92
        psicr2: float
            Fitting parameter of the creep time evolution function as per aci 209r-92
        tcast: float
            Analysis time corresponding to concrete casting (in days; minimum value 2.0)
        """
        self.fc = float(fc)
        self.fct = float(fct)
        self.ec = float(ec)
        self.beta = float(beta)
        self.t_d = float(t_d)
        self.epsshu = float(epsshu)
        self.psish = float(psish)
        self.tcr = float(tcr)
        self.phiu = float(phiu)
        self.psicr1 = float(psicr1)
        self.psicr2 = float(psicr2)
        self.tcast = float(tcast)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc, self.fct, self.ec, self.beta, self.t_d, self.epsshu, self.psish, self.tcr, self.phiu, self.psicr1, self.psicr2, self.tcast]
        self.to_process(osi)


class TDConcreteEXP(UniaxialMaterialBase):
    """
    The TDConcreteEXP UniaxialMaterial Class
    
    This command is used to construct a uniaxial time-dependent concrete material object with linear behavior in
    compression, nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to ACI 209R-92.
    """
    op_type = 'TDConcreteEXP'

    def __init__(self, osi, fc, fct, ec, beta, t_d, epsshu, psish, tcr, epscru, sig_cr, psicr1, psicr2, tcast):
        """
        Initial method for TDConcreteEXP

        Parameters
        ----------
        fc: float
            Concrete compressive strength (compression is negative)
        fct: float
            Concrete tensile strength (tension is positive)
        ec: float
            Concrete modulus of elasticity
        beta: float
            Tension softening parameter (tension softening exponent)
        t_d: float
            Analysis time at initiation of drying (in days)
        epsshu: float
            Ultimate shrinkage strain as per aci 209r-92 (shrinkage is negative)
        psish: float
            Fitting parameter of the shrinkage time evolution function as per aci 209r-92
        tcr: float
            Creep model age (in days)
        epscru: float
            Ultimate creep strain (e.g., taken from experimental measurements)
        sig_cr: float
            Concrete compressive stress (input as negative) associated with $epscru (e.g., experimentally applied)
        psicr1: float
            Fitting parameter of the creep time evolution function as per aci 209r-92
        psicr2: float
            Fitting parameter of the creep time evolution function as per aci 209r-92
        tcast: float
            Analysis time corresponding to concrete casting (in days; minimum value 2.0)
        """
        self.fc = float(fc)
        self.fct = float(fct)
        self.ec = float(ec)
        self.beta = float(beta)
        self.t_d = float(t_d)
        self.epsshu = float(epsshu)
        self.psish = float(psish)
        self.tcr = float(tcr)
        self.epscru = float(epscru)
        self.sig_cr = float(sig_cr)
        self.psicr1 = float(psicr1)
        self.psicr2 = float(psicr2)
        self.tcast = float(tcast)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc, self.fct, self.ec, self.beta, self.t_d, self.epsshu, self.psish, self.tcr, self.epscru, self.sig_cr, self.psicr1, self.psicr2, self.tcast]
        self.to_process(osi)


class TDConcreteMC10(UniaxialMaterialBase):
    """
    The TDConcreteMC10 UniaxialMaterial Class
    
    This command is used to construct a uniaxial time-dependent concrete material object with linear behavior in
    compression, nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to fib
    Model Code 2010.
    """
    op_type = 'TDConcreteMC10'

    def __init__(self, osi, fc, fct, ec, ecm, beta, t_d, epsba, epsbb, epsda, epsdb, phiba, phibb, phida, phidb, tcast, cem):
        """
        Initial method for TDConcreteMC10

        Parameters
        ----------
        fc: float
            Concrete compressive strength (compression is negative)
        fct: float
            Concrete tensile strength (tension is positive)
        ec: float
            Concrete modulus of elasticity at loading age
        ecm: float
            Concrete modulus of elasticity at 28 days
        beta: float
            Tension softening parameter (tension softening exponent)
        t_d: float
            Analysis time at initiation of drying (in days)
        epsba: float
            Ultimate basic shrinkage strain (input as negative) as per fib model code 2010
        epsbb: float
            Fitting parameter of the basic shrinkage time evolution function as per fib model code 2010
        epsda: float
            Product of ultimate drying shrinkage strain and relative humidity function as per fib model code 2010
        epsdb: float
            Fitting parameter of the basic shrinkage time evolution function as per fib model code 2010
        phiba: float
            Parameter for the effect of compressive strength on basic creep as per fib model code 2010
        phibb: float
            Fitting parameter of the basic creep time evolution function as per fib model code 2010
        phida: float
            Product of the effect of compressive strength and relative humidity on drying creep as per fib model code
            2010
        phidb: float
            Fitting parameter of the drying creep time evolution function as per fib model code 2010
        tcast: float
            Analysis time corresponding to concrete casting (in days; minimum value 2.0)
        cem: float
            Coefficient dependent on the type of cement as per fib model code 2010
        """
        self.fc = float(fc)
        self.fct = float(fct)
        self.ec = float(ec)
        self.ecm = float(ecm)
        self.beta = float(beta)
        self.t_d = float(t_d)
        self.epsba = float(epsba)
        self.epsbb = float(epsbb)
        self.epsda = float(epsda)
        self.epsdb = float(epsdb)
        self.phiba = float(phiba)
        self.phibb = float(phibb)
        self.phida = float(phida)
        self.phidb = float(phidb)
        self.tcast = float(tcast)
        self.cem = float(cem)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc, self.fct, self.ec, self.ecm, self.beta, self.t_d, self.epsba, self.epsbb, self.epsda, self.epsdb, self.phiba, self.phibb, self.phida, self.phidb, self.tcast, self.cem]
        self.to_process(osi)


class TDConcreteMC10NL(UniaxialMaterialBase):
    """
    The TDConcreteMC10NL UniaxialMaterial Class
    
    This command is used to construct a uniaxial time-dependent concrete material object with non-linear behavior in
    compression (REF: Concrete02), nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage
    according to fib Model Code 2010.
    """
    op_type = 'TDConcreteMC10NL'

    def __init__(self, osi, fc, fcu, epscu, fct, ec, ecm, beta, t_d, epsba, epsbb, epsda, epsdb, phiba, phibb, phida, phidb, tcast, cem):
        """
        Initial method for TDConcreteMC10NL

        Parameters
        ----------
        fc: float
            Concrete compressive strength (compression is negative)
        fcu: float
            Concrete crushing strength (compression is negative)
        epscu: float
            Concrete strain at crushing strength (input as negative)
        fct: float
            Concrete tensile strength (tension is positive)
        ec: float
            Concrete modulus of elasticity at loading age
        ecm: float
            Concrete modulus of elasticity at 28 days
        beta: float
            Tension softening parameter (tension softening exponent)
        t_d: float
            Analysis time at initiation of drying (in days)
        epsba: float
            Ultimate basic shrinkage strain (input as negative) as per fib model code 2010
        epsbb: float
            Fitting parameter of the basic shrinkage time evolution function as per fib model code 2010
        epsda: float
            Product of ultimate drying shrinkage strain and relative humidity function as per fib model code 2010
        epsdb: float
            Fitting parameter of the basic shrinkage time evolution function as per fib model code 2010
        phiba: float
            Parameter for the effect of compressive strength on basic creep as per fib model code 2010
        phibb: float
            Fitting parameter of the basic creep time evolution function as per fib model code 2010
        phida: float
            Product of the effect of compressive strength and relative humidity on drying creep as per fib model code
            2010
        phidb: float
            Fitting parameter of the drying creep time evolution function as per fib model code 2010
        tcast: float
            Analysis time corresponding to concrete casting (in days; minimum value 2.0)
        cem: float
            Coefficient dependent on the type of cement as per fib model code 2010
        """
        self.fc = float(fc)
        self.fcu = float(fcu)
        self.epscu = float(epscu)
        self.fct = float(fct)
        self.ec = float(ec)
        self.ecm = float(ecm)
        self.beta = float(beta)
        self.t_d = float(t_d)
        self.epsba = float(epsba)
        self.epsbb = float(epsbb)
        self.epsda = float(epsda)
        self.epsdb = float(epsdb)
        self.phiba = float(phiba)
        self.phibb = float(phibb)
        self.phida = float(phida)
        self.phidb = float(phidb)
        self.tcast = float(tcast)
        self.cem = float(cem)
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.fc, self.fcu, self.epscu, self.fct, self.ec, self.ecm, self.beta, self.t_d, self.epsba, self.epsbb, self.epsda, self.epsdb, self.phiba, self.phibb, self.phida, self.phidb, self.tcast, self.cem]
        self.to_process(osi)
