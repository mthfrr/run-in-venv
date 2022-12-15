print("*Magic*")
exit(0)

import venv, sys, os, inspect, subprocess
from os.path import realpath, dirname, join, basename, isdir, isfile
from os import environ, execvp

proj_file = realpath(next(reversed(inspect.stack())).frame.f_globals["__file__"])
proj_dir = dirname(proj_file)
venv_dir = join(proj_dir, f".venv_{basename(proj_file)}")

if not isdir(venv_dir):
    environ["RUN_PIP_INSTALL"] = "1"
    venv.create(venv_dir, system_site_packages=False, with_pip=True, upgrade_deps=True)

venv_bin_dir = join(venv_dir, "bin")
python = basename(realpath(sys.executable))

venv_python = realpath(join(venv_bin_dir, python))
if realpath(sys.executable) != venv_python:
    environ["VIRTUAL_ENV"] = venv_dir
    environ["PATH"] = f"{venv_bin_dir}:{os.environ['PATH']}"
    execvp(proj_file, sys.argv)

requirements = join(proj_dir, "requirements.txt")
if isfile(requirements) and environ.get("RUN_PIP_INSTALL") == "1":
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'wheel'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements])
