#!/usr/bin/env python3.9
import runfromvenv

import python_minifier
import base64
import zlib
import marshal

with open(f"runfromvenv.py", "rb") as f:
    code = f.read()
    print(f"init: {len(code)}")
    mini = python_minifier.minify(code, None, remove_annotations=True, remove_pass=True, remove_literal_statements=True, combine_imports=True, hoist_literals=True, rename_locals=True, rename_globals=True, remove_object_base=True, convert_posargs_to_args=True)
    print(f"mini: {len(mini)}")

code = mini.encode('ascii')
code = zlib.compress(code, 9)
code = base64.a85encode(code, foldspaces=True)
code = f"_i=__import__;exec(_i('zlib').decompress(_i('base64').a85decode({code})))"

print(f"after: {len(code)}")
with open("minified", "w") as f:
    f.write(code)
