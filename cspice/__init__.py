# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_cspice')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_cspice')
    _cspice = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cspice', [dirname(__file__)])
        except ImportError:
            import _cspice
            return _cspice
        try:
            _mod = imp.load_module('_cspice', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _cspice = swig_import_helper()
    del swig_import_helper
else:
    import _cspice
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def axisar(axis, angle):
    """axisar(double [3] axis, double angle)"""
    return _cspice.axisar(axis, angle)

def b1900():
    """b1900() -> double"""
    return _cspice.b1900()

def b1950():
    """b1950() -> double"""
    return _cspice.b1950()

def bodc2n(code):
    """bodc2n(int code)"""
    return _cspice.bodc2n(code)

def boddef(CONST_STRING, code):
    """boddef(char * CONST_STRING, int code)"""
    return _cspice.boddef(CONST_STRING, code)

def bodfnd(body, CONST_STRING):
    """bodfnd(int body, char * CONST_STRING) -> int"""
    return _cspice.bodfnd(body, CONST_STRING)

def bodn2c(CONST_STRING):
    """bodn2c(char * CONST_STRING)"""
    return _cspice.bodn2c(CONST_STRING)

def bods2c(CONST_STRING):
    """bods2c(char * CONST_STRING)"""
    return _cspice.bods2c(CONST_STRING)

def bodvcd(bodyid, CONST_STRING):
    """bodvcd(int bodyid, char * CONST_STRING)"""
    return _cspice.bodvcd(bodyid, CONST_STRING)

def bodvrd(arg1, arg2):
    """bodvrd(char * arg1, char * arg2)"""
    return _cspice.bodvrd(arg1, arg2)

def cgv2el(center, vec1, vec2):
    """cgv2el(double [3] center, double [3] vec1, double [3] vec2)"""
    return _cspice.cgv2el(center, vec1, vec2)

def cidfrm(cent):
    """cidfrm(int cent)"""
    return _cspice.cidfrm(cent)

def ckcov(ck, idcode, needav, level, tol, timsys):
    """ckcov(char * ck, int idcode, int needav, char * level, double tol, char * timsys)"""
    return _cspice.ckcov(ck, idcode, needav, level, tol, timsys)

def ckgp(inst, sclkdp, tol, CONST_STRING):
    """ckgp(int inst, double sclkdp, double tol, char * CONST_STRING)"""
    return _cspice.ckgp(inst, sclkdp, tol, CONST_STRING)

def ckgpav(inst, sclkdp, tol, CONST_STRING):
    """ckgpav(int inst, double sclkdp, double tol, char * CONST_STRING)"""
    return _cspice.ckgpav(inst, sclkdp, tol, CONST_STRING)

def ckobj(ck):
    """ckobj(char * ck)"""
    return _cspice.ckobj(ck)

def clight():
    """clight() -> double"""
    return _cspice.clight()

def clpool():
    """clpool()"""
    return _cspice.clpool()

def cnmfrm(cname):
    """cnmfrm(char * cname)"""
    return _cspice.cnmfrm(cname)

def conics(elts, et):
    """conics(double [8] elts, double et)"""
    return _cspice.conics(elts, et)

def convrt(x, arg2, arg3):
    """convrt(double x, char * arg2, char * arg3)"""
    return _cspice.convrt(x, arg2, arg3)

def cyllat(r, lonc, z):
    """cyllat(double r, double lonc, double z)"""
    return _cspice.cyllat(r, lonc, z)

def cylrec(r, lon, z):
    """cylrec(double r, double lon, double z)"""
    return _cspice.cylrec(r, lon, z)

def cylsph(r, lonc, z):
    """cylsph(double r, double lonc, double z)"""
    return _cspice.cylsph(r, lonc, z)

def dcyldr(x, y, z):
    """dcyldr(double x, double y, double z)"""
    return _cspice.dcyldr(x, y, z)

def deltet(epoch, CONST_STRING):
    """deltet(double epoch, char * CONST_STRING)"""
    return _cspice.deltet(epoch, CONST_STRING)

def det(m1):
    """det(double [3][3] m1) -> double"""
    return _cspice.det(m1)

def dgeodr(x, y, z, re, f):
    """dgeodr(double x, double y, double z, double re, double f)"""
    return _cspice.dgeodr(x, y, z, re, f)

def diags2(symmat):
    """diags2(double [2][2] symmat)"""
    return _cspice.diags2(symmat)

def dlatdr(x, y, z):
    """dlatdr(double x, double y, double z)"""
    return _cspice.dlatdr(x, y, z)

def dpgrdr(CONST_STRING, x, y, z, re, f):
    """dpgrdr(char * CONST_STRING, double x, double y, double z, double re, double f)"""
    return _cspice.dpgrdr(CONST_STRING, x, y, z, re, f)

def dpmax():
    """dpmax() -> double"""
    return _cspice.dpmax()

def dpmin():
    """dpmin() -> double"""
    return _cspice.dpmin()

def dpr():
    """dpr() -> double"""
    return _cspice.dpr()

def drdcyl(r, lon, z):
    """drdcyl(double r, double lon, double z)"""
    return _cspice.drdcyl(r, lon, z)

def drdgeo(lon, lat, alt, re, f):
    """drdgeo(double lon, double lat, double alt, double re, double f)"""
    return _cspice.drdgeo(lon, lat, alt, re, f)

def drdlat(r, lon, lat):
    """drdlat(double r, double lon, double lat)"""
    return _cspice.drdlat(r, lon, lat)

def drdpgr(CONST_STRING, lon, lat, alt, re, f):
    """drdpgr(char * CONST_STRING, double lon, double lat, double alt, double re, double f)"""
    return _cspice.drdpgr(CONST_STRING, lon, lat, alt, re, f)

def drdsph(r, colat, lon):
    """drdsph(double r, double colat, double lon)"""
    return _cspice.drdsph(r, colat, lon)

def dsphdr(x, y, z):
    """dsphdr(double x, double y, double z)"""
    return _cspice.dsphdr(x, y, z)

def dtpool(CONST_STRING):
    """dtpool(char * CONST_STRING)"""
    return _cspice.dtpool(CONST_STRING)

def dvdot(s1, s2):
    """dvdot(double [6] s1, double [6] s2) -> double"""
    return _cspice.dvdot(s1, s2)

def dvhat(s1):
    """dvhat(double [6] s1)"""
    return _cspice.dvhat(s1)

def edlimb(a, b, c, viewpt):
    """edlimb(double a, double b, double c, double [3] viewpt)"""
    return _cspice.edlimb(a, b, c, viewpt)

def el2cgv(ellipse):
    """el2cgv(double [NELLIPSE] ellipse)"""
    return _cspice.el2cgv(ellipse)

def erract(CONST_STRING, lenout):
    """erract(char * CONST_STRING, int lenout)"""
    return _cspice.erract(CONST_STRING, lenout)

def errch(arg1, arg2):
    """errch(char * arg1, char * arg2)"""
    return _cspice.errch(arg1, arg2)

def errdev(CONST_STRING, lenout):
    """errdev(char * CONST_STRING, int lenout)"""
    return _cspice.errdev(CONST_STRING, lenout)

def errdp(CONST_STRING, number):
    """errdp(char * CONST_STRING, double number)"""
    return _cspice.errdp(CONST_STRING, number)

def errint(CONST_STRING, number):
    """errint(char * CONST_STRING, int number)"""
    return _cspice.errint(CONST_STRING, number)

def errprt(CONST_STRING, lenout):
    """errprt(char * CONST_STRING, int lenout)"""
    return _cspice.errprt(CONST_STRING, lenout)

def et2lst(et, body, lon, type, hr, mn, sc):
    """et2lst(double et, int body, double lon, char * type, int * hr, int * mn, int * sc)"""
    return _cspice.et2lst(et, body, lon, type, hr, mn, sc)

def et2utc(et, CONST_STRING, prec):
    """et2utc(double et, char * CONST_STRING, int prec)"""
    return _cspice.et2utc(et, CONST_STRING, prec)

def etcal(et):
    """etcal(double et)"""
    return _cspice.etcal(et)

def eul2m(angle3, angle2, angle1, axis3, axis2, axis1):
    """eul2m(double angle3, double angle2, double angle1, int axis3, int axis2, int axis1)"""
    return _cspice.eul2m(angle3, angle2, angle1, axis3, axis2, axis1)

def eul2xf(eulang, axisa, axisb, axisc):
    """eul2xf(double [6] eulang, int axisa, int axisb, int axisc)"""
    return _cspice.eul2xf(eulang, axisa, axisb, axisc)

def expool(CONST_STRING):
    """expool(char * CONST_STRING)"""
    return _cspice.expool(CONST_STRING)

def failed():
    """failed() -> int"""
    return _cspice.failed()

def frame(xin):
    """frame(double [3] xin)"""
    return _cspice.frame(xin)

def frinfo(frcode):
    """frinfo(int frcode)"""
    return _cspice.frinfo(frcode)

def frmchg(frame1, frame2, et):
    """frmchg(int frame1, int frame2, double et)"""
    return _cspice.frmchg(frame1, frame2, et)

def frmchg_(frame1, frame2, et, xform):
    """frmchg_(int * frame1, int * frame2, double * et, double * xform)"""
    return _cspice.frmchg_(frame1, frame2, et, xform)

def frmnam(frcode):
    """frmnam(int frcode)"""
    return _cspice.frmnam(frcode)

def furnsh(CONST_STRING):
    """furnsh(char * CONST_STRING)"""
    return _cspice.furnsh(CONST_STRING)

def gcpool(CONST_STRING, start):
    """gcpool(char * CONST_STRING, int start)"""
    return _cspice.gcpool(CONST_STRING, start)

def gdpool(CONST_STRING, start):
    """gdpool(char * CONST_STRING, int start)"""
    return _cspice.gdpool(CONST_STRING, start)

def georec(lon, lat, alt, re, f):
    """georec(double lon, double lat, double alt, double re, double f)"""
    return _cspice.georec(lon, lat, alt, re, f)

def getfov(instid, room, n, bounds):
    """getfov(int instid, int room, int * n, double [100][3] bounds)"""
    return _cspice.getfov(instid, room, n, bounds)

def getmsg(CONST_STRING):
    """getmsg(char * CONST_STRING)"""
    return _cspice.getmsg(CONST_STRING)

def gipool(CONST_STRING, start):
    """gipool(char * CONST_STRING, int start)"""
    return _cspice.gipool(CONST_STRING, start)

def gnpool(CONST_STRING, start):
    """gnpool(char * CONST_STRING, int start)"""
    return _cspice.gnpool(CONST_STRING, start)

def halfpi():
    """halfpi() -> double"""
    return _cspice.halfpi()

def ident():
    """ident()"""
    return _cspice.ident()

def illum(arg1, et, arg3, arg4, spoint):
    """illum(char * arg1, double et, char * arg3, char * arg4, double [3] spoint)"""
    return _cspice.illum(arg1, et, arg3, arg4, spoint)

def inedpl(a, b, c, plane):
    """inedpl(double a, double b, double c, double [NPLANE] plane)"""
    return _cspice.inedpl(a, b, c, plane)

def inelpl(ellipse, plane):
    """inelpl(double [NELLIPSE] ellipse, double [NPLANE] plane)"""
    return _cspice.inelpl(ellipse, plane)

def inrypl(vertex, dir, plane):
    """inrypl(double [3] vertex, double [3] dir, double [NPLANE] plane)"""
    return _cspice.inrypl(vertex, dir, plane)

def intmax():
    """intmax() -> int"""
    return _cspice.intmax()

def intmin():
    """intmin() -> int"""
    return _cspice.intmin()

def invert(m1):
    """invert(double [3][3] m1)"""
    return _cspice.invert(m1)

def invort(m):
    """invort(double [3][3] m)"""
    return _cspice.invort(m)

def isrot(m, ntol, dtol):
    """isrot(double [3][3] m, double ntol, double dtol) -> int"""
    return _cspice.isrot(m, ntol, dtol)

def j1900():
    """j1900() -> double"""
    return _cspice.j1900()

def j1950():
    """j1950() -> double"""
    return _cspice.j1950()

def j2000():
    """j2000() -> double"""
    return _cspice.j2000()

def j2100():
    """j2100() -> double"""
    return _cspice.j2100()

def jyear():
    """jyear() -> double"""
    return _cspice.jyear()

def latcyl(radius, lon, lat):
    """latcyl(double radius, double lon, double lat)"""
    return _cspice.latcyl(radius, lon, lat)

def latrec(radius, longitude, latitude):
    """latrec(double radius, double longitude, double latitude)"""
    return _cspice.latrec(radius, longitude, latitude)

def latsph(radius, lon, lat):
    """latsph(double radius, double lon, double lat)"""
    return _cspice.latsph(radius, lon, lat)

def ldpool(CONST_STRING):
    """ldpool(char * CONST_STRING)"""
    return _cspice.ldpool(CONST_STRING)

def lspcn(arg1, et, arg3):
    """lspcn(char * arg1, double et, char * arg3) -> double"""
    return _cspice.lspcn(arg1, et, arg3)

def ltime(etobs, obs, CONST_STRING, targ):
    """ltime(double etobs, int obs, char * CONST_STRING, int targ)"""
    return _cspice.ltime(etobs, obs, CONST_STRING, targ)

def m2eul(rin, axis3, axis2, axis1):
    """m2eul(double [3][3] rin, int axis3, int axis2, int axis1)"""
    return _cspice.m2eul(rin, axis3, axis2, axis1)

def m2q(rin):
    """m2q(double [3][3] rin)"""
    return _cspice.m2q(rin)

def mequ(m1):
    """mequ(double [3][3] m1)"""
    return _cspice.mequ(m1)

def mequg(m1, mout, nr_vout, nc_vout):
    """mequg(double * m1, double ** mout, int * nr_vout, int * nc_vout)"""
    return _cspice.mequg(m1, mout, nr_vout, nc_vout)

def mtxm(m1, m2):
    """mtxm(double [3][3] m1, double [3][3] m2)"""
    return _cspice.mtxm(m1, m2)

def mtxmg(m1, m2):
    """mtxmg(double * m1, double * m2)"""
    return _cspice.mtxmg(m1, m2)

def mtxv(m1, vin):
    """mtxv(double [3][3] m1, double [3] vin)"""
    return _cspice.mtxv(m1, vin)

def mtxvg(m1, v2):
    """mtxvg(double * m1, double * v2)"""
    return _cspice.mtxvg(m1, v2)

def mxm(m1, m2):
    """mxm(double [3][3] m1, double [3][3] m2)"""
    return _cspice.mxm(m1, m2)

def mxmg(m1, m2):
    """mxmg(double * m1, double * m2)"""
    return _cspice.mxmg(m1, m2)

def mxmt(m1, m2):
    """mxmt(double [3][3] m1, double [3][3] m2)"""
    return _cspice.mxmt(m1, m2)

def mxmtg(m1, m2):
    """mxmtg(double * m1, double * m2)"""
    return _cspice.mxmtg(m1, m2)

def mxv(m1, vin):
    """mxv(double [3][3] m1, double [3] vin)"""
    return _cspice.mxv(m1, vin)

def mxvg(m1, v2):
    """mxvg(double * m1, double * v2)"""
    return _cspice.mxvg(m1, v2)

def namfrm(CONST_STRING):
    """namfrm(char * CONST_STRING)"""
    return _cspice.namfrm(CONST_STRING)

def nearpt(positn, a, b, c):
    """nearpt(double [3] positn, double a, double b, double c)"""
    return _cspice.nearpt(positn, a, b, c)

def npedln(a, b, c, linept, linedr):
    """npedln(double a, double b, double c, double [3] linept, double [3] linedr)"""
    return _cspice.npedln(a, b, c, linept, linedr)

def npelpt(point):
    """npelpt(double [3] point)"""
    return _cspice.npelpt(point)

def nplnpt(linpt, lindir, point):
    """nplnpt(double [3] linpt, double [3] lindir, double [3] point)"""
    return _cspice.nplnpt(linpt, lindir, point)

def nvc2pl(normal, constant):
    """nvc2pl(double [3] normal, double constant)"""
    return _cspice.nvc2pl(normal, constant)

def nvp2pl(normal, point):
    """nvp2pl(double [3] normal, double [3] point)"""
    return _cspice.nvp2pl(normal, point)

def oscelt(state, et, mu):
    """oscelt(double [6] state, double et, double mu)"""
    return _cspice.oscelt(state, et, mu)

def pcpool(CONST_STRING, n):
    """pcpool(char * CONST_STRING, int n)"""
    return _cspice.pcpool(CONST_STRING, n)

def pdpool(CONST_STRING, n):
    """pdpool(char * CONST_STRING, int n)"""
    return _cspice.pdpool(CONST_STRING, n)

def pgrrec(CONST_STRING, lon, lat, alt, re, f):
    """pgrrec(char * CONST_STRING, double lon, double lat, double alt, double re, double f)"""
    return _cspice.pgrrec(CONST_STRING, lon, lat, alt, re, f)

def pi():
    """pi() -> double"""
    return _cspice.pi()

def pipool(CONST_STRING, n):
    """pipool(char * CONST_STRING, int n)"""
    return _cspice.pipool(CONST_STRING, n)

def pjelpl(elin, plane):
    """pjelpl(double [NELLIPSE] elin, double [NPLANE] plane)"""
    return _cspice.pjelpl(elin, plane)

def pl2nvc(plane, normal):
    """pl2nvc(double [NPLANE] plane, double [3] normal)"""
    return _cspice.pl2nvc(plane, normal)

def pl2nvp(plane):
    """pl2nvp(double [NPLANE] plane)"""
    return _cspice.pl2nvp(plane)

def pl2psv(plane):
    """pl2psv(double [NPLANE] plane)"""
    return _cspice.pl2psv(plane)

def prop2b(gm, pvinit, dt):
    """prop2b(double gm, double [6] pvinit, double dt)"""
    return _cspice.prop2b(gm, pvinit, dt)

def psv2pl(point, span1, span2):
    """psv2pl(double [3] point, double [3] span1, double [3] span2)"""
    return _cspice.psv2pl(point, span1, span2)

def pxform(arg1, arg2, et):
    """pxform(char * arg1, char * arg2, double et)"""
    return _cspice.pxform(arg1, arg2, et)

def q2m(qin):
    """q2m(double [4] qin)"""
    return _cspice.q2m(qin)

def qdq2av(qin, dq):
    """qdq2av(double [4] qin, double [4] dq)"""
    return _cspice.qdq2av(qin, dq)

def qxq(q1, q2):
    """qxq(double [4] q1, double [4] q2)"""
    return _cspice.qxq(q1, q2)

def radrec(range, ra, dec):
    """radrec(double range, double ra, double dec)"""
    return _cspice.radrec(range, ra, dec)

def rav2xf(rot, av):
    """rav2xf(double [3][3] rot, double [3] av)"""
    return _cspice.rav2xf(rot, av)

def raxisa(matrix):
    """raxisa(double [3][3] matrix)"""
    return _cspice.raxisa(matrix)

def reccyl(rectan1):
    """reccyl(double [3] rectan1)"""
    return _cspice.reccyl(rectan1)

def recgeo(rectan1, re, f):
    """recgeo(double [3] rectan1, double re, double f)"""
    return _cspice.recgeo(rectan1, re, f)

def reclat(rectan1):
    """reclat(double [3] rectan1)"""
    return _cspice.reclat(rectan1)

def recpgr(CONST_STRING, rectan1, re, f):
    """recpgr(char * CONST_STRING, double [3] rectan1, double re, double f)"""
    return _cspice.recpgr(CONST_STRING, rectan1, re, f)

def recrad(rectan):
    """recrad(double [3] rectan)"""
    return _cspice.recrad(rectan)

def recsph(rectan):
    """recsph(double [3] rectan)"""
    return _cspice.recsph(rectan)

def refchg(frame1, frame2, et):
    """refchg(int frame1, int frame2, double et)"""
    return _cspice.refchg(frame1, frame2, et)

def refchg_(frame1, frame2, et, rotate):
    """refchg_(int * frame1, int * frame2, double * et, double * rotate)"""
    return _cspice.refchg_(frame1, frame2, et, rotate)

def repmc(arg1, arg2, arg3):
    """repmc(char * arg1, char * arg2, char * arg3)"""
    return _cspice.repmc(arg1, arg2, arg3)

def repmct(arg1, arg2, value, IN_STRING):
    """repmct(char * arg1, char * arg2, int value, char IN_STRING)"""
    return _cspice.repmct(arg1, arg2, value, IN_STRING)

def repmd(arg1, arg2, value, sigdig):
    """repmd(char * arg1, char * arg2, double value, int sigdig)"""
    return _cspice.repmd(arg1, arg2, value, sigdig)

def repmf(arg1, arg2, value, sigdig, format):
    """repmf(char * arg1, char * arg2, double value, int sigdig, char format)"""
    return _cspice.repmf(arg1, arg2, value, sigdig, format)

def repmi(arg1, arg2, value, lenout, out):
    """repmi(char * arg1, char * arg2, int value, int lenout, char * out)"""
    return _cspice.repmi(arg1, arg2, value, lenout, out)

def repmot(arg1, arg2, value, IN_STRING):
    """repmot(char * arg1, char * arg2, int value, char IN_STRING)"""
    return _cspice.repmot(arg1, arg2, value, IN_STRING)

def reset():
    """reset()"""
    return _cspice.reset()

def rotate(angle, iaxis):
    """rotate(double angle, int iaxis)"""
    return _cspice.rotate(angle, iaxis)

def rotmat(m1, angle, iaxis):
    """rotmat(double [3][3] m1, double angle, int iaxis)"""
    return _cspice.rotmat(m1, angle, iaxis)

def rotvec(v1, angle, iaxis):
    """rotvec(double [3] v1, double angle, int iaxis)"""
    return _cspice.rotvec(v1, angle, iaxis)

def rpd():
    """rpd() -> double"""
    return _cspice.rpd()

def rquad(a, b, c):
    """rquad(double a, double b, double c)"""
    return _cspice.rquad(a, b, c)

def saelgv(vec1, vec2):
    """saelgv(double [3] vec1, double [3] vec2)"""
    return _cspice.saelgv(vec1, vec2)

def scdecd(sc, sclkdp):
    """scdecd(int sc, double sclkdp)"""
    return _cspice.scdecd(sc, sclkdp)

def sce2c(sc, et):
    """sce2c(int sc, double et)"""
    return _cspice.sce2c(sc, et)

def sce2s(sc, et):
    """sce2s(int sc, double et)"""
    return _cspice.sce2s(sc, et)

def sce2t(sc, et):
    """sce2t(int sc, double et)"""
    return _cspice.sce2t(sc, et)

def scencd(sc, CONST_STRING):
    """scencd(int sc, char * CONST_STRING)"""
    return _cspice.scencd(sc, CONST_STRING)

def scfmt(sc, ticks):
    """scfmt(int sc, double ticks)"""
    return _cspice.scfmt(sc, ticks)

def scpart(sc):
    """scpart(int sc)"""
    return _cspice.scpart(sc)

def scs2e(sc, CONST_STRING):
    """scs2e(int sc, char * CONST_STRING)"""
    return _cspice.scs2e(sc, CONST_STRING)

def sct2e(sc, sclkdp):
    """sct2e(int sc, double sclkdp)"""
    return _cspice.sct2e(sc, sclkdp)

def sctiks(sc, CONST_STRING):
    """sctiks(int sc, char * CONST_STRING)"""
    return _cspice.sctiks(sc, CONST_STRING)

def setmsg(CONST_STRING):
    """setmsg(char * CONST_STRING)"""
    return _cspice.setmsg(CONST_STRING)

def sigerr(CONST_STRING):
    """sigerr(char * CONST_STRING)"""
    return _cspice.sigerr(CONST_STRING)

def spd():
    """spd() -> double"""
    return _cspice.spd()

def sphcyl(radius, colat, slon):
    """sphcyl(double radius, double colat, double slon)"""
    return _cspice.sphcyl(radius, colat, slon)

def sphlat(r, colat, lons):
    """sphlat(double r, double colat, double lons)"""
    return _cspice.sphlat(r, colat, lons)

def sphrec(r, colat, lon):
    """sphrec(double r, double colat, double lon)"""
    return _cspice.sphrec(r, colat, lon)

def spkapo(targ, et, arg3, sobs, arg5):
    """spkapo(int targ, double et, char * arg3, double [6] sobs, char * arg5)"""
    return _cspice.spkapo(targ, et, arg3, sobs, arg5)

def spkapp(targ, et, arg3, sobs, arg5):
    """spkapp(int targ, double et, char * arg3, double [6] sobs, char * arg5)"""
    return _cspice.spkapp(targ, et, arg3, sobs, arg5)

def spkcov(spk, idcode):
    """spkcov(char * spk, int idcode)"""
    return _cspice.spkcov(spk, idcode)

def spkez(targ, et, arg3, arg4, obs):
    """spkez(int targ, double et, char * arg3, char * arg4, int obs)"""
    return _cspice.spkez(targ, et, arg3, arg4, obs)

def spkez_vector(targ, et, ref, abcorr, obs):
    """spkez_vector(int targ, double * et, char * ref, char * abcorr, int obs)"""
    return _cspice.spkez_vector(targ, et, ref, abcorr, obs)

def spkezp(targ, et, arg3, arg4, obs):
    """spkezp(int targ, double et, char * arg3, char * arg4, int obs)"""
    return _cspice.spkezp(targ, et, arg3, arg4, obs)

def spkezr(arg1, et, arg3, arg4, arg5):
    """spkezr(char * arg1, double et, char * arg3, char * arg4, char * arg5)"""
    return _cspice.spkezr(arg1, et, arg3, arg4, arg5)

def spkgeo(targ, et, CONST_STRING, obs):
    """spkgeo(int targ, double et, char * CONST_STRING, int obs)"""
    return _cspice.spkgeo(targ, et, CONST_STRING, obs)

def spkgps(targ, et, CONST_STRING, obs):
    """spkgps(int targ, double et, char * CONST_STRING, int obs)"""
    return _cspice.spkgps(targ, et, CONST_STRING, obs)

def spkobj(spk):
    """spkobj(char * spk)"""
    return _cspice.spkobj(spk)

def spkpos(arg1, et, arg3, arg4, arg5):
    """spkpos(char * arg1, double et, char * arg3, char * arg4, char * arg5)"""
    return _cspice.spkpos(arg1, et, arg3, arg4, arg5)

def spkssb(targ, et, CONST_STRING):
    """spkssb(int targ, double et, char * CONST_STRING)"""
    return _cspice.spkssb(targ, et, CONST_STRING)

def srfrec(body, longitude, latitude):
    """srfrec(int body, double longitude, double latitude)"""
    return _cspice.srfrec(body, longitude, latitude)

def srfxpt(arg1, arg2, et, arg4, arg5, arg6, dvec):
    """srfxpt(char * arg1, char * arg2, double et, char * arg4, char * arg5, char * arg6, double [3] dvec)"""
    return _cspice.srfxpt(arg1, arg2, et, arg4, arg5, arg6, dvec)

def stcf01(catnam, westra, eastra, sthdec, nthdec):
    """stcf01(char * catnam, double westra, double eastra, double sthdec, double nthdec)"""
    return _cspice.stcf01(catnam, westra, eastra, sthdec, nthdec)

def stcg01(index):
    """stcg01(int index)"""
    return _cspice.stcg01(index)

def stcl01(catfnm):
    """stcl01(char * catfnm)"""
    return _cspice.stcl01(catfnm)

def stelab(pobj, vobs):
    """stelab(double [3] pobj, double [3] vobs)"""
    return _cspice.stelab(pobj, vobs)

def stlabx(pobj, vobs):
    """stlabx(double [3] pobj, double [3] vobs)"""
    return _cspice.stlabx(pobj, vobs)

def stpool(arg1, nth, arg3):
    """stpool(char * arg1, int nth, char * arg3)"""
    return _cspice.stpool(arg1, nth, arg3)

def str2et(CONST_STRING):
    """str2et(char * CONST_STRING)"""
    return _cspice.str2et(CONST_STRING)

def subpt(arg1, arg2, et, arg4, arg5):
    """subpt(char * arg1, char * arg2, double et, char * arg4, char * arg5)"""
    return _cspice.subpt(arg1, arg2, et, arg4, arg5)

def subsol(arg1, arg2, et, arg4, arg5):
    """subsol(char * arg1, char * arg2, double et, char * arg4, char * arg5)"""
    return _cspice.subsol(arg1, arg2, et, arg4, arg5)

def surfnm(a, b, c, point):
    """surfnm(double a, double b, double c, double [3] point)"""
    return _cspice.surfnm(a, b, c, point)

def surfpt(positn, u, a, b, c):
    """surfpt(double [3] positn, double [3] u, double a, double b, double c)"""
    return _cspice.surfpt(positn, u, a, b, c)

def sxform(arg1, arg2, et):
    """sxform(char * arg1, char * arg2, double et)"""
    return _cspice.sxform(arg1, arg2, et)

def sxform_vector(_from, to, et):
    """sxform_vector(char * _from, char * to, double * et)"""
    return _cspice.sxform_vector(_from, to, et)

def timdef(arg1, arg2, lenout):
    """timdef(char * arg1, char * arg2, int lenout)"""
    return _cspice.timdef(arg1, arg2, lenout)

def timout(et, CONST_STRING):
    """timout(double et, char * CONST_STRING)"""
    return _cspice.timout(et, CONST_STRING)

def tipbod(CONST_STRING, body, et):
    """tipbod(char * CONST_STRING, int body, double et)"""
    return _cspice.tipbod(CONST_STRING, body, et)

def tisbod(CONST_STRING, body, et):
    """tisbod(char * CONST_STRING, int body, double et)"""
    return _cspice.tisbod(CONST_STRING, body, et)

def tkvrsn(CONST_STRING):
    """tkvrsn(char * CONST_STRING) -> char *"""
    return _cspice.tkvrsn(CONST_STRING)

def tparse(string):
    """tparse(char * string)"""
    return _cspice.tparse(string)

def tpictr(sample):
    """tpictr(char * sample)"""
    return _cspice.tpictr(sample)

def trace(matrix):
    """trace(double [3][3] matrix) -> double"""
    return _cspice.trace(matrix)

def trcoff():
    """trcoff()"""
    return _cspice.trcoff()

def tsetyr(year):
    """tsetyr(int year)"""
    return _cspice.tsetyr(year)

def twopi():
    """twopi() -> double"""
    return _cspice.twopi()

def twovec(axdef, indexa, plndef, indexp):
    """twovec(double [3] axdef, int indexa, double [3] plndef, int indexp)"""
    return _cspice.twovec(axdef, indexa, plndef, indexp)

def tyear():
    """tyear() -> double"""
    return _cspice.tyear()

def ucrss(v1, v2):
    """ucrss(double [3] v1, double [3] v2)"""
    return _cspice.ucrss(v1, v2)

def unitim(epoch, arg2, arg3):
    """unitim(double epoch, char * arg2, char * arg3) -> double"""
    return _cspice.unitim(epoch, arg2, arg3)

def unload(CONST_STRING):
    """unload(char * CONST_STRING)"""
    return _cspice.unload(CONST_STRING)

def unorm(v1):
    """unorm(double [3] v1)"""
    return _cspice.unorm(v1)

def unormg(v1):
    """unormg(double * v1)"""
    return _cspice.unormg(v1)

def utc2et(CONST_STRING):
    """utc2et(char const * CONST_STRING)"""
    return _cspice.utc2et(CONST_STRING)

def vadd(v1, v2):
    """vadd(double [3] v1, double [3] v2)"""
    return _cspice.vadd(v1, v2)

def vaddg(v1, v2):
    """vaddg(double * v1, double * v2)"""
    return _cspice.vaddg(v1, v2)

def vcrss(v1, v2):
    """vcrss(double [3] v1, double [3] v2)"""
    return _cspice.vcrss(v1, v2)

def vdist(v1, v2):
    """vdist(double [3] v1, double [3] v2) -> double"""
    return _cspice.vdist(v1, v2)

def vdistg(v1, v2):
    """vdistg(double * v1, double * v2) -> double"""
    return _cspice.vdistg(v1, v2)

def vdot(v1, v2):
    """vdot(double [3] v1, double [3] v2) -> double"""
    return _cspice.vdot(v1, v2)

def vdotg(v1, v2):
    """vdotg(double * v1, double * v2) -> double"""
    return _cspice.vdotg(v1, v2)

def vequ(vin):
    """vequ(double [3] vin)"""
    return _cspice.vequ(vin)

def vequg(v1):
    """vequg(double * v1)"""
    return _cspice.vequg(v1)

def vhat(v1):
    """vhat(double [3] v1)"""
    return _cspice.vhat(v1)

def vhatg(v1):
    """vhatg(double * v1)"""
    return _cspice.vhatg(v1)

def vlcom3(a, v1, b, v2, c, v3):
    """vlcom3(double a, double [3] v1, double b, double [3] v2, double c, double [3] v3)"""
    return _cspice.vlcom3(a, v1, b, v2, c, v3)

def vlcom(a, v1, b, v2):
    """vlcom(double a, double [3] v1, double b, double [3] v2)"""
    return _cspice.vlcom(a, v1, b, v2)

def vlcomg(a, v1, b, v2):
    """vlcomg(double a, double * v1, double b, double * v2)"""
    return _cspice.vlcomg(a, v1, b, v2)

def vminug(v1):
    """vminug(double * v1)"""
    return _cspice.vminug(v1)

def vminus(v1):
    """vminus(double [3] v1)"""
    return _cspice.vminus(v1)

def vnorm(v1):
    """vnorm(double [3] v1) -> double"""
    return _cspice.vnorm(v1)

def vnormg(v1):
    """vnormg(double * v1) -> double"""
    return _cspice.vnormg(v1)

def vpack(x, y, z):
    """vpack(double x, double y, double z)"""
    return _cspice.vpack(x, y, z)

def vperp(a, b):
    """vperp(double [3] a, double [3] b)"""
    return _cspice.vperp(a, b)

def vprjp(vin, plane):
    """vprjp(double [3] vin, double [NPLANE] plane)"""
    return _cspice.vprjp(vin, plane)

def vprjpi(vin, projpl, invpl):
    """vprjpi(double [3] vin, double [NPLANE] projpl, double [NPLANE] invpl)"""
    return _cspice.vprjpi(vin, projpl, invpl)

def vproj(a, b):
    """vproj(double [3] a, double [3] b)"""
    return _cspice.vproj(a, b)

def vrel(v1, v2):
    """vrel(double [3] v1, double [3] v2) -> double"""
    return _cspice.vrel(v1, v2)

def vrelg(v1, v2):
    """vrelg(double * v1, double * v2) -> double"""
    return _cspice.vrelg(v1, v2)

def vrotv(v, axis, theta):
    """vrotv(double [3] v, double [3] axis, double theta)"""
    return _cspice.vrotv(v, axis, theta)

def vscl(s, v1):
    """vscl(double s, double [3] v1)"""
    return _cspice.vscl(s, v1)

def vsclg(s, v1):
    """vsclg(double s, double * v1)"""
    return _cspice.vsclg(s, v1)

def vsep(v1, v2):
    """vsep(double [3] v1, double [3] v2) -> double"""
    return _cspice.vsep(v1, v2)

def vsepg(v1, v2):
    """vsepg(double * v1, double * v2) -> double"""
    return _cspice.vsepg(v1, v2)

def vsub(v1, v2):
    """vsub(double [3] v1, double [3] v2)"""
    return _cspice.vsub(v1, v2)

def vsubg(v1, v2):
    """vsubg(double * v1, double * v2)"""
    return _cspice.vsubg(v1, v2)

def vtmv(v1, matrix):
    """vtmv(double [3] v1, double [3][3] matrix) -> double"""
    return _cspice.vtmv(v1, matrix)

def vtmvg(v1, matrix, v2):
    """vtmvg(double * v1, double * matrix, double * v2) -> double"""
    return _cspice.vtmvg(v1, matrix, v2)

def vupack(v):
    """vupack(double [3] v)"""
    return _cspice.vupack(v)

def vzero(v):
    """vzero(double [3] v) -> int"""
    return _cspice.vzero(v)

def vzerog(v):
    """vzerog(double * v) -> int"""
    return _cspice.vzerog(v)

def xf2eul(xform, axisa, axisb, axisc):
    """xf2eul(double [6][6] xform, int axisa, int axisb, int axisc)"""
    return _cspice.xf2eul(xform, axisa, axisb, axisc)

def xf2rav(xform):
    """xf2rav(double [6][6] xform)"""
    return _cspice.xf2rav(xform)

def xpose6(m1):
    """xpose6(double [6][6] m1)"""
    return _cspice.xpose6(m1)

def xpose(m1):
    """xpose(double [3][3] m1)"""
    return _cspice.xpose(m1)

def xposeg(matrix):
    """xposeg(double * matrix)"""
    return _cspice.xposeg(matrix)
# This file is compatible with both classic and new-style classes.


