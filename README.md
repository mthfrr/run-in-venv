# Run In Venv

## Why ?

I hate to have to remember to enter a venv before running a script.

## Features

When run in `myscript.py`

- [x] Create a new venv `.myscript.venv` if it doesn't exist
- [x] Enter the venv on start
- [x] Pip install -r `myscript.req` on creation if `myscript.req` exists

## Usage

### Import runfromvenv.py

At the beginning of your main python file **AND ONLY THERE**, import `runfromvenv.py`

```py
deps = ("cowsay",)
import runfromvenv

import cowsay

cowsay.cow("it works")
```

### Paste oneliner

At the beginning of your main python file **AND ONLY THERE**, paste the content
of `minified.py`

```py
deps = ("cowsay",)

exec("N='pip'\nM='VIRTUAL_ENV'\nG='PATH'\nF='P'\nimport venv,sys,inspect as O\nfrom subprocess import check_call as P,getoutput as Q\nfrom os.path import realpath as C,dirname as R,join as D,basename as H,isdir,splitext as S\nfrom os import environ as A,execvp as T\nI=next(reversed(O.stack())).frame\nE=C(I.f_globals['__file__'])\nU=R(E)\nV=S(H(E))[0]\nB=D(U,'.'+V+'.venv')\nif M!=B:\n	if not isdir(B):A[F]=G;venv.create(B,with_pip=True)\n	J=D(B,'bin');K=C(sys.executable)\n	if K!=C(D(J,H(K))):A.update({M:B,G:J+':'+A[G]});T(E,sys.argv)\n	L=I.f_locals['deps'];[P([N,'install',*(B)])for B in(('--upgrade',N,'setuptools','wheel'),L)if F in A];[Q('pip install '+B)for B in L if F in A]")

import cowsay

cowsay.cow("it works")
```
