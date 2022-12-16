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
import runfromvenv

import other_stuff

# do actual work
```

### Paste oneliner

At the beginning of your main python file **AND ONLY THERE**, paste the content
of `minified.py`

```py
I=__import__;exec(I('zlib').decompress(I('base64').a85decode(b'GhP$<9lo;J%#3*o?]fB6h%?5AViq3Z^\'^^$ZFqqc`WQOZ%C+N.BQk<mqo[T4nOTs]pT`fBN*:\'I)/"\'E>>HZp-YlsXcDj\'\\s6Du&hPqbFdO,Flc-A@K..<r26:tlcM=JI*E(mtrSW["=A&]b[[B&C\\7:uqANNT&,K:VZ"(8$-NR"f7QX#BMUhGu\\9Y?#ghPIW+bRWbRqe-GZCMR/<9)]<7KXMuaPe6+f8p1tn"OMqIbS;YghTIBD!ATkBM)k,qe0[K!LPA.I96Va5Y\'q:l42a=c^OS.6?b)Wto>t#`(LD*r?[0]DtbQ^2sDs3@%ZggDq(Blud-oQTO*KE,i2I!d_EAGF,"/%_];bfeQM3A[:]ErU[WOD3X%c]]1K*`J?DV>ndh8aCLqEA2eJ+_t"E:H]P!K>L5F.$=_97JbS?9;6fnA^3&=[K^;R?RG*GJn[ic[Y4]2WqC&,;&>VT9::mEQL7-LG@NM2YQ(i?;YqOl;_M60W+CTkiYgBMK6KX7q%Ec0;:G+iZg*e<O\'dSB_U#BiD0asU2\\H0I*;Njr+3S%')))

import other_stuff

# do actual work
```
