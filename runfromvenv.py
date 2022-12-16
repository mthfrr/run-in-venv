import venv as v, sys as s, os, inspect as i, subprocess as sp
from os.path import realpath as rp, dirname as dn, join as j, basename as bn, isdir, isfile
from os import environ as e, execvp as ex

pj_f=rp(next(reversed(i.stack())).frame.f_globals["__file__"])
pj_d=dn(pj_f)
v_d=j(pj_d, f".{bn(pj_d)}.venv")

if not isdir(v_d):
    e['P']=''
    v.create(v_d, False, False, True, True, None, True)

v_bin_d=j(v_d, "bin")
p=bn(rp(s.executable))

v_py = rp(j(v_bin_d, p))
if rp(s.executable) != v_py:
    e={**e,"VIRTUAL_ENV":v_d,"PATH":f"{v_bin_d}:{os.environ['PATH']}"}
    ex(pj_f, s.argv)

r = j(pj_d, "requirements.txt")
if isfile(r) and 'P' in e:
    for a in (('wheel',), ('-r', r)):
        sp.check_call([s.executable, '-m', 'pip', 'install', *a])
