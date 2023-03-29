#!/usr/bin/env python3.10
deps = ("cowsay",)
exec(
    "N='pip'\nM='VIRTUAL_ENV'\nG='PATH'\nF='P'\nimport venv,sys,inspect as O\nfrom subprocess import check_call as P,getoutput as Q\nfrom os.path import realpath as C,dirname as R,join as D,basename as H,isdir,splitext as S\nfrom os import environ as A,execvp as T\nI=next(reversed(O.stack())).frame\nE=C(I.f_globals['__file__'])\nU=R(E)\nV=S(H(E))[0]\nB=D(U,'.'+V+'.venv')\nif M!=B:\n	if not isdir(B):A[F]=G;venv.create(B,with_pip=True)\n	J=D(B,'bin');K=C(sys.executable)\n	if K!=C(D(J,H(K))):A.update({M:B,G:J+':'+A[G]});T(E,sys.argv)\n	L=I.f_locals['deps'];[P([N,'install',*(B)])for B in(('--upgrade',N,'setuptools','wheel'),L)if F in A];[Q('pip install '+B)for B in L if F in A]"
)

import cowsay

cowsay.cow("it works")
