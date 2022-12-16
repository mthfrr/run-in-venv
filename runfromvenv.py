import venv, sys, inspect, subprocess
from os.path import realpath, dirname, join, basename, isdir, isfile, splitext
from os import environ, execvp

project_main_file = realpath(
    next(reversed(inspect.stack())).frame.f_globals["__file__"]
)
project_dir = dirname(project_main_file)
project_name = splitext(basename(project_main_file))[0]
venv_dir = join(project_dir, f".{project_name}.venv")

if not isdir(venv_dir):
    environ["P"] = "PATH"  # random value but reusing already aliased value
    # system_site_packages=False, clear=False, symlinks=False, upgrade=False, with_pip=False, prompt=None, upgrade_deps=False
    venv.create(venv_dir, with_pip=True)

venv_bin_dir = join(venv_dir, "bin")
e = realpath(sys.executable)

if e != realpath(join(venv_bin_dir, basename(e))):
    environ.update(
        {
            "VIRTUAL_ENV": venv_dir,
            "PATH": f"{venv_bin_dir}:{environ['PATH']}",
        }
    )
    execvp(project_main_file, sys.argv)

requirements = join(project_dir, f"{project_name}.req")
if isfile(requirements) and "P" in environ:
    for args in (("--upgrade", "pip", "setuptools", "wheel"), ("-r", requirements)):
        subprocess.check_call([e, "-m", "pip", "install", *args])
