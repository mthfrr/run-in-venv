#!/usr/bin/env python3.9
deps = ("cowsay",)
exec(
    """K='pip'G='PATH'import venv,sys,inspect as L,subprocess as Mfrom os.path import realpath as C,dirname as N,join as D,basename as H,isdir,splitext as Ofrom os import environ as A,execvp as PI=next(reversed(L.stack())).frameE=C(I.f_globals['__file__'])Q=N(E)R=O(H(E))[0]B=D(Q,f".{R}.venv")if not isdir(B):A['P']=G;venv.create(B,with_pip=True)J=D(B,'bin')F=C(sys.executable)if F!=C(D(J,H(F))):A.update({'VIRTUAL_ENV':B,G:f"{J}:{A[G]}"});P(E,sys.argv)if'P'in A:	for S in (('--upgrade',K,'setuptools','wheel'),I.f_locals['deps']):M.check_call([F,'-m',K,'install',*(S)])""".replace(
        "\v", "\n"
    )
)

import cowsay

cowsay.cow("it works")
