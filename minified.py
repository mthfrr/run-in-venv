exec("M='pip'\nF='PATH'\nimport venv,sys,inspect as N\nfrom subprocess import check_call as O,getoutput as G\nfrom os.path import realpath as C,dirname as P,join as D,basename as H,isdir,splitext as Q\nfrom os import environ as A,execvp as R\nI=next(reversed(N.stack())).frame\nE=C(I.f_globals['__file__'])\nS=P(E)\nT=Q(H(E))[0]\nB=D(S,'.'+T+'.venv')\nif not isdir(B):A['P']=F;venv.create(B,with_pip=True)\nJ=D(B,'bin')\nK=C(sys.executable)\nif K!=C(D(J,H(K))):A.update({'VIRTUAL_ENV':B,F:J+':'+A[F]});R(E,sys.argv)\nL=I.f_locals['deps']\n[O([M,'install',*(B)])for B in(('--upgrade',M,'setuptools','wheel'),L)if'P'in A]\nU=G('pip freeze').split()\n[G('pip install '+A)for A in L if A not in U]")