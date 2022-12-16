#!/usr/bin/env python3.9
import runfromvenv

import python_minifier
import base64
import zlib


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
    # print(mini)

code = mini.encode("ascii")
code = zlib.compress(code, 9)
code = base64.a85encode(code, foldspaces=True)
code = f"I=__import__;exec(I('zlib').decompress(I('base64').a85decode({code})))"

print(f"after: {len(code)}")
exec(code)
with open("minified.py", "w") as f:
    f.write(code)
