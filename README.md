# Run In Venv

## Why ?

I hate to have to remember to enter a venv before running a script.

## Features

- [x] Create a new venv if it doesn't exist
- [x] Enter the venv on start
- [x] Install dependencies on creation if `requirements.txt` is in the same
  directory as the script

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
I=__import__;exec(I('zlib').decompress(I('base64').a85decode(b'GhP#Q9lK#F&3[4H7ET3.Q15AUPs_3l;b@YV$UTs^\'6\'GZ=kfWLM#Y24Zs9\\XcSKLrN4hoX;%8UY!paqi"er"d)])ea^2WsZ\\Z0M!\\Vm8C?Fan`NR9ai)t8_!7TY_\\U64j`rNA%+b7=E.(Of>\\Q5\'Vn`]pl26^7.o[.rRW>Zm]]cU*m;Z[N0E1qac<FB:Q^GfBU/K_V+^Or%<^ePUr81_u/E<ELX?0?P+FL%-`_Oe#*mOJUc!QA$)W#(&g/aW$d*1/(S,i^HYuVKBcE+q3=<6krS$?.:m06P^2UY_IQ]Gn0QmpHq!;6iO4C3V*VP[\\cJ_k$DlFiLjpnAF.#*%>s)QFn/@<-TceJHqNRL9#oe!4:l@N$u.`rQu09]dUb=?I6]pUPITi4k4eX/fM2)6hOQgEdogo0+jK8gaJ-!N#62-S@"l"p_He1(D:WgFA:=*QrQYX&q,M)AD\'BK=KmpdR:.?9:pl^7uf/?CidK53m1L^ZLq]l8ki=2qXI`D:9b@Oi)h3^RElH9%NE1R.1Rr6lMr<"s:\\ao')))

import other_stuff

# do actual work
```
