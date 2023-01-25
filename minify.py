#!/usr/bin/env python3.9
deps = ("python-minifier==2.7.0", "cowsay==5.0")
# deps = ("python-minifier==2.7.0",)
import runfromvenv

import python_minifier
import base64
import zlib
import textwrap


def minify_all(x):
    return python_minifier.minify(
        x,
        None,
        remove_annotations=True,
        remove_pass=True,
        remove_literal_statements=True,
        combine_imports=True,
        hoist_literals=True,
        rename_locals=True,
        rename_globals=True,
        remove_object_base=True,
        convert_posargs_to_args=True,
    )


with open(f"runfromvenv.py", "rb") as f:
    code = f.read()
    print(f"init: {len(code)}")
    mini = minify_all(code)
    print(f"mini: {len(f'exec({repr(mini)})')}")
    print(textwrap.indent(mini, "  "))

SUBST_CHAR = "\\n"
assert not (SUBST_CHAR.encode("ascii") in code)
code = mini.replace("\n", "\\n").replace('"', '\\"')
code = f'exec("{code}")'  # .replace("{SUBST_CHAR}","\\n"))'
print(code)

# code = zlib.compress(code, 9)
# code = f"__import__('zlib').decompress({code})".encode("ascii")
# code = f"exec(bytes.fromhex('{code.hex()}'))"

print(f"after: {len(code)}")
exec(code)
with open("minified.py", "w") as f:
    f.write(code)
